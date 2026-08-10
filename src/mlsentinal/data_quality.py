

from typing import Dict, Any


def compute_data_quality_summary(df) -> Dict[str, Any]:
    """
    Takes a pandas DataFrame and returns a small summary dict.
    Requires pandas — imported lazily so the SDK doesn't force
    this dependency on users who don't use this feature.
    """
    try:
        import pandas as pd
        import numpy as np
    except ImportError:
        raise ImportError(
            "Data quality checks require pandas and numpy. "
            "Install with: pip install pandas numpy"
        )

    total_rows = len(df)

    columns_summary = {}
    for col in df.columns:
        series = df[col]
        col_info = {
            "dtype": str(series.dtype),
            "null_count": int(series.isnull().sum()),
            "null_percentage": round(float(series.isnull().sum() / total_rows * 100), 2) if total_rows > 0 else 0.0,
            "unique_count": int(series.nunique()),
        }

        if pd.api.types.is_numeric_dtype(series):
            clean = series.dropna()
            if len(clean) > 0:
                q1, q3 = clean.quantile(0.25), clean.quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                outlier_count = int(((clean < lower_bound) | (clean > upper_bound)).sum())

                col_info.update({
                    "mean": round(float(clean.mean()), 4),
                    "std": round(float(clean.std()), 4) if len(clean) > 1 else 0.0,
                    "min": round(float(clean.min()), 4),
                    "max": round(float(clean.max()), 4),
                    "outlier_count": outlier_count,
                    "outlier_percentage": round(outlier_count / len(clean) * 100, 2),
                })
        else:
            # categorical/text column — top value frequency, useful for
            # spotting a column that suddenly became mostly one value
            value_counts = series.value_counts(normalize=True)
            col_info["top_value_ratio"] = round(float(value_counts.iloc[0]), 4) if len(value_counts) > 0 else 0.0

        columns_summary[col] = col_info

    return {
        "row_count": total_rows,
        "column_count": len(df.columns),
        "duplicate_row_count": int(df.duplicated().sum()),
        "duplicate_row_percentage": round(float(df.duplicated().sum() / total_rows * 100), 2) if total_rows > 0 else 0.0,
        "columns": columns_summary,
    }