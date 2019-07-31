from TradingAlgorithms.FirstAlgorithm import FirstAlgorithm
from Portfolio import Portfolio
from Data.Stock import Stock
from Data.StockRepository import StockRepository

def BackTest():
    stockRepository = StockRepository()
    appleStock = stockRepository.GetStockByTicker('AAPL')
    startingCash = 1000
    portfolio = Portfolio(startingCash)
    numberOfDays = len(appleStock.dailyClose)
    counter = 0
    portfolioValues = []
    while (counter < numberOfDays):
        previousDayClose = appleStock.dailyClose[counter - 1]
        currentDayClose = appleStock.dailyClose[counter]
        portfolio.UpdateStockValue(currentDayClose)
        portfolioValues.append(portfolio.GetTotalValue())
        if (counter > 0):
            choice = FirstAlgorithm(previousDayClose, currentDayClose)
            if (choice == 'buy'):
                portfolio.Buy(currentDayClose)
            else:
                portfolio.Sell(currentDayClose)
        counter += 1
    return portfolioValues
