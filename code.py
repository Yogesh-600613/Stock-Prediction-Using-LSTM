import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import datetime as dt

dataset = pd.read_csv(r'Google_Stock_Price_Train.csv', index_col="Date", parse_dates=True)

# print(dataset.head())
# print(dataset.isna().any())
# print(dataset.info())

plt.subplot(2, 1, 1)
dataset['Open'].plot(figsize=(16, 6))
plt.show()
