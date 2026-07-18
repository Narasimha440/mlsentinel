"""
Handles communication with the MLSentinal Backend
"""

import requests


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

        headers["Authorization"] = f"Bearer {self.api_key}"

        payload = {
            "project": report.project,
            "model": report.model,
            "metrics": report.metrics
        }

        print("Headers: ", headers)
        print("Payload: ", payload)