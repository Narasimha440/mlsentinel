![MLSentinel logo](https://raw.githubusercontent.com/Narasimha440/mlsentinal/main/logo.png)

# MLSentinel

[![PyPI](https://img.shields.io/pypi/v/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![Python](https://img.shields.io/pypi/pyversions/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/mlsentinel?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/mlsentinel)

**Validate and submit machine-learning evaluation metrics from Python.**

MLSentinel is a lightweight Python SDK for sending model evaluation reports to the MLSentinel platform. It validates report data locally, authenticates requests with your API key, and returns the platform response as JSON.

> **Developer preview — v0.1.3.dev3**
>
> This pre-release focuses on reliable report submission: local validation, HTTP transport, API-key authentication, and actionable SDK errors. Analysis and dashboard features are planned for later releases.

## Installation

MLSentinel supports Python 3.9 and later.

```bash
pip install mlsentinel
```

For this development build, install from a local checkout:

```bash
pip install .
```

## Quick start

Create an API key in the MLSentinel platform, then submit a report:

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
print(client.version())  # 0.1.3.dev3
```

Keep API keys out of source control. In production, load the key from your secret manager or environment rather than embedding it in code.

## What happens when you submit a report

```text
Your application
      │
      ▼
MLDoc.doc_report(...)
      │
      ├─ Local input validation
      │
      └─ HTTP request with X-API-Key
                    │
                    ▼
            MLSentinel API
                    │
                    ▼
            JSON response or SDK exception
```

## Supported metrics and validation

All reports require a non-empty string for both `project` and `model`. The `metrics` argument must be a non-empty dictionary containing only the supported metrics below.

| Metric | Accepted value |
| --- | --- |
| `accuracy` | Number from `0` to `1` |
| `precision` | Number from `0` to `1` |
| `recall` | Number from `0` to `1` |
| `f1_score` | Number from `0` to `1` |
| `roc_auc` | Number from `0` to `1` |
| `val_loss` | Number greater than or equal to `0` |

Validation occurs before a network request is made, helping you catch malformed reports early.

## Error handling

MLSentinel raises SDK-specific exceptions with stable error codes. Catch the common base class when you want one error path for validation, authentication, network, and server failures.

```python
from mlsentinal import MLDoc
from mlsentinal.exceptions import MLSentinalError

client = MLDoc("YOUR_API_KEY")

try:
    client.doc_report(
        project="Spam Detector",
        model="Random Forest",
        metrics={"accuracy": 1.2},
    )
except MLSentinalError as error:
    print(error.code)     # for example: MLS026
    print(error.message)  # accuracy must be between 0 and 1.
```

| Category | Exception |
| --- | --- |
| Invalid project, model, or metrics | `ProjectValidationError`, `ModelValidationError`, `MetricValidationError` |
| Invalid API key | `InvalidAPIKeyError` |
| Authentication or authorization failure | `AuthenticationError` |
| Timeout, connection, or request error | `MLSentinalConnectionError` |
| Unexpected API response or server error | `MLSentinalServerError` |

## Version 0.1.3.dev3

This development release adds and improves:

- Standardized SDK error codes for validation, network, authentication, and server failures.
- Clearer exception messages for unsupported and invalid metric values.
- HTTP report transport with API-key authentication through the `X-API-Key` header.
- Timeout and connection-error handling.
- Local validation of projects, models, and supported evaluation metrics.

## API reference

### `MLDoc(api_key)`

Creates a client authenticated with the supplied API key.

### `client.doc_report(project, model, metrics)`

Validates and submits a model report. On success, it returns the JSON body returned by the MLSentinel API. On failure, it raises an `MLSentinalError` subclass.

### `client.version()`

Returns the installed SDK version.

## Requirements

- Python 3.9+
- `requests` 2.31.0+

## Roadmap

- AI-assisted model analysis and health reports
- Performance recommendations and diagnostics
- Dashboard and report history
- Model monitoring and drift detection
- CI/CD integrations

## Contributing

Contributions are welcome. Please open an issue to discuss significant changes, then submit a focused pull request with tests or examples where appropriate.

## License

MLSentinel is distributed under the [MIT License](LICENSE).

## Author

Created by [Adari Narasimha Dhoni](https://github.com/Narasimha440).
