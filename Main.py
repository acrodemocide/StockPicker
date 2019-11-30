import sys
sys.path.append('./TradingAlgorithms/')
from Data.Stock import Stock
from Data.StockRepository import StockRepository
from BackTester import BackTest
from OnBalanceVolume import obv

# We should probably move the below function into a separate module that
#   provides utilities that we need.
def CalculateROI(portfolioValues):
    roi = 0.0
    if (len(portfolioValues) > 1):
        startingValue = portfolioValues[0]
        endingValue = portfolioValues[len(portfolioValues) - 1]
        difference = endingValue - startingValue
        roi = difference / startingValue
    return roi

startDate = ''
endDate = ''
portfolioValues = BackTest(obv, startDate, endDate)
print(portfolioValues)

roi = CalculateROI(portfolioValues)
print('Ending ROI: ')
print(roi)

# print('--------------------------------------')
# print('--------------------------------------')
# print('--------------------------------------')
# print('--------------------------------------')

# appleStockTickerSymbol = 'AAPL'
# stockRepository = StockRepository()
# appleStock = stockRepository.GetStockByTicker(appleStockTickerSymbol)
# print(appleStock.dailyClose)