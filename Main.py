from Stock import Stock
from Data.StockRepository import StockRepository
from BackTester import BackTest

portfolioValues = BackTest()
print(portfolioValues)

print('--------------------------------------')
print('--------------------------------------')
print('--------------------------------------')
print('--------------------------------------')

appleStockTickerSymbol = 'AAPL'
stockRepository = StockRepository()
appleStock = stockRepository.GetStockByTicker(appleStockTickerSymbol)
print(appleStock.dailyClose)