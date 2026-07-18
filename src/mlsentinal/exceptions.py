"""
Custom made exceptions for MLSentinal SDK for efficient error handling
"""

class MLSentinalError(Exception):
    """
    Base exception
    """
    pass

class InvalidAPIKeyError(Exception):
    """
    Raised when entered API key was wrong
    """

    pass

class AuthenticationError(Exception):
    """
    When Authentication failes
    """

    pass

class MetricValidationError(Exception):
    """
    Raised one or more metrics
    """

    pass

class ProjectValidationError(Exception):
    """
    When project name is invalid
    """

    pass

class ModelValidationError(Exception):
    """
    When invalid model name
    """

    pass

class MLSentinalConnectionError(Exception):
    """
    When SDK could not connect the MLSentinal servers
    """

    pass

class MLSentinalServerError(Exception):
    """
    When server returns error
    """

    pass