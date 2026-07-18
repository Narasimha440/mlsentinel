"""
Data model used by the mlsentinal SDK
"""


from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Report:

    """
    Represents model report.
    """

    project: str
    model: str
    metrics: Dict[str, Any]


@dataclass
class ReportResponse:

    """
    Represents server response.
    """

    success: bool
    message: str
    report_id: str
    health_score: float