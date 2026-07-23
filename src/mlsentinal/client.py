"""
Main client for serving to the Platform
"""

from .version import __version__
from .models import Report
from .transport import Transport
from .version_check import check_sdk_version
from .validators import (
    validate_project,
    validate_metrics,
    validate_model,
)

class MLDoc:
    """
    Main SDK client
    """

    def __init__(self, api_key: str, check_version: bool = True):
        self.api_key = api_key

        if check_version:
            check_sdk_version(silent=True)

        

    def doc_report(self, project: str, model: str, metrics: dict):

        """
        Validates the details first.
        """

        print("Validating details...")

        validate_project(project)
        validate_model(model)
        validate_metrics(metrics)

        """
        Prints the details....
        """

        report = Report(
            project=project,
            model=model,
            metrics=metrics
        )

        print("Uploading Project...")

        transport = Transport(self.api_key)
        response = transport.send_report(report)

        return response


    
    def version(self):
        return __version__