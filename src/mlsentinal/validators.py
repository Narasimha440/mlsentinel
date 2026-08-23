"""
Validation utilities for the MLSentinel Python SDK.

This module provides validation functions used to verify project
names, model names, and model evaluation metrics before reports
are submitted to the MLSentinel platform.

Validation errors are reported using MLSentinel-specific exception
classes and error codes.
"""

from .error_codes import ErrorCodes

from .exceptions import (
    ProjectValidationError,
    ModelValidationError,
    MetricValidationError,
)


# Metrics currently supported by the MLSentinel SDK.
SUPPORTED_METRICS = {
    "accuracy",
    "precision",
    "recall",
    "f1_score",
    "roc_auc",
    "val_loss",
}


def validate_project(project: str):
    """
    Validate an MLSentinel project name.

    The project name must be a string and cannot be empty or
    contain only whitespace.

    Parameters
    ----------
    project : str
        Project name to validate.

    Raises
    ------
    ProjectValidationError
        Raised when the project name is not a string or when
        the project name is empty.

    Examples
    --------
    >>> validate_project("fraud-detection")

    >>> validate_project("")
    Traceback (most recent call last):
        ...
    ProjectValidationError: ...
    """

    if not isinstance(project, str):
        raise ProjectValidationError(
            ErrorCodes.PROJECT_NAME_INVALID,
            "Project name must be a string."
        )

    if not project.strip():
        raise ProjectValidationError(
            ErrorCodes.PROJECT_NAME_REQUIRED,
            "Project name connot be empty."
        )


def validate_model(model: str):
    """
    Validate an MLSentinel model name.

    The model name must be a string and cannot be empty or
    contain only whitespace.

    Parameters
    ----------
    model : str
        Model name to validate.

    Raises
    ------
    ModelValidationError
        Raised when the model name is not a string or when
        the model name is empty.

    Examples
    --------
    >>> validate_model("xgboost-v1")

    >>> validate_model("")
    Traceback (most recent call last):
        ...
    ModelValidationError: ...
    """

    if not isinstance(model, str):
        raise ModelValidationError(
            ErrorCodes.MODEL_NAME_INVALID,
            "Model name must be a string."
        )

    if not model.strip():
        raise ModelValidationError(
            ErrorCodes.MODEL_NAME_REQUIRED,
            "Model name cannot be empty."
        )


def validate_metrics(metrics: dict):
    """
    Validate model evaluation metrics.

    The metrics object must be a non-empty dictionary containing
    only metrics supported by the MLSentinel SDK.

    Supported metrics are:

    - ``accuracy``
    - ``precision``
    - ``recall``
    - ``f1_score``
    - ``roc_auc``
    - ``val_loss``

    Classification metrics must have values between ``0`` and ``1``.
    Validation loss may be any non-negative numeric value.

    Parameters
    ----------
    metrics : dict
        Dictionary containing model evaluation metrics.

    Raises
    ------
    MetricValidationError
        Raised when:

        - ``metrics`` is not a dictionary.
        - The metrics dictionary is empty.
        - An unsupported metric is provided.
        - A metric value is not numeric.
        - A classification metric is outside the range ``0`` to ``1``.
        - Validation loss is negative.

    Examples
    --------
    >>> validate_metrics({
    ...     "accuracy": 0.94,
    ...     "precision": 0.92,
    ...     "recall": 0.91,
    ...     "f1_score": 0.915,
    ... })

    Validation loss can be greater than 1:

    >>> validate_metrics({
    ...     "val_loss": 1.25,
    ... })
    """

    if not isinstance(metrics, dict):
        raise MetricValidationError(
            ErrorCodes.METRICS_MUST_DICT,
            "Metrics should be a dictionary."
        )

    if len(metrics) == 0:
        raise MetricValidationError(
            ErrorCodes.METRICS_REQUIRED,
            "Metrics dictionary cannot be empty."
        )

    for metric_name, value in metrics.items():

        if metric_name not in SUPPORTED_METRICS:
            raise MetricValidationError(
                ErrorCodes.METRIC_UNSUPPORTED,
                f"Unsupported Metric '{metric_name}'. "
                f"Supported metrics are "
                f"{', '.join(sorted(SUPPORTED_METRICS))}."
            )

        if not isinstance(value, (int, float)):
            raise MetricValidationError(
                ErrorCodes.METRIC_VALUE_BE_NUMERIC,
                f"{metric_name} must be numeric."
            )

        if metric_name != "val_loss":

            if value < 0 or value > 1:
                raise MetricValidationError(
                    ErrorCodes.METRIC_OUT_RANGE,
                    f"{metric_name} must be between 0 and 1."
                )

        else:

            if value < 0:
                raise MetricValidationError(
                    ErrorCodes.METRIC_OUT_RANGE,
                    "Validation loss cannot be negative."
                )