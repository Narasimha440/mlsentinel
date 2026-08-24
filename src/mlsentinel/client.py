"""
Main public client for the MLSentinel Python SDK.

This module provides :class:`MLDoc`, the primary entry point for
interacting with the MLSentinel platform.

The client can be used to:

- Submit machine-learning model evaluation metrics.
- Analyze dataset quality locally.
- Submit data-quality summaries to MLSentinel.
- Retrieve the installed SDK version.
"""

import logging
import sys, time, threading
from typing import Any

from .data_quality import compute_data_quality_summary
from .models import DataQualityReport, Report
from .transport import Transport
from .auto_metrics import auto_compute_metrics
from .validators import (
    validate_metrics,
    validate_model,
    validate_project,
)
from .version import __version__
from .version_check import check_sdk_version


logger = logging.getLogger(__name__)


class MLDoc:
    """
    Main client for interacting with the MLSentinel platform.

    ``MLDoc`` is the primary public interface of the MLSentinel
    Python SDK. It handles validation, report creation, and
    communication with the MLSentinel API.

    Parameters
    ----------
    api_key : str
        API key used to authenticate requests with the
        MLSentinel platform.

    check_version : bool, optional
        Whether to check for a newer version of the SDK when
        initializing the client. Defaults to ``True``.

    Examples
    --------
    Create an MLSentinel client:

    >>> from mlsentinel import MLDoc
    >>> monitor = MLDoc("YOUR_API_KEY")

    Disable the automatic version check:

    >>> monitor = MLDoc(
    ...     "YOUR_API_KEY",
    ...     check_version=False,
    ... )
    """

    class _Spinner:
        def __init__(self, message):
            self.message = message
            self._stop = False

        def __enter__(self):
            def spin():
                frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
                i = 0
                while not self._stop:
                    sys.stdout.write(f"\r{frames[i % len(frames)]} {self.message}")
                    sys.stdout.flush()
                    time.sleep(0.08); i+= 1
            self._thread = threading.Thread(target=spin, daemon=True)
            self._thread.start()

            return self

        def __exit__(self, *args):
            self._stop = True
            self._thread.join()
            sys.stdout.write("\r✓" + self.message + " " * 10 + "\n")

    def auto_report(self, model, X_test, y_test):
        with self._Spinner("Computing metrics locally"):
            metrics = auto_compute_metrics(model, X_test, y_test)

        with self._Spinner("Uploading to MLSentinel"):
            transport = Transport(self.api_key)
            response = transport.send_report_no_names(metrics)

        return response
    def __init__(
        self,
        api_key: str,
        check_version: bool = True,
    ) -> None:
        """
        Initialize an MLSentinel client.

        Parameters
        ----------
        api_key : str
            API key used to authenticate with MLSentinel.

        check_version : bool, optional
            If ``True``, checks whether a newer version of the
            MLSentinel SDK is available. Defaults to ``True``.
        """

        self.api_key = api_key

        if check_version:
            check_sdk_version(silent=True)

        logger.debug("MLSentinel client initialized.")

    def doc_report(
        self,
        project: str,
        model: str,
        metrics: dict[str, Any],
    ) -> Any:
        """
        Submit a machine-learning model report to MLSentinel.

        The project name, model name, and metrics are validated
        locally before the report is sent to the MLSentinel API.

        Parameters
        ----------
        project : str
            Name of the MLSentinel project.

        model : str
            Name or identifier of the machine-learning model.

        metrics : dict[str, Any]
            Model evaluation metrics.

            Common metrics include:

            - ``accuracy``
            - ``precision``
            - ``recall``
            - ``f1_score``
            - ``val_loss``

            Example:

            .. code-block:: python

                {
                    "accuracy": 0.94,
                    "precision": 0.92,
                    "recall": 0.91,
                    "f1_score": 0.915,
                    "val_loss": 0.12,
                }

        Returns
        -------
        Any
            Response returned by the MLSentinel API.

        Raises
        ------
        ValueError
            If the project, model, or metrics fail validation.

        Examples
        --------
        >>> monitor.doc_report(
        ...     project="fraud-detection",
        ...     model="xgboost-v1",
        ...     metrics={
        ...         "accuracy": 0.94,
        ...         "precision": 0.92,
        ...         "recall": 0.91,
        ...         "f1_score": 0.915,
        ...         "val_loss": 0.12,
        ...     },
        ... )
        """

        logger.debug(
            "Validating model report: project=%s, model=%s",
            project,
            model,
        )

        validate_project(project)
        validate_model(model)
        validate_metrics(metrics)

        report = Report(
            project=project,
            model=model,
            metrics=metrics,
        )

        logger.debug(
            "Uploading model report: project=%s, model=%s",
            project,
            model,
        )

        transport = Transport(self.api_key)

        return transport.send_report(report)

    def report_data_quality(
        self,
        project: str,
        model: str,
        dataframe: Any,
    ) -> Any:
        """
        Analyze and submit a dataset quality report.

        Data-quality analysis is performed locally using the
        provided dataframe. MLSentinel receives the generated
        data-quality summary rather than the raw dataframe.

        Parameters
        ----------
        project : str
            Name of the MLSentinel project.

        model : str
            Name or identifier of the machine-learning model
            associated with the dataset.

        dataframe : Any
            Dataset to analyze. Typically a
            :class:`pandas.DataFrame`.

        Returns
        -------
        Any
            Response returned by the MLSentinel API.

        Examples
        --------
        >>> import pandas as pd
        >>> from mlsentinel import MLDoc

        >>> monitor = MLDoc("YOUR_API_KEY")

        >>> dataframe = pd.read_csv("dataset.csv")

        >>> monitor.report_data_quality(
        ...     project="fraud-detection",
        ...     model="xgboost-v1",
        ...     dataframe=dataframe,
        ... )
        """

        logger.debug(
            "Analyzing data quality locally: project=%s, model=%s",
            project,
            model,
        )

        summary = compute_data_quality_summary(dataframe)

        report = DataQualityReport(
            project=project,
            model=model,
            summary=summary,
        )

        logger.debug(
            "Uploading data-quality summary: project=%s, model=%s",
            project,
            model,
        )

        transport = Transport(self.api_key)

        return transport.send_data_quality_report(report)

    def version(self) -> str:
        """
        Return the installed MLSentinel SDK version.

        Returns
        -------
        str
            Current installed MLSentinel SDK version.

        Examples
        --------
        >>> monitor.version()
        '0.1.4.dev3'
        """

        return __version__