from TradingAlgorithms.FirstAlgorithm import FirstAlgorithm
from Portfolio import Portfolio
from Data.Stock import Stock
from Data.StockRepository import BackTestStockRepository
from StockBroker import StockBroker

def BackTest(tradingAlgorithm, startDate, endDate):
    # Trading algorithm should take
    # 1- a reference to our stock universe (so that it can choose any available stock)
    #   2 - The dates we get will be used to get the slice of information between
    #       the specified time periods
    # 
    # We want to set up the back tester so that it just feeds data to the algorithm
    #   We don't want to create an algorithm for back testing then adjust it for paper/real
    #   trading. The backtester should facility feeding the data to the algorithm, simulating
    #   information like it's coming in real time. The algorithm will then take the available
    #   information, make the decisions it's programmed to make until it is fed the next data
    #   point (next stock price)
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
