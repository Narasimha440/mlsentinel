"""
Configuration values used throughout the SDK
"""

BASE_URL = "https://mlsentinel-backend.onrender.com"
# BASE_URL = "http://127.0.0.1:8000"

VERSION_CHECK_URL = f"{BASE_URL}/sdk/version"
VERSION_CHECK_TIMEOUT = 5

REQUEST_TIMEOUT = 30

DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}