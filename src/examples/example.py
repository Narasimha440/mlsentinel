from mlsentinal import MLDoc
from mlsentinal.exceptions import MLSentinelError

monitor = MLDoc("narasimha_9963111874")

try:


    response = monitor.doc_report(
        project="MLSentinal",
        model="ResNet50",
        metrics={
            "accuracy": 0.95,
            "precision": 0.94,
            "recall": 0.93,
            "f1_score": 0.94,
            "roc_auc": 0.98,
            "val_loss": 0.18,
        },
    )

    print(response)

except MLSentinelError as e:
    print(f"{e}")