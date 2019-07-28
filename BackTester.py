# from FirstAlgorithm import FirstAlgorithm
from TradingAlgorithms.FirstAlgorithm import FirstAlgorithm
from Portfolio import Portfolio
from Stock import Stock

def BackTest():
    appleStock = Stock('Apple', 'AAPL')
    # Starting money = 1000
    portfolio = Portfolio(1000)
    numberOfDays = len(appleStock.dailyClose)
    counter = 0
    portfolioValues = []
    while (counter < numberOfDays):
        portfolioValues.append(portfolio.GetTotalValue())
        if (counter > 0):
            previousDayClose = appleStock.dailyClose[counter - 1]
            currentDayClose = appleStock.dailyClose[counter]
            choice = FirstAlgorithm(previousDayClose, currentDayClose)
            if (choice == 'buy'):
                portfolio.Buy(currentDayClose)
            else:
                portfolio.Sell(currentDayClose)
        counter += 1
    return portfolioValues
