from Stock import Stock
from TechnicalAnalyzer import ShouldBuy, ShouldSell
from StockMarket import StockMarket

stockMarket = StockMarket()
appleStock = stockMarket.GetStock('AAPL')
microsoftStock = stockMarket.GetStock('MSFT')
googleStock = stockMarket.GetStock('GOOGL')

print('On Volume Balance Analysis')
for stockSymbol in stockMarket.market:
    stock = stockMarket.market[stockSymbol]
    if ShouldBuy(stock):
        print('Buy ' + stock.name)
    elif ShouldSell(stock):
        print('Sell ' + stock.name)
    else:
        print('Hold ' + stock.name)