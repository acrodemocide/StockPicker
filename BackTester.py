from TradingAlgorithms.FirstAlgorithm import FirstAlgorithm
from Portfolio import Portfolio
from Data.Stock import Stock
from Data.StockRepository import StockRepository
from StockBroker import StockBroker

def BackTest():
    appleTickerSymbol = 'AAPL'
    stockRepository = StockRepository()
    startingCash = 1000
    stockBroker = StockBroker(startingCash)
    appleStock = stockRepository.GetStockByTicker(appleTickerSymbol)
    # This will be replaced by using the stockBroker
    # portfolio = Portfolio(startingCash)
    numberOfDays = len(appleStock.dailyClose)
    counter = 0
    portfolioValues = []
    while (counter < numberOfDays):
        previousDayClose = appleStock.dailyClose[counter - 1]
        currentDayClose = appleStock.dailyClose[counter]
        # Tech Debt: Determine a better way to simulate stock market
        stockBroker.UpdateStockValue(currentDayClose)
        portfolioValues.append(stockBroker.GetPortfolio().GetTotalValue())
        if (counter > 0):
            choice = FirstAlgorithm(previousDayClose, currentDayClose)
            if (choice == 'buy'):
                # portfolio.Buy(currentDayClose)
                # Tech Debt: We'll need to be able to get data from the
                #   portfolio to determine how much we can actually buy
                stockBroker.MarketBuy(appleTickerSymbol, 10000)
            else:
                stockBroker.MarketSell(appleTickerSymbol, 10000)
        counter += 1
    return portfolioValues
