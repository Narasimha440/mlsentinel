<p align="center">
  <img src="https://raw.githubusercontent.com/Narasimha440/mlsentinal/main/logo.png" alt="MLSentinel logo" width="800">
</p>

<p align="center">
  Python SDK for monitoring machine learning models with MLSentinel.
</p>

<p align="center">
  <a href="https://mlsentinel.dev">Website</a> ·
  <a href="https://mlsentinel.dev/dashboard">Dashboard</a> ·
  <a href="https://pypi.org/project/mlsentinel/">PyPI</a> ·
  <a href="https://github.com/Narasimha440/mlsentinal">GitHub</a>
</p>

<p align="center">

[![PyPI](https://img.shields.io/pypi/v/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![Python](https://img.shields.io/pypi/pyversions/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/mlsentinel?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/mlsentinel)

</p>

MLSentinel is a Python SDK for sending machine learning model evaluation metrics and data-quality reports to the MLSentinel platform.

The SDK handles local validation, authentication, report submission, and API errors while keeping the integration simple.

You can use the SDK to:

- send model evaluation reports
- automatically associate reports with a model
- send data-quality reports
- monitor model health through the MLSentinel Dashboard
- handle validation, authentication, connection, and server errors

There are two main ways to send model evaluation reports:

- `auto_report()` — automatically uses the model associated with your API key.
- `doc_report()` — lets you provide the project and model manually.

---

## Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [MLSentinel Dashboard](#mlsentinel-dashboard)
- [Dashboard Setup](#dashboard-setup)
- [Creating an API Key](#creating-an-api-key)
- [Using the SDK](#using-the-sdk)
- [Auto Reports](#auto-reports)
- [Auto Report with a Trained Model](#auto-report-with-a-trained-model)
- [Using Environment Variables](#using-environment-variables)
- [Manual Reports](#manual-reports)
- [Auto Report vs Manual Report](#auto-report-vs-manual-report)
- [Data Quality Reports](#data-quality-reports)
- [Supported Metrics](#supported-metrics)
- [Validation](#validation)
- [Managing API Keys](#managing-api-keys)
- [Monitoring Models](#monitoring-models)
- [Multiple Models](#multiple-models)
- [Error Handling](#error-handling)
- [API Reference](#api-reference)
- [Requirements](#requirements)
- [Security](#security)
- [License](#license)
- [Author](#author)

---

## Installation

MLSentinel supports Python 3.9 and newer.

Install the latest version from PyPI:

```bash
pip install mlsentinel
```

To install the SDK from a local checkout while developing:

```bash
pip install .
```

---

## Quick Start

Import `MLDoc` and initialize the client using your MLSentinel API key.

```python
from mlsentinel import MLDoc

client = MLDoc("YOUR_API_KEY")
```

You can now send model evaluation reports to MLSentinel.

For production applications, do not hard-code your API key in your source code. Use an environment variable or a secret manager.

---

# MLSentinel Dashboard

The [MLSentinel Dashboard](https://mlsentinel.dev/dashboard) is the web interface for managing your machine learning monitoring projects.

The SDK is used from your Python application to send evaluation data to MLSentinel. The dashboard is used to configure your projects and models and monitor the results.

From the dashboard, you can:

- create and manage workspaces
- create projects
- add machine learning models
- create and manage API keys
- assign a default model to an API key
- view model health
- view evaluation history
- monitor model performance
- review detected issues
- review recommendations
- manage monitoring settings

Open the dashboard:

**[https://mlsentinel.dev](https://mlsentinel.dev)**

---

## Dashboard Setup

Before using `auto_report()`, create your workspace, project, model, and API key from the dashboard.

### Step 1: Sign in to MLSentinel

Open the [MLSentinel Signup](https://www.mlsentinel.dev/login?mode=signup) and sign in to your account.

After signing in, open your workspace.

---

### Step 2: Create a Workspace

Create a workspace for your machine learning projects.

For example:

```text
Workspace: My ML Projects
```
<video autoplay loop src="https://github.com/user-attachments/assets/5de2396d-56cc-4770-9943-ac4be3efa05e" width="100%" controls>
  Your browser does not support the video tag.
</video>


If you already have a workspace, you can use the existing one.

A workspace keeps your projects and models organized.

---

### Step 3: Create a Project

Open your workspace and create a project for the machine learning application you want to monitor.

For example:

```text
Project: Spam Detector
```
<video autoplay loop src="https://github.com/user-attachments/assets/cfe1eb92-84fa-4578-87dc-f3ae4d09942d" width="100%" controls>
  Your browser does not support the video tag.
</video>


The project contains the models you want to monitor.

---

### Step 4: Add Your Machine Learning Model

Open the project and add the model you want to monitor.

For example:

```text
Model: Random Forest
```
<video autoplay loop src="https://github.com/user-attachments/assets/a2aed00f-c27c-4616-9eae-77285fe4e9c1" width="100%" controls>
  Your browser does not support the video tag.
</video>


You can add multiple models to the same project.

For example:

```text
Spam Detector
├── Random Forest
├── XGBoost
└── Logistic Regression
```

---

### Step 5: Open API Keys

Open the [API Keys](https://www.mlsentinel.dev/dashboard/api-keys) section from the dashboard.

Click:

```text
Create API Key
```
<video autoplay loop src="https://github.com/user-attachments/assets/1a82d46b-0766-4840-9069-7d95b689e31b" width="100%" controls>
  Your browser does not support the video tag.
</video>

A form will appear for creating the API key.

---

### Step 6: Add an API Key Label

Enter a label that helps you identify how the key will be used.

For example:

```text
Production Monitoring
```

<video autoplay loop src="https://github.com/user-attachments/assets/71291ac9-57d8-4f10-b307-7f66e84fa163" width="100%" controls>
  Your browser does not support the video tag.
</video>

Other useful labels include:

```text
Development
Production
GitHub Actions
Local Testing
Model Evaluation
```

The label is only used to identify the API key.

---

### Step 7: Select the Default Model

Select the model that the API key should be associated with.

For example:

```text
Default Model: Random Forest
```
<video autoplay loop src="https://github.com/user-attachments/assets/7dcdc0b7-1429-4f6d-9fc5-14327ee3d7ef" width="100%" controls>
  Your browser does not support the video tag.
</video>

This is important when using `auto_report()`.

The selected model becomes the default model for that API key.

When the SDK sends an automatic report, MLSentinel uses the API key to determine which model should receive the report.

---

### Step 8: Create the API Key

Click **Create Key**.

MLSentinel will generate a new API key.

It will look similar to:

```text
mls_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
<video autoplay loop src="https://github.com/user-attachments/assets/368a1f4e-0cff-4006-9c5c-46e8f5e53186" width="100%" controls>
  Your browser does not support the video tag.
</video>

Copy the key and store it securely.

The API key should be treated as a secret.

Do not publish it on GitHub or include it directly in publicly accessible source code.

---

### Step 9: Install the SDK

Install MLSentinel in your Python project:

```bash
pip install mlsentinel
```

---

### Step 10: Initialize the SDK

Create an `MLDoc` client using the API key generated from the dashboard.

```python
from mlsentinel import MLDoc

client = MLDoc("YOUR_API_KEY")
```

Replace `YOUR_API_KEY` with the key generated from the dashboard.

---

### Step 11: Send Your First Report

Prepare your model evaluation metrics:

```python
metrics = {
    "accuracy": 0.95,
    "precision": 0.94,
    "recall": 0.93,
    "f1_score": 0.935,
    "roc_auc": 0.98,
    "val_loss": 0.18,
}
```

Send them using `auto_report()`:

```python
response = client.auto_report(
    metrics=metrics
)

print(response)
```

You do not need to provide the project or model name.

MLSentinel uses the default model associated with the API key.

---

### Auto Report Setup

This video demonstrates how to:

- install the SDK
- create an `MLDoc` client
- configure an API key
- evaluate a model
- send metrics using `auto_report()`

**Video:** `ADD_VIDEO_LINK_HERE`

---

### Model Monitoring

This video demonstrates how to:

- send model evaluation reports
- open the dashboard
- view model health
- review evaluation history
- review detected issues and recommendations

**Video:** `ADD_VIDEO_LINK_HERE`

> Replace `ADD_VIDEO_LINK_HERE` with your YouTube or other video URL when the videos are published.

---

# Auto Reports

`auto_report()` is the simplest way to send model evaluation metrics to MLSentinel.

You do not need to provide the project or model name with every report.

The API key already has a default model associated with it, so MLSentinel uses that model automatically.

### Create Your Metrics

Prepare the evaluation metrics from your model:

```python
metrics = {
    "accuracy": 0.95,
    "precision": 0.94,
    "recall": 0.93,
    "f1_score": 0.935,
    "roc_auc": 0.98,
    "val_loss": 0.18,
}
```

### Initialize the Client

```python
from mlsentinel import MLDoc

client = MLDoc("YOUR_API_KEY")
```

### Send the Report

```python
response = client.auto_report(
    metrics=metrics
)

print(response)
```

You do not need to provide:

```python
project="..."
model="..."
```

MLSentinel uses the default model associated with your API key.

---

## Auto Report with a Trained Model

You can use `auto_report()` directly after evaluating a machine learning model.

For example, using scikit-learn:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from mlsentinel import MLDoc


model = RandomForestClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


metrics = {
    "accuracy": accuracy_score(y_test, y_pred),

    "precision": precision_score(
        y_test,
        y_pred,
        average="weighted",
    ),

    "recall": recall_score(
        y_test,
        y_pred,
        average="weighted",
    ),

    "f1_score": f1_score(
        y_test,
        y_pred,
        average="weighted",
    ),
}


client = MLDoc("YOUR_API_KEY")

response = client.auto_report(
    metrics=metrics
)

print(response)
```

The metrics are calculated locally and then submitted to MLSentinel.

The backend uses the API key to find the associated default model and stores the report under that model.

---

# Using Environment Variables

Do not hard-code API keys in production applications.

Set your API key as an environment variable.

### Linux/macOS

```bash
export MLSENTINEL_API_KEY="your_api_key"
```

### Windows PowerShell

```powershell
$env:MLSENTINEL_API_KEY="your_api_key"
```

Then load the key in Python:

```python
import os

from mlsentinel import MLDoc


client = MLDoc(
    os.environ["MLSENTINEL_API_KEY"]
)
```

You can then send reports normally:

```python
response = client.auto_report(
    metrics={
        "accuracy": 0.95,
        "precision": 0.94,
        "recall": 0.93,
        "f1_score": 0.935,
    }
)

print(response)
```

---

# Manual Reports

Use `doc_report()` when you want to specify the project and model manually.

This is useful when the same API key is used to report metrics for different models or projects.

```python
from mlsentinel import MLDoc


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
```

Unlike `auto_report()`, `doc_report()` requires both the project and model.

---

# Auto Report vs Manual Report

| Feature | `auto_report()` | `doc_report()` |
| --- | --- | --- |
| Metrics required | Yes | Yes |
| Project required | No | Yes |
| Model required | No | Yes |
| Default model required | Yes | No |
| Model selected automatically | Yes | No |
| Best for | Monitoring one configured model | Reporting to different models |

For most integrations where one API key belongs to one model, `auto_report()` is the simpler option.

---

# What the SDK Does

MLSentinel handles the common work required to communicate with the MLSentinel platform.

The SDK:

- validates project, model, and metric information
- validates metrics locally before sending requests
- authenticates requests using your API key
- sends reports to the MLSentinel backend
- returns successful API responses as JSON
- converts API failures into SDK-specific exceptions
- supports automatic model association with `auto_report()`
- supports manual reports with `doc_report()`
- generates and uploads data-quality summaries from pandas DataFrames

Validation happens locally first whenever possible, so invalid input can be detected before a request is sent.

---

# Data Quality Reports

MLSentinel can generate a summary of a pandas DataFrame and send the result to the platform.

This can be useful for checking the quality of data being used by a model.

```python
import pandas as pd

from mlsentinel import MLDoc


df = pd.read_csv("creditcard.csv")

client = MLDoc("YOUR_API_KEY")

response = client.report_data_quality(
    project="Loan Prediction",
    model="Random Forest",
    dataframe=df,
)

print(response)
```

The data-quality feature requires:

```text
pandas
numpy
```

The data-quality summary is generated locally before being submitted to MLSentinel.

---

# Supported Metrics

MLSentinel supports the following model evaluation metrics.

| Metric | Accepted value |
| --- | --- |
| `accuracy` | Number from `0` to `1` |
| `precision` | Number from `0` to `1` |
| `recall` | Number from `0` to `1` |
| `f1_score` | Number from `0` to `1` |
| `roc_auc` | Number from `0` to `1` |
| `val_loss` | Number greater than or equal to `0` |

Example:

```python
metrics = {
    "accuracy": 0.95,
    "precision": 0.94,
    "recall": 0.93,
    "f1_score": 0.935,
}
```

Metric values are validated before the report is submitted.

---

# Validation

For `doc_report()`, both `project` and `model` must be non-empty strings.

```python
client.doc_report(
    project="Spam Detector",
    model="Random Forest",
    metrics={
        "accuracy": 0.95,
    },
)
```

For `auto_report()`, project and model names are not required.

```python
client.auto_report(
    metrics={
        "accuracy": 0.95,
    }
)
```

In both cases, `metrics` must be a non-empty dictionary containing supported metrics with valid values.

Invalid input is rejected locally before the request is sent.

---

# API Keys and Default Models

Every API key used with `auto_report()` must have a default model.

The default model is selected when the API key is created from the MLSentinel Dashboard.

For example:

```text
Label: Production Monitoring
Default Model: Random Forest
```

When the key is used:

```python
from mlsentinel import MLDoc

client = MLDoc("YOUR_API_KEY")

client.auto_report(
    metrics={
        "accuracy": 0.94,
        "precision": 0.93,
        "recall": 0.92,
        "f1_score": 0.925,
    }
)
```

MLSentinel automatically sends the report to the model associated with the API key.

If an API key does not have a default model, `auto_report()` cannot determine which model should receive the metrics.

---

# Managing API Keys

API keys can be managed from the [MLSentinel APIKeys](https://mlsentinel.dev/dashboard/api-keys).

You can:

- create new API keys
- give keys meaningful labels
- select a default model
- view existing API keys
- revoke keys that are no longer needed

When a key is no longer required, revoke it from the dashboard.

A revoked API key can no longer be used to authenticate requests to MLSentinel.

---

# Monitoring Models

After reports are submitted through the SDK, open the [MLSentinel Monitoring](https://mlsentinel.dev/dashboard/monitoring) to monitor the associated model.

The dashboard provides information about your model's evaluation history and health.

You can use it to review:

- current model health
- evaluation metrics
- previous model runs
- performance changes
- detected issues
- rule-based warnings
- recommendations

You can continue sending reports from your training or evaluation pipeline and use the dashboard as the central place to monitor your models.

---

# Multiple Models

You can monitor multiple models by creating separate API keys and assigning each key to its corresponding default model.

For example:

```text
Production API Key
→ Random Forest

Development API Key
→ XGBoost

Testing API Key
→ Logistic Regression
```

Each application can then use its own API key:

```python
from mlsentinel import MLDoc

client = MLDoc("YOUR_API_KEY")

client.auto_report(
    metrics={
        "accuracy": 0.95,
        "precision": 0.94,
        "recall": 0.93,
        "f1_score": 0.935,
    }
)
```

The SDK does not need to specify the model because the API key already has a default model configured.

---

# Error Handling

The SDK provides its own exception types so applications can handle MLSentinel failures cleanly.

```python
from mlsentinel import MLDoc
from mlsentinel.exceptions import MLSentinelError


client = MLDoc("YOUR_API_KEY")

try:
    response = client.auto_report(
        metrics={
            "accuracy": 1.2,
        }
    )

except MLSentinelError as error:
    print(error.code)
    print(error.message)
```

For example, an accuracy value of `1.2` is invalid because accuracy must be between `0` and `1`.

## SDK Exceptions

| Situation | Exception |
| --- | --- |
| Invalid project | `ProjectValidationError` |
| Invalid model | `ModelValidationError` |
| Invalid metrics | `MetricValidationError` |
| Invalid API key | `InvalidAPIKeyError` |
| Authentication or authorization failure | `AuthenticationError` |
| Timeout or connection failure | `MLSentinalConnectionError` |
| Unexpected API response | `MLSentinalServerError` |
| Backend server failure | `MLSentinalServerError` |

You can catch specific exceptions when different failures need different handling.

---

# API Reference

## `MLDoc(api_key, check_version=True)`

Creates an MLSentinel client.

```python
client = MLDoc(
    "YOUR_API_KEY"
)
```

### Parameters

- `api_key` — MLSentinel API key.
- `check_version` — enables or disables SDK compatibility checking.

---

## `client.auto_report(metrics)`

Automatically submits model evaluation metrics using the default model associated with the API key.

```python
response = client.auto_report(
    metrics={
        "accuracy": 0.95,
        "precision": 0.94,
        "recall": 0.93,
        "f1_score": 0.935,
    }
)
```

### Parameters

- `metrics` — dictionary containing supported model evaluation metrics.

The API key must have a default model associated with it.

---

## `client.doc_report(project, model, metrics)`

Submits a report while manually specifying the project and model.

```python
response = client.doc_report(
    project="Spam Detector",
    model="Random Forest",
    metrics={
        "accuracy": 0.95,
    },
)
```

### Parameters

- `project` — MLSentinel project name.
- `model` — model name.
- `metrics` — dictionary containing model evaluation metrics.

---

## `client.report_data_quality(project, model, dataframe)`

Generates a local data-quality summary from a pandas DataFrame and submits it to MLSentinel.

```python
response = client.report_data_quality(
    project="Loan Prediction",
    model="Random Forest",
    dataframe=df,
)
```

### Parameters

- `project` — MLSentinel project name.
- `model` — model name.
- `dataframe` — pandas DataFrame to analyze.

---

## `client.version()`

Returns the installed MLSentinel SDK version.

```python
print(client.version())
```

---

# Requirements

MLSentinel requires:

- Python 3.9 or newer
- `requests` 2.31.0 or newer

Data-quality features also require:

- `pandas`
- `numpy`

---

# Security

Treat your MLSentinel API key like a password.

Do not expose API keys in:

- GitHub repositories
- public documentation
- frontend applications
- screenshots
- source code
- public logs

Do not do this in production:

```python
client = MLDoc("mls_your_real_api_key_here")
```

Instead, use an environment variable:

```python
import os

from mlsentinel import MLDoc


client = MLDoc(
    os.environ["MLSENTINEL_API_KEY"]
)
```

If an API key is accidentally exposed, revoke it from the [MLSentinel Dashboard](https://mlsentinel.dev) and create a new one.

---

# Links

- **Website:** https://mlsentinel.dev
- **Dashboard:** https://mlsentinel.dev/dashboard
- **PyPI:** https://pypi.org/project/mlsentinel/
- **GitHub:** https://github.com/Narasimha440/mlsentinal

---

# License

MLSentinel is distributed under the [MIT License](LICENSE).

---

# Author

Created by [Adari Narasimha Dhoni](https://github.com/Narasimha440).