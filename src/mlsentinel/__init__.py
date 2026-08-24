"""
MLSentinel Python SDK.

A lightweight Python SDK for sending machine-learning model
metrics and data-quality summaries to the MLSentinel platform.

The public API is intentionally kept small. Most users only need
to import :class:`MLDoc` and use the installed SDK version when needed.

Example
-------
>>> from mlsentinel import MLDoc

>>> monitor = MLDoc("YOUR_API_KEY")

>>> monitor.doc_report(
...     project="fraud-detection",
...     model="xgboost-v1",
...     metrics={
...         "accuracy": 0.94,
...         "precision": 0.92,
...         "recall": 0.91,
...         "f1_score": 0.915,
...     },
... )
"""

from .client import MLDoc
from .version import __version__

__all__ = [
    "MLDoc",
    "__version__",
]