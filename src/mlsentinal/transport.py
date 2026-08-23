"""
HTTP transport layer for the MLSentinel Python SDK.

This module handles communication between the MLSentinel SDK and
the MLSentinel backend API.

The :class:`Transport` class is responsible for:

- Preparing authenticated HTTP requests.
- Sending model reports.
- Sending data-quality reports.
- Handling common network errors.
- Handling HTTP error responses.
- Converting valid JSON responses into Python objects.

The transport layer is an internal SDK component. Most users should
interact with the public :class:`mlsentinel.MLDoc` client instead.
"""

import requests

from .config import (
    BASE_URL,
    REQUEST_TIMEOUT,
    DEFAULT_HEADERS,
)
from .error_codes import ErrorCodes
from .exceptions import (
    AuthenticationError,
    InvalidAPIKeyError,
    MLSentinalConnectionError,
    MLSentinalServerError,
)


class Transport:
    """
    Handles HTTP communication with the MLSentinel API.

    ``Transport`` is responsible for sending authenticated requests
    to the MLSentinel backend and converting API/network failures
    into MLSentinel-specific exceptions.

    Parameters
    ----------
    api_key : str
        API key used to authenticate requests with the MLSentinel
        backend.

    Notes
    -----
    This class is primarily used internally by the SDK's public
    client and is not normally instantiated directly by users.
    """

    def __init__(self, api_key: str):
        """
        Initialize the HTTP transport.

        Parameters
        ----------
        api_key : str
            MLSentinel API key used for authentication.
        """

        self.api_key = api_key

    def send_report(self, report):
        """
        Send a model evaluation report to the MLSentinel backend.

        The report is converted into the API request payload and
        submitted to the model reporting endpoint.

        Parameters
        ----------
        report : Report
            Model report containing the project name, model name,
            and evaluation metrics.

        Returns
        -------
        dict
            JSON response returned by the MLSentinel backend.

        Raises
        ------
        MLSentinalConnectionError
            Raised when the request times out, the backend cannot
            be reached, the backend URL is invalid, or another
            network-related request error occurs.

        InvalidAPIKeyError
            Raised when the backend returns HTTP 401.

        AuthenticationError
            Raised when access to the requested resource is denied.

        MLSentinalServerError
            Raised when the backend returns an unsupported HTTP
            response, a server error, or an invalid JSON response.
        """

        headers = DEFAULT_HEADERS.copy()

        headers["X-API-Key"] = self.api_key

        payload = {
            "project": report.project,
            "model": report.model,
            "metrics": report.metrics,
        }

        try:
            response = requests.post(
                f"{BASE_URL}/api/report",
                headers=headers,
                json=payload,
                timeout=REQUEST_TIMEOUT,
            )

        except requests.exceptions.Timeout:
            raise MLSentinalConnectionError(
                ErrorCodes.REQUEST_TIME_OUT,
                f"Request timed out after {REQUEST_TIMEOUT} seconds.",
            )

        except requests.exceptions.ConnectionError:
            raise MLSentinalConnectionError(
                ErrorCodes.MLSENTINAL_CONNECTION_ERROR,
                "Unable to connect to the MLSentinal Backend.",
            )

        except requests.exceptions.InvalidURL:
            raise MLSentinalConnectionError(
                ErrorCodes.INVALID_BACKEND_URL,
                "The configured backend URL is invalid.",
            )

        except requests.exceptions.RequestException as e:
            raise MLSentinalConnectionError(
                ErrorCodes.UNKNOWN_NETWORK_ERROR,
                f"Unexpected error: {e}",
            )

        return self._handle_response(response)

    def send_report_no_names(self, metrics):
        headers = DEFAULT_HEADERS.copy()
        headers["X-API-Key"] = self.api_key

        payload = {
            "metrics": metrics,
        }

        try:
            response = requests.post(
                f"{BASE_URL}/api/report/auto",
                headers=headers,
                json=payload,
                timeout=REQUEST_TIMEOUT,
            )
        except requests.exceptions.Timeout:
            raise MLSentinalConnectionError(
                ErrorCodes.REQUEST_TIME_OUT,
                f"Request timed out after {REQUEST_TIMEOUT} seconds.",
            )

        except requests.exceptions.ConnectionError:
            raise MLSentinalConnectionError(
                ErrorCodes.MLSENTINAL_CONNECTION_ERROR,
                "Unable to connect to the MLSentinel Backend.",
            )

        except requests.exceptions.InvalidURL:
            raise MLSentinalConnectionError(
                ErrorCodes.INVALID_BACKEND_URL,
                "The configured backend URL is invalid.",
            )

        except requests.exceptions.RequestException as e:
            raise MLSentinalConnectionError(
                ErrorCodes.UNKNOWN_NETWORK_ERROR,
                f"Unexpected error: {e}",
            )

        return self._handle_response(response)

    def _handle_response(self, response):
        """
        Handle an HTTP response from the MLSentinel backend.

        The response status code is mapped to the appropriate
        MLSentinel SDK exception when an error occurs. Successful
        responses are decoded from JSON.

        Parameters
        ----------
        response : requests.Response
            HTTP response returned by the MLSentinel backend.

        Returns
        -------
        dict
            Parsed JSON response for successful requests.

        Raises
        ------
        InvalidAPIKeyError
            If the server returns HTTP 401.

        AuthenticationError
            If the server returns HTTP 403.

        MLSentinalServerError
            If the server returns HTTP 404, HTTP 429, a 5xx response,
            another unsuccessful response, or invalid JSON.
        """

        if response.status_code == 401:
            raise InvalidAPIKeyError(
                ErrorCodes.INVALID_API_KEY,
                "The provided API key is invalid or expired.",
            )

        if response.status_code == 403:
            raise AuthenticationError(
                ErrorCodes.ACCESS_DENIED,
                "Access denied. Check your account permissions.",
            )

        if response.status_code == 404:
            raise MLSentinalServerError(
                ErrorCodes.ENDPOINT_NOT_EXIST,
                "The requested API endpoint does not exist.",
            )

        if response.status_code == 429:
            raise MLSentinalServerError(
                ErrorCodes.RATE_LIMIT_EXCEEDED,
                "Rate limit exceeded. Please retry later.",
            )

        if response.status_code >= 500:
            raise MLSentinalServerError(
                ErrorCodes.INTERNAL_SERVER_ERROR,
                f"Server error (HTTP {response.status_code}).",
            )

        if not response.ok:
            try:
                detail = response.json()
            except ValueError:
                detail = response.text

            raise MLSentinalServerError(
                ErrorCodes.UNKNOWN_SERVER_ERROR,
                f"Unexpected response (HTTP {response.status_code}): {detail}.",
            )

        try:
            return response.json()

        except ValueError:
            raise MLSentinalServerError(
                ErrorCodes.SERVER_INVALID_RESPONSE,
                "Server returned a response that is not valid JSON.",
            )

    def send_data_quality_report(self, report):
        """
        Send a data-quality report to the MLSentinel backend.

        The data-quality report contains the project name, model name,
        and locally generated data-quality summary.

        Parameters
        ----------
        report : DataQualityReport
            Data-quality report containing the project, model, and
            generated summary.

        Returns
        -------
        dict
            JSON response returned by the MLSentinel backend.

        Raises
        ------
        MLSentinalConnectionError
            Raised when the request times out or the backend cannot
            be reached.

        MLSentinalServerError
            Raised when the backend returns an unsuccessful response
            or invalid JSON.
        """

        headers = DEFAULT_HEADERS.copy()

        headers["X-API-Key"] = self.api_key

        payload = {
            "project": report.project,
            "model": report.model,
            "summary": report.summary,
        }

        try:
            print("BASE_URL:", BASE_URL)
            print("REQUEST URL:", f"{BASE_URL}/api/data-quality")

            response = requests.post(
                f"{BASE_URL}/api/data-quality",
                headers=headers,
                json=payload,
                timeout=REQUEST_TIMEOUT,
            )

        except requests.exceptions.Timeout:
            raise MLSentinalConnectionError(
                ErrorCodes.REQUEST_TIME_OUT,
                f"Request timed out after {REQUEST_TIMEOUT} seconds.",
            )

        except requests.exceptions.ConnectionError:
            raise MLSentinalConnectionError(
                ErrorCodes.MLSENTINAL_CONNECTION_ERROR,
                "Unable to connect to the MLSentinel Backend.",
            )

        return self._handle_response(response)