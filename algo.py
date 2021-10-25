import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime.now()

ticker = input("Enter Ticker Symbol : ")
stock = pdr.DataReader(ticker, 'yahoo')

plt.style.use("dark_background")

ma_50 = stock['50-day'] = stock['Adj Close'].rolling(50).mean()
ma_100 = stock['100-day'] = stock['Adj Close'].rolling(100).mean()

buy_signals = []
sell_signals = []
trigger = 0

for x in range(len(stock)):
	if ma_50.iloc[x] > ma_100.iloc[x] and trigger != 1:
		buy_signals.append(stock['Adj Close'].iloc[x])
		sell_signals.append(float('nan'))
		trigger = 1
	elif  ma_50.iloc[x] < ma_100.iloc[x] and trigger != -1:
		buy_signals.append(float('nan'))
		sell_signals.append(stock['Adj Close'].iloc[x])
		trigger = -1
	else:
		buy_signals.append(float('nan'))
		sell_signals.append(float('nan'))

print(stock)

stock['Buy Signals'] = buy_signals
stock['Sell Signals'] = sell_signals

plt.plot(stock['Adj Close'], label="Stock Price", color ="lightgray", zorder=2)
plt.plot(ma_50, label="50 Days MA", color ="#f7c325", linestyle = "--", zorder =1)
plt.plot(ma_100, label="100 Days MA", color ="#ed7f1f", linestyle = "--", zorder =1)
plt.scatter(stock.index, stock['Buy Signals'], label="Buy Signal", marker = "^",color ="#00ff00", lw=3, zorder=3)
plt.scatter(stock.index, stock['Sell Signals'], label="Sell Signal", marker = "v",color ="#ff0000", lw=3, zorder=3)
plt.legend(loc="upper left")
plt.show()
