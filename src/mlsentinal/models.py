"""
Data models used by the MLSentinel Python SDK.

This module defines the data structures used to represent model
reports, data-quality reports, and responses returned by the
MLSentinel platform.

The models are implemented using Python dataclasses to provide
simple, lightweight containers for structured SDK data.
"""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Report:
    """
    Represents a machine-learning model evaluation report.

    A ``Report`` contains the project and model identifiers along
    with the evaluation metrics that will be submitted to the
    MLSentinel platform.

    Attributes
    ----------
    project : str
        Name of the MLSentinel project associated with the report.

    model : str
        Name or identifier of the machine-learning model.

    metrics : Dict[str, Any]
        Dictionary containing the model evaluation metrics.

    Examples
    --------
    >>> report = Report(
    ...     project="fraud-detection",
    ...     model="xgboost-v1",
    ...     metrics={
    ...         "accuracy": 0.94,
    ...         "precision": 0.92,
    ...         "recall": 0.91,
    ...     },
    ... )
    """

    project: str
    model: str
    metrics: Dict[str, Any]


@dataclass
class ReportResponse:
    """
    Represents the response returned by the MLSentinel server.

    This model contains the result of a report submission, including
    whether the request was successful, a descriptive message, the
    generated report identifier, and the calculated model health
    score.

    Attributes
    ----------
    success : bool
        Indicates whether the report request was successfully
        processed.

    message : str
        Human-readable message returned by the MLSentinel server.

    report_id : str
        Unique identifier assigned to the submitted report.

    health_score : float
        Health score calculated for the submitted model report.

    Examples
    --------
    >>> response = ReportResponse(
    ...     success=True,
    ...     message="Report processed successfully",
    ...     report_id="report_123",
    ...     health_score=92.5,
    ... )

    >>> response.health_score
    92.5
    """

    success: bool
    message: str
    report_id: str
    health_score: float


@dataclass
class DataQualityReport:
    """
    Represents a dataset data-quality report.

    The report contains the project and model identifiers together
    with a summary generated from local data-quality analysis.

    Attributes
    ----------
    project : str
        Name of the MLSentinel project associated with the report.

    model : str
        Name or identifier of the machine-learning model associated
        with the dataset.

    summary : Dict[str, Any]
        Data-quality summary generated from the dataset.

    Notes
    -----
    The summary is generated locally by the SDK before being sent
    to the MLSentinel platform. The raw dataset itself is not stored
    inside this model.

    Examples
    --------
    >>> report = DataQualityReport(
    ...     project="fraud-detection",
    ...     model="xgboost-v1",
    ...     summary={
    ...         "row_count": 1000,
    ...         "column_count": 12,
    ...     },
    ... )
    """

    project: str
    model: str
    summary: Dict[str, Any]