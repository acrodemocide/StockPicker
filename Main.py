import json
from Stock import Stock
from TechnicalAnalyzer import OnBalanceVolumeApi, OnBalanceVolumeOverTime
from StockMarket import StockMarket

stockMarket = StockMarket()
appleStock = stockMarket.GetStock('AAPL')

# print(appleStock.dailyClose)

# accumulatedOnBalanceVolume = OnBalanceVolumeOverTime(appleStock)
# print(accumulatedOnBalanceVolume)

print(appleStock.onBalanceVolume)