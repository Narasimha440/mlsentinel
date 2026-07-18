from mlsentinal import MLDoc

doctor = MLDoc("MDUsZx6ijZFeNg1GFqmcpihYdAm8smb7r2KXl1ypxjuaJpuKemVE403Dxl3J9khfOJm9aDQCaAmAMrIqQ7rJ3o1W8yPcIqud8ln8m95Da1sGEEhNXVwdI6Ne2lRAEkfQ")

doctor.doc_report(
    project="Spam detector",
    model = "Random forest",
    metrics = {
        "accuracy": 0.95,
        "precision": 0.94,
        "recall": 0.93,
        "f1_score": 0.935,
        "val_loss": 0.18
    }
)

print("SDK version:", doctor.version())