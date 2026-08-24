"""
SDK version compatibility utilities for MLSentinel.

This module checks the installed MLSentinel SDK version against
the latest and minimum supported versions provided by the
MLSentinel backend.

The version check is designed to be non-blocking by default.
Network failures are silently ignored when ``silent=True``.
"""

import requests
from packaging.version import Version, InvalidVersion
from colorama import Fore, Style, init

from .version import __version__
from .config import VERSION_CHECK_URL, VERSION_CHECK_TIMEOUT
init(autoreset=True)
from .error_codes import ErrorCodes
from .exceptions import UnsupportedSDKVersionError


def _parse_version(v: str) -> tuple:
    """
    Convert a version string into a comparable tuple.

    Development and build suffixes are ignored for version
    comparison.

    Parameters
    ----------
    v : str
        Version string to parse.

    Returns
    -------
    tuple
        Numeric version components suitable for comparison.

    Examples
    --------
    >>> _parse_version("0.1.4")
    (0, 1, 4)

    >>> _parse_version("0.1.4.dev3")
    (0, 1, 4)

    >>> _parse_version("0.1.4+build")
    (0, 1, 4)

    Notes
    -----
    Development and build suffixes are intentionally ignored
    for simplicity.
    """

    core = v.split(".dev")[0].split("+")[0]
    return tuple(int(part) for part in core.split("."))


def check_sdk_version(silent: bool = True):
    """
    Check the installed SDK version against the backend.

    The MLSentinel backend provides the latest available SDK
    version and the minimum SDK version supported by the backend.

    Parameters
    ----------
    silent : bool, optional
        Controls how network failures are handled.

        ``True``
            Network failures are ignored and the version check
            is skipped.

        ``False``
            Network failures are allowed to propagate.

        Defaults to ``True``.

    Raises
    ------
    UnsupportedSDKVersionError
        Raised when the installed SDK version is lower than the
        minimum version supported by the MLSentinel backend.

    requests.exceptions.RequestException
        May be raised when ``silent=False`` and the version
        check request fails.

    Examples
    --------
    Perform a non-blocking version check:

    >>> check_sdk_version()

    Perform a version check that propagates network errors:

    >>> check_sdk_version(silent=False)

    Notes
    -----
    The default ``silent=True`` behavior ensures that an
    unavailable version-check service does not prevent the
    SDK from being initialized.
    """

    try:
        response = requests.get(
            VERSION_CHECK_URL,
            timeout=VERSION_CHECK_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()
        latest = data["info"]["version"]

        installed_version = Version(__version__)
        latest_version = Version(latest)

    except (requests.exceptions.RequestException, KeyError, ValueError, InvalidVersion):
        if silent:
            return
        raise

    installed_tuple = _parse_version(__version__)
    latest_tuple = _parse_version(latest)

    if installed_tuple < latest_tuple:
        print(
            f"{Fore.CYAN}[MLSentinel]{Style.RESET_ALL} " 
            f"{Fore.YELLOW}A newer SDK version is available!{Style.RESET_ALL}\n"
            f"  Installed: "
            f"{Fore.LIGHTBLACK_EX}{__version__}{Style.RESET_ALL}\n"
            f"  Latest:   "
            f"{Fore.YELLOW}{latest}{Style.RESET_ALL}\n"
            f"  Upgrade:  "
            f"{Fore.GREEN}pip install --upgrade mlsentinel{Style.RESET_ALL}\n"
        )