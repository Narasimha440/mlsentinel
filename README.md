![MLSentinel logo](https://raw.githubusercontent.com/Narasimha440/mlsentinal/main/logo.png)

# MLSentinel SDK

[![PyPI](https://img.shields.io/pypi/v/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![Python](https://img.shields.io/pypi/pyversions/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/mlsentinel?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/mlsentinel)

MLSentinel SDK is the Python client for sending model evaluation reports and data-quality summaries to the MLSentinel platform. It keeps the workflow simple: validate locally, send with your API key, and get back a structured JSON response or a clear SDK error.

## Installation

The SDK supports Python 3.9 and newer.

Install from PyPI:

```bash
pip install mlsentinel
```

Or install from a local checkout while developing:

```bash
pip install .
```

## Quick Start

```python
from mlsentinal import MLDoc

client = MLDoc("YOUR_API_KEY")

response = client.doc_report(
    project="Spam Detector",
    model="Random Forest",
    metrics={
        "accuracy": 0.95,
        "precision": 0.94,
        "recall": 0.93,
        "f1_score": 0.935,
        "roc_auc": 0.98,
        "val_loss": 0.18,
    },
)

print(response)
print(client.version())
```

Keep API keys out of source control. In real projects, read them from environment variables or a secret manager instead of hard-coding them.

## What the SDK Does

MLSentinel SDK is designed to stay out of your way:

- validates `project`, `model`, and `metrics` before making a network request
- sends reports to the backend using the `X-API-Key` header
- returns the API response as JSON when the request succeeds
- raises SDK-specific exceptions when validation, authentication, network, or server handling fails
- can also generate and upload a data-quality summary from a pandas DataFrame

## Data Quality Reports

If you want a quick health snapshot of a dataset, the SDK can summarize it locally and send the result to the platform.

```python
import pandas as pd
from mlsentinal import MLDoc

df = pd.read_csv("creditcard.csv")

client = MLDoc("YOUR_API_KEY")
response = client.report_data_quality(
    project="Loan Prediction",
    model="ResNet50",
    dataframe=df,
)

print(response)
```

This feature requires `pandas` and `numpy`.

## Validation Rules

Every report expects a non-empty string for both `project` and `model`. The `metrics` argument must be a non-empty dictionary, and only the supported metrics below are accepted.

| Metric | Accepted value |
| --- | --- |
| `accuracy` | Number from `0` to `1` |
| `precision` | Number from `0` to `1` |
| `recall` | Number from `0` to `1` |
| `f1_score` | Number from `0` to `1` |
| `roc_auc` | Number from `0` to `1` |
| `val_loss` | Number greater than or equal to `0` |

Validation happens locally first, so malformed payloads are caught before a request leaves your machine.

## Errors

The SDK raises its own exception types so you can handle failures cleanly in one place.

```python
from mlsentinal import MLDoc
from mlsentinal.exceptions import MLSentinelError

client = MLDoc("YOUR_API_KEY")

try:
    client.doc_report(
        project="Spam Detector",
        model="Random Forest",
        metrics={"accuracy": 1.2},
    )
except MLSentinelError as error:
    print(error.code)
    print(error.message)
```

| Situation | Exception |
| --- | --- |
| Invalid project, model, or metrics | `ProjectValidationError`, `ModelValidationError`, `MetricValidationError` |
| Invalid API key | `InvalidAPIKeyError` |
| Authentication or authorization failure | `AuthenticationError` |
| Timeout, connection, or request failure | `MLSentinalConnectionError` |
| Unexpected API response or server failure | `MLSentinalServerError` |

## API Reference

### `MLDoc(api_key, check_version=True)`

Creates a client for the MLSentinel platform. The client can optionally check SDK compatibility during initialization.

### `client.doc_report(project, model, metrics)`

Validates and submits a model report. On success, it returns the JSON response from the backend.

### `client.report_data_quality(project, model, dataframe)`

Builds a local data-quality summary and submits it to the backend.

### `client.version()`

Returns the installed SDK version.

## Requirements

- Python 3.9+
- `requests` 2.31.0+

## License

MLSentinel is distributed under the [MIT License](LICENSE).

## Author

Created by [Adari Narasimha Dhoni](https://github.com/Narasimha440).
