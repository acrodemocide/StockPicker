import json
from Stock import Stock
from TechnicalAnalyzer import OnBalanceVolumeApi, OnBalanceVolumeOverTime
from StockMarket import StockMarket

stockMarket = StockMarket()
appleStock = stockMarket.GetStock('AAPL')
# microsoftStock = stockMarket.GetStock('MSFT')
# googleStock = stockMarket.GetStock('GOOGL')

# watchedStocks = []
# watchedStocks.append(appleStock)
# watchedStocks.append(microsoftStock)
# watchedStocks.append(googleStock)

print(appleStock.dailyClose)

accumulatedOnBalanceVolume = OnBalanceVolumeOverTime(appleStock)
print(accumulatedOnBalanceVolume)

# print('On Volume Balance Analysis')
# for stock in watchedStocks:
#     if ShouldBuy(stock):
#         print('Buy ' + stock.name)
#     elif ShouldSell(stock):
#         print('Sell ' + stock.name)
#     else:
#         print('Hold ' + stock.name)
    # with open('data.txt', 'w') as outfile:
    #     json.dump(data, outfile)
# print(OnBalanceVolumeApi(stock))