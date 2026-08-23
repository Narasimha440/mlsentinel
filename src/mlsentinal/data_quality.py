"""
Local data-quality analysis for the MLSentinel Python SDK.

This module provides utilities for analyzing pandas DataFrames
locally and generating compact data-quality summaries.

Raw dataframe contents are not uploaded by this module. Only the
generated summary is passed to the MLSentinel client for reporting.
"""

from typing import Any

try:
    from typing import TypedDict
except ImportError:  # pragma: no cover
    from typing_extensions import TypedDict


class ColumnQualitySummary(TypedDict, total=False):
    """
    Data-quality information collected for a single dataframe column.

    Attributes
    ----------
    dtype : str
        Pandas data type of the column.

    null_count : int
        Number of missing values in the column.

    null_percentage : float
        Percentage of values that are missing.

    unique_count : int
        Number of unique values in the column.

    mean : float
        Mean value for numeric columns.

    std : float
        Standard deviation for numeric columns.

    min : float
        Minimum value for numeric columns.

    max : float
        Maximum value for numeric columns.

    outlier_count : int
        Number of statistical outliers detected using the IQR method.

    outlier_percentage : float
        Percentage of non-null numeric values classified as outliers.

    top_value_ratio : float
        Proportion of rows containing the most frequent value for
        categorical or text columns.
    """


class DataQualitySummary(TypedDict):
    """
    Summary generated from a dataframe.

    Attributes
    ----------
    row_count : int
        Total number of rows.

    column_count : int
        Total number of columns.

    duplicate_row_count : int
        Number of duplicated rows.

    duplicate_row_percentage : float
        Percentage of rows that are duplicates.

    columns : dict[str, ColumnQualitySummary]
        Per-column data-quality statistics.
    """

    row_count: int
    column_count: int
    duplicate_row_count: int
    duplicate_row_percentage: float
    columns: dict[str, ColumnQualitySummary]


def compute_data_quality_summary(df: Any) -> DataQualitySummary:
    """
    Compute a local data-quality summary for a pandas DataFrame.

    The analysis is performed entirely in the local Python process.
    The original dataframe and its raw values are not sent to the
    MLSentinel platform by this function.

    The summary includes:

    - Total row and column counts.
    - Duplicate row counts.
    - Missing-value counts and percentages.
    - Unique-value counts.
    - Numeric statistics.
    - IQR-based outlier counts.
    - Most-common-value ratios for categorical/text columns.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame to analyze.

    Returns
    -------
    DataQualitySummary
        Dictionary containing dataset-level and column-level
        data-quality statistics.

    Raises
    ------
    ImportError
        If pandas is not installed.

    TypeError
        If the provided object is not a pandas DataFrame.

    Examples
    --------
    >>> import pandas as pd
    >>> from mlsentinel.data_quality import (
    ...     compute_data_quality_summary,
    ... )

    >>> df = pd.DataFrame({
    ...     "age": [21, 25, 30, None],
    ...     "city": ["Delhi", "Mumbai", "Delhi", "Delhi"],
    ... })

    >>> summary = compute_data_quality_summary(df)

    >>> summary["row_count"]
    4

    >>> summary["column_count"]
    2
    """

    try:
        import pandas as pd
    except ImportError as exc:
        raise ImportError(
            "Data quality checks require pandas. "
            "Install it with: pip install pandas"
        ) from exc

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "df must be a pandas DataFrame."
        )

    total_rows = len(df)

    columns_summary: dict[str, ColumnQualitySummary] = {}

    for column in df.columns:
        series = df[column]

        null_count = int(series.isnull().sum())
        unique_count = int(series.nunique())

        column_info: ColumnQualitySummary = {
            "dtype": str(series.dtype),
            "null_count": null_count,
            "null_percentage": (
                round((null_count / total_rows) * 100, 2)
                if total_rows > 0
                else 0.0
            ),
            "unique_count": unique_count,
        }

        if pd.api.types.is_numeric_dtype(series):
            clean = series.dropna()

            if not clean.empty:
                q1 = clean.quantile(0.25)
                q3 = clean.quantile(0.75)

                iqr = q3 - q1

                lower_bound = q1 - (1.5 * iqr)
                upper_bound = q3 + (1.5 * iqr)

                outlier_mask = (
                    (clean < lower_bound)
                    | (clean > upper_bound)
                )

                outlier_count = int(outlier_mask.sum())

                column_info.update(
                    {
                        "mean": round(float(clean.mean()), 4),
                        "std": (
                            round(float(clean.std()), 4)
                            if len(clean) > 1
                            else 0.0
                        ),
                        "min": round(float(clean.min()), 4),
                        "max": round(float(clean.max()), 4),
                        "outlier_count": outlier_count,
                        "outlier_percentage": round(
                            (outlier_count / len(clean)) * 100,
                            2,
                        ),
                    }
                )

        else:
            value_counts = series.value_counts(
                normalize=True,
                dropna=True,
            )

            column_info["top_value_ratio"] = (
                round(float(value_counts.iloc[0]), 4)
                if not value_counts.empty
                else 0.0
            )

        columns_summary[str(column)] = column_info

    duplicate_row_count = int(df.duplicated().sum())

    return {
        "row_count": total_rows,
        "column_count": len(df.columns),
        "duplicate_row_count": duplicate_row_count,
        "duplicate_row_percentage": (
            round(
                (duplicate_row_count / total_rows) * 100,
                2,
            )
            if total_rows > 0
            else 0.0
        ),
        "columns": columns_summary,
    }