from Stock import Stock
from TechnicalAnalyzer import OnBalanceVolumeShouldBuy, OnBalanceVolumeShouldSell
from StockMarket import StockMarket

stockMarket = StockMarket()
appleStock = stockMarket.GetStock('AAPL')
microsoftStock = stockMarket.GetStock('MSFT')
googleStock = stockMarket.GetStock('GOOGL')

currentlyHeldStock = []
currentlyHeldStock.append(appleStock)
currentlyHeldStock.append(microsoftStock)
currentlyHeldStock.append(googleStock)

print('On Volume Balance Analysis')
for stockSymbol in stockMarket.market:
    stock = stockMarket.market[stockSymbol]
    if OnBalanceVolumeShouldBuy(stock):
        print('Buy ' + stock.name)
    else:
        print('Do not buy ' + stock.name)

for stockSymbol in currentlyHeldStock:
    if OnBalanceVolumeShouldSell(stockSymbol):
        print('Sell ' + stockSymbol.name)
    else:
        print('Hold ' + stockSymbol.name)
