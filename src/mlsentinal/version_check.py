"""
Checks installed SDK version against the MLSentinel backend's
latest/minimum supported version.
"""

import requests

from .version import __version__
from .config import VERSION_CHECK_URL, VERSION_CHECK_TIMEOUT
from .error_codes import ErrorCodes
from .exceptions import UnsupportedSDKVersionError

def _parse_version(v: str) -> tuple:
    """
    Converts '0.1.4' -> (0, 1, 4) for comparison.
    Ignores dev/pre-release suffixes for simplicity.
    """

    core = v.split(".dev")[0].split("+")[0]
    return tuple(int(part) for part in core.split("."))

def check_sdk_version(silent: bool = True):
    """
    Calls the backend to check installed version against latest/minimum.

    silent=True:  never raises on network failure, just skips the check.
    silent=False: raises MLSentinalConnectionError on network failure.
    """

    try:
        response = requests.get(VERSION_CHECK_URL, timeout=VERSION_CHECK_TIMEOUT)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        if silent:
            return
        raise

    latest = data.get("latest")
    minimum = data.get("minimum")
    message = data.get("message", "")

    installed_tuple = _parse_version(__version__)

    if minimum:
        minimum_tuple = _parse_version(minimum)
        if installed_tuple < minimum_tuple:
            raise UnsupportedSDKVersionError(
                ErrorCodes.UNSUPPORT_API_VERSION,
                f"Installed MLSentinel SDK version {__version__} is below the minimum"
                f"required version {minimum}. Please upgrade: "
                f"pip install --upgrade mlsentinel"
            )

        if latest:
            latest_tuple = _parse_version(latest)
            if installed_tuple < latest_tuple:
                print(
                    f"[MLSentinel] A newer SDK version is available: {latest} "
                    f"(installed: {__version__}). {message}"
                )