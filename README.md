![LOGO](logo.png)

# MLSentinel

[![PyPI version](https://img.shields.io/pypi/v/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![Python](https://img.shields.io/pypi/pyversions/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

MLSentinel is a Python SDK for monitoring, validating, and analyzing Machine Learning models.

> 🚧 **Developer Preview**
>
> MLSentinel is currently under active development. This release provides the SDK architecture, validation system, data models, and transport layer. Backend integration and AI-powered analysis will be added in future releases.

---

## Features

- Clean Python SDK
- Input validation
- Report data models
- HTTP transport layer
- Simple developer API
- Lightweight and easy to integrate

---
## Reference
Check out the [PyPi Readme](https://pypi.org/project/mlsentinel/0.1.0.dev1/) for verification!1

## Installation

```bash
pip install mlsentinel
```

---

## Quick Start

```python
from mlsentinel import MLDoc

doctor = MLDoc("YOUR_API_KEY")

doctor.doc_report(
    project="Spam Detector",
    model="Random Forest",
    metrics={
        "accuracy": 0.95,
        "precision": 0.94,
        "recall": 0.93,
        "f1_score": 0.935,
        "val_loss": 0.18
    }
)
```

---

## Current SDK Architecture

```
Developer
      │
      ▼
MLDoc
      │
      ▼
Validators
      │
      ▼
Report Model
      │
      ▼
Transport
      │
      ▼
MLSentinel Backend (Coming Soon)
```

---

## Project Structure

```
src/
└── mlsentinel/
    ├── __init__.py
    ├── client.py
    ├── config.py
    ├── exceptions.py
    ├── models.py
    ├── transport.py
    ├── validators.py
    └── version.py
```

---

## Roadmap

- ✅ SDK Foundation
- ✅ Validation Engine
- ✅ Transport Layer
- ⏳ Backend API
- ⏳ AI Analysis Engine
- ⏳ Dashboard
- ⏳ Web Platform

---

## Requirements

- Python 3.9+
- requests

---

## Author

Adari Narasimha Dhoni

---

## License

This project is licensed under the MIT License.
