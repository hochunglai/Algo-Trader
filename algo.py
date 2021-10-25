import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)
aapl = pdr.DataReader('AAPL', 'yahoo')

plt.style.use("dark_background")

ma_50 = aapl['50-day'] = aapl['Adj Close'].rolling(50).mean()
ma_100 = aapl['100-day'] = aapl['Adj Close'].rolling(100).mean()

plt.plot(aapl['Adj Close'], label="Stock Price", color ="lightgray")
plt.plot(ma_50, label="50 Days MA", color ="red")
plt.plot(ma_100, label="100 Days MA", color ="purple")

plt.legend(loc="upper left")
plt.show()
