"""
Handles communication with the MLSentinal Backend
"""
import requests

from .error_codes import ErrorCodes
from .exceptions import (
    InvalidAPIKeyError,
    AuthenticationError,
    MLSentinalConnectionError,
    MLSentinalServerError,
)

from .config import (
    BASE_URL,
    REQUEST_TIMEOUT,
    DEFAULT_HEADERS
)

class Transport:
    """
    Handles HTTP communication with the MLSentinal API.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def send_report(self, report):
        """
        Send a report to the MLSentinal Backend
        """

        headers = DEFAULT_HEADERS.copy()

        headers["X-API-Key"] = self.api_key

        payload = {
            "project": report.project,
            "model": report.model,
            "metrics": report.metrics
        }

        try:
            response = requests.post(
                f"{BASE_URL}/api/report",
                headers=headers,
                json=payload,
                timeout=REQUEST_TIMEOUT
            )

        except requests.exceptions.Timeout:
            raise MLSentinalConnectionError(
                ErrorCodes.REQUEST_TIME_OUT,
                f"Request timed out after {REQUEST_TIMEOUT} seconds."
            )
        
        except requests.exceptions.ConnectionError:
            raise MLSentinalConnectionError(
                ErrorCodes.MLSENTINAL_CONNECTION_ERROR,
                "Unable to connect to the MLSentinal Backend."
            )
        
        except requests.exceptions.InvalidURL:
            raise MLSentinalConnectionError(
                ErrorCodes.INVALID_BACKEND_URL,
                "The configured backend URL is invalid."
            )
        
        except requests.exceptions.RequestException as e:
            raise MLSentinalConnectionError(
                ErrorCodes.UNKNOWN_NETWORK_ERROR,
                f"Unexpected error: {e}"
            )

        return self._handle_response(response)
    
    def _handle_response(self, response):

        if response.status_code == 401:
            raise InvalidAPIKeyError(
                ErrorCodes.INVALID_API_KEY,
                "The provided API key is invalid or expired."
            )
        
        if response.status_code == 403:
            raise AuthenticationError(
                ErrorCodes.ACCESS_DENIED,
                "Access denied. Check your account permissions."
            )
        
        if response.status_code == 404:
            raise MLSentinalServerError(
                ErrorCodes.ENDPOINT_NOT_EXIST,
                "The requested API endpoint does not exist."
            )
        
        if response.status_code == 429:
            raise MLSentinalServerError(
                ErrorCodes.RATE_LIMIT_EXCEEDED,
                "Rate limit exceeded. Please retry later."
            )
        
        if response.status_code >= 500:
            raise MLSentinalServerError(
                ErrorCodes.INTERNAL_SERVER_ERROR,
                f"Server error (HTTP {response.status_code})."
            )
        
        if not response.ok:
            raise MLSentinalServerError(
                ErrorCodes.UNKNOWN_SERVER_ERROR,
                f"Unexpected response (HTTP {response.status_code})."
            )
        
        try:
            return response.json()
        except ValueError:
            raise MLSentinalServerError(
                ErrorCodes.SERVER_INVALID_RESPONSE,
                "Server returned a response that is not valid JSON."
            )

    def send_data_quality_report(self, report):
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
                timeout=REQUEST_TIMEOUT
            )
        except requests.exceptions.Timeout:
            raise MLSentinalConnectionError(ErrorCodes.REQUEST_TIME_OUT, f"Request timed out after {REQUEST_TIMEOUT} seconds.")
        except requests.exceptions.ConnectionError:
            raise MLSentinalConnectionError(ErrorCodes.MLSENTINAL_CONNECTION_ERROR, "Unable to connect to the MLSentinel Backend.")

        return self._handle_response(response)