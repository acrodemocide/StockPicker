from Stock import Stock
from TechnicalAnalyzer import ShouldBuy, ShouldSell
from StockMarket import StockMarket

stockMarket = StockMarket()
appleStock = stockMarket.GetStock('AAPL')
microsoftStock = stockMarket.GetStock('MSFT')
googleStock = stockMarket.GetStock('GOOGL')

watchedStocks = []
watchedStocks.append(appleStock)
watchedStocks.append(microsoftStock)
watchedStocks.append(googleStock)

print('On Volume Balance Analysis')
for stock in watchedStocks:
    if ShouldBuy(stock):
        print('Buy ' + stock.name)
    elif ShouldSell(stock):
        print('Sell ' + stock.name)
    else:
        print('Hold ' + stock.name)