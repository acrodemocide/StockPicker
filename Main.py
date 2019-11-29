import sys
sys.path.append('./TradingAlgorithms/')
from OnBalanceVolume import obv
from Data.Stock import Stock
from Data.StockRepository import StockRepository
from BackTester import BackTest

startDate = ''
endDate = ''
portfolioValues = BackTest(obv, startDate, endDate)
print(portfolioValues)

# print('--------------------------------------')
# print('--------------------------------------')
# print('--------------------------------------')
# print('--------------------------------------')

# appleStockTickerSymbol = 'AAPL'
# stockRepository = StockRepository()
# appleStock = stockRepository.GetStockByTicker(appleStockTickerSymbol)
# print(appleStock.dailyClose)