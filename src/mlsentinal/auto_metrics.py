def detect_framework(model) -> str:
    module = type(model).__module__

    if "sklearn" in module: return "sklearn"
    if "xgboost" in module: return "xgboost"
    if "lightgbm" in module: return " lightgbm"
    if "torch" in module: return "pytorch"
    if "keras" in model or "tensorflow" in module: return "tensorflow"

    return "generic"

def auto_compute_metrics(model, X_test, y_test) -> dict:
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    y_pred = model.predict(X_test)

    return {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, average="weighted", zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, average="weighted", zero_division=0)),
        "f1_score": float(f1_score(y_test, y_pred, average="weighted", zero_division=0)),
    }