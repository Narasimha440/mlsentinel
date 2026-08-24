"""
Custom exceptions for the MLSentinel Python SDK.

This module defines the exception hierarchy used by MLSentinel
for structured and consistent error handling.

All MLSentinel-specific exceptions inherit from
:class:`MLSentinelError`, allowing users to catch either a
specific error or any MLSentinel SDK error.

Example
-------
Catch any MLSentinel SDK error:

    try:
        monitor.doc_report(...)
    except MLSentinelError as error:
        print(error)

Catch a specific error:

    try:
        monitor.doc_report(...)
    except InvalidAPIKeyError as error:
        print("Invalid API key:", error)
"""


class MLSentinelError(Exception):
    """
    Base exception for all MLSentinel SDK errors.

    This exception stores a machine-readable error code and a
    human-readable error message.

    Parameters
    ----------
    code : str
        Unique MLSentinel error code associated with the error.

    message : str
        Human-readable description of the error.

    Attributes
    ----------
    code : str
        Error code associated with the exception.

    message : str
        Human-readable error message.

    Examples
    --------
    >>> error = MLSentinelError("MLS001", "Invalid API key")
    >>> error.code
    'MLS001'

    >>> str(error)
    '[MLS001] Invalid API key'
    """

    def __init__(self, code: str, message: str):
        """
        Initialize an MLSentinel SDK exception.

        Parameters
        ----------
        code : str
            Unique error code.

        message : str
            Description of the error.
        """

        self.code = code
        self.message = message

        super().__init__(f"[{code}] {message}")

    def __str__(self):
        """
        Return the formatted error message.

        Returns
        -------
        str
            Error code followed by the human-readable message.
        """

        return f"[{self.code}] {self.message}"


class InvalidAPIKeyError(MLSentinelError):
    """
    Raised when the provided MLSentinel API key is invalid.

    This exception indicates that the API key supplied by the
    user could not be accepted by the MLSentinel platform.
    """

    pass


class AuthenticationError(MLSentinelError):
    """
    Raised when authentication with the MLSentinel platform fails.

    This exception represents authentication-related failures
    that prevent the SDK from accessing the requested resource.
    """

    pass


class MetricValidationError(MLSentinelError):
    """
    Raised when one or more model metrics fail validation.

    This may occur when metrics are missing, incorrectly formatted,
    contain invalid values, or do not satisfy the expected metric
    requirements.
    """

    pass


class ProjectValidationError(MLSentinelError):
    """
    Raised when the provided project name is invalid.

    The exception is used when a project identifier does not satisfy
    the validation requirements of the MLSentinel SDK or platform.
    """

    pass


class ModelValidationError(MLSentinelError):
    """
    Raised when the provided model name is invalid.

    The exception is used when a model identifier does not satisfy
    the validation requirements of the MLSentinel SDK or platform.
    """

    pass


class MLSentinalConnectionError(MLSentinelError):
    """
    Raised when the SDK cannot connect to the MLSentinel servers.

    This exception represents connection-related failures that
    prevent the SDK from communicating with the MLSentinel platform.
    """

    pass


class MLSentinalServerError(MLSentinelError):
    """
    Raised when the MLSentinel server returns an error.

    This exception represents server-side failures encountered
    while processing an SDK request.
    """

    pass


class UnsupportedSDKVersionError(MLSentinelError):
    """
    Raised when the installed SDK version is unsupported.

    This exception is raised when the installed MLSentinel SDK
    version does not meet the minimum version requirements of
    the MLSentinel backend.
    """

    pass