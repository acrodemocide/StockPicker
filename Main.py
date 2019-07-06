from Stock import Stock
from TechnicalAnalyzer import ShouldBuyStock, ShouldSellStock, OnBalanceVolumeShouldBuy, OnBalanceVolumeShouldSell

stockMarket = []
appleStock = Stock('Apple', 'AAPL')
microsoftStock = Stock('Microsoft', 'MSFT')
googleStock = Stock('Google', "GOOGL")
stockMarket.append(appleStock)
stockMarket.append(microsoftStock)
stockMarket.append(googleStock)

currentlyHeldStock = []
currentlyHeldStock.append(appleStock)
currentlyHeldStock.append(microsoftStock)
currentlyHeldStock.append(googleStock)

for stock in stockMarket:
    if ShouldBuyStock(stock):
        print('Buy ' + stock.name)
    else:
        print('Do not buy ' + stock.name)

for stock in currentlyHeldStock:
    if ShouldSellStock(stock):
        print('Sell ' + stock.name)
    else:
        print('Hold ' + stock.name)

print('\n\n\nOn Volume Balance Analysis')
for stock in stockMarket:
    if OnBalanceVolumeShouldBuy(stock):
        print('Buy ' + stock.name)
    else:
        print('Do not buy ' + stock.name)

for stock in currentlyHeldStock:
    if OnBalanceVolumeShouldSell(stock):
        print('Sell ' + stock.name)
    else:
        print('Hold ' + stock.name)