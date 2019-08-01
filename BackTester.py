from TradingAlgorithms.FirstAlgorithm import FirstAlgorithm
from Portfolio import Portfolio
from Data.Stock import Stock
from Data.StockRepository import BackTestStockRepository
from StockBroker import StockBroker

def BackTest():
    appleTickerSymbol = 'AAPL'
    stockRepository = BackTestStockRepository()
    startingCash = 1000
    stockBroker = StockBroker(startingCash, stockRepository)
    appleStock = stockRepository.GetStockByTicker(appleTickerSymbol)
    numberOfDays = len(appleStock.dailyClose)
    counter = 0
    portfolioValues = []
    while (counter < numberOfDays):
        # Tech Debt - We should only be calling the stock trading algorithm in here
        #   No new information should be derived here -- only passing the stock with
        #   the simulated values created so far
        previousDayClose = 0
        if (counter > 0):
            previousDayClose = appleStock.dailyClose[counter - 1]
        currentDayClose = appleStock.dailyClose[counter]
        portfolioValues.append(stockBroker.GetPortfolio().GetTotalValue())
        if (counter > 0):
            choice = FirstAlgorithm(previousDayClose, currentDayClose)
            if (choice == 'buy'):
                # Tech Debt: We'll need to be able to get data from the
                #   portfolio to determine how much we can actually buy
                stockBroker.MarketBuy(appleTickerSymbol, 10000)
            else:
                # Tech Debt: We'll need to be able to get data from the
                #   portfolio to determine how much we can actually buy
                stockBroker.MarketSell(appleTickerSymbol, 10000)
        counter += 1
    return portfolioValues
