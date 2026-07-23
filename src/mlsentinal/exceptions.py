"""
Custom made exceptions for MLSentinal SDK for efficient error handling
"""

class MLSentinelError(Exception):
    """
    Base exception
    """
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

    def __str__(self):
        return f"[{self.code}] {self.message}"
    
    
class InvalidAPIKeyError(MLSentinelError):
    """
    Raised when entered API key was wrong
    """

    pass

class AuthenticationError(MLSentinelError):
    """
    When Authentication failes
    """

    pass

class MetricValidationError(MLSentinelError):
    """
    Raised one or more metrics
    """

    pass

class ProjectValidationError(MLSentinelError):
    """
    When project name is invalid
    """

    pass

class ModelValidationError(MLSentinelError):
    """
    When invalid model name
    """

    pass

class MLSentinalConnectionError(MLSentinelError):
    """
    When SDK could not connect the MLSentinal servers
    """

    pass

class MLSentinalServerError(MLSentinelError):
    """
    When server returns error
    """

    pass

class UnsupportedSDKVersionError(MLSentinelError):
    """
    Raised when installed SDK version is below the backend's required minimum.
    """
    pass