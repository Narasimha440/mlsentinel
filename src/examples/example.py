# mls_855bffd0f743d073c18e7b9783942a8d8e1039b330a4011a

import pandas as pd
from mlsentinal import MLDoc

df = pd.read_csv("creditcard.csv")

monitor = MLDoc("mls_855bffd0f743d073c18e7b9783942a8d8e1039b330a4011a")
response = monitor.report_data_quality(project="loan prediction", model="ResNet50", dataframe=df)
print(response)