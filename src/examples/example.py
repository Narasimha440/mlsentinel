from mlsentinal import MLDoc
from mlsentinal.exceptions import MLSentinelError

monitor = MLDoc("mls_0233e1e75ba1fa850887caeb29ae39ca67e74bde87a5c121")

# try:


response = monitor.doc_report(
        project="MLSentinal",
        model="ResNet50",
        metrics={
            "accuracy": 0.50,
            "precision": 0.44,
            "recall": 0.23,
            "f1_score": 0.84,
            "roc_auc": 0.18,
            "val_loss": 0.56,
        },
    )

print(response)

# except MLSentinelError as e:
#     print(f"{e}")