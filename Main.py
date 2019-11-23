import sys
sys.path.append('./TradingAlgorithms/')
from OnBalanceVolume import OnBalanceVolume
from Data.Stock import Stock
from Data.StockRepository import StockRepository
from BackTester import BackTest

portfolioValues = BackTest(OnBalanceVolume)
print(portfolioValues)

print('--------------------------------------')
print('--------------------------------------')
print('--------------------------------------')
print('--------------------------------------')

appleStockTickerSymbol = 'AAPL'
stockRepository = StockRepository()
appleStock = stockRepository.GetStockByTicker(appleStockTickerSymbol)
print(appleStock.dailyClose)