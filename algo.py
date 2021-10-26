import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime
import yfinance

plt.style.use("dark_background")

ticker = str(input("Enter Ticker Symbol : "))
		

def makeplot():
	
	start = datetime.datetime(2021, 10, 25)
	end = datetime.datetime.now()


	stock = yfinance.download(tickers= ticker, period='1d', interval='1m')
	print(stock)
	

	plt.plot(stock['Adj Close'], label="Stock Price", color ="lightgray", zorder=2)

	plt.legend(loc="upper left")
	plt.show()

makeplot()


"""
u_ma1 = int(input("Enter First Moving Average : "))
u_ma2 = int(input("Enter Second Moving Average : "))

ma1 = stock[u_ma1,'-day'] = stock['Adj Close'].rolling(u_ma1).mean()
	ma2 = stock[u_ma2,'-day'] = stock['Adj Close'].rolling(u_ma2).mean()

	buy_signals = []
	sell_signals = []
	trigger = 0

	for x in range(len(stock)):
		if ma1.iloc[x] > ma2.iloc[x] and trigger != 1:
			buy_signals.append(stock['Adj Close'].iloc[x])
			sell_signals.append(float('nan'))
			trigger = 1
		elif  ma1.iloc[x] < ma2.iloc[x] and trigger != -1:
			buy_signals.append(float('nan'))
			sell_signals.append(stock['Adj Close'].iloc[x])
			trigger = -1
		else:
			buy_signals.append(float('nan'))
			sell_signals.append(float('nan'))

	print(stock)

	stock['Buy Signals'] = buy_signals
	stock['Sell Signals'] = sell_signals

	style = "--";

	label_1 = str(u_ma1) + " Days MA"
	label_2 = str(u_ma2) + " Days MA"


		plt.plot(ma1, label=label_1, color ="#f7c325", linestyle = style, zorder =1)
	plt.plot(ma2, label=label_2, color ="#ed7f1f", linestyle = "--", zorder =1)
	plt.scatter(stock.index, stock['Buy Signals'], label="Buy Signal", marker = "^",color ="#00ff00", lw=3, zorder=3)
	plt.scatter(stock.index, stock['Sell Signals'], label="Sell Signal", marker = "v",color ="#ff0000", lw=3, zorder=3)
"""


