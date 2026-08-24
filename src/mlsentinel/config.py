"""
Configuration values used throughout the MLSentinel Python SDK.

This module centralizes the URLs, request timeouts, and default
HTTP headers used by the SDK when communicating with the
MLSentinel backend.
"""

# Base URL of the MLSentinel backend API.
BASE_URL = "https://api.mlsentinel.dev"

# Local development backend.
# BASE_URL = "http://127.0.0.1:8000"


# Endpoint used to check the installed SDK version against the
# versions supported by the MLSentinel backend.
VERSION_CHECK_URL = "https://pypi.org/pypi/mlsentinel/json"

# Maximum amount of time, in seconds, allowed for an SDK
# version-check request.
VERSION_CHECK_TIMEOUT = 5

# Maximum amount of time, in seconds, allowed for regular
# API requests.
REQUEST_TIMEOUT = 30

# Default HTTP headers sent with SDK API requests.
DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}