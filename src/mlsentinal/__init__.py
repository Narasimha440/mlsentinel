"""
MLSentinal SDK

The lightweight SDK which server the user model metrics to the MLSentinal Official Dashboard

"""

from .version import __version__
from .client import MLDoc

__all__ = [
    "MLDoc",
    "__version__",
]