import random

# Generate Initial Data -- This will be replaced with actual data
class Stock:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.GenerateDummyData()

    def GenerateDummyData(self):
        lowPossibility = 0
        highPossibility = 100
        numberOfValues = 100
        self.dailyHigh = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
        self.dailyLow = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
        self.dailyOpen = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
        self.dailyClose = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
        self.volume = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
    
    def GenerateRandomValues(self, lowPossibility, highPossibility, numberOfValues):
        randomGeneratedValues = []
        for x in range(numberOfValues):
            randomGeneratedValues.append(random.randint(lowPossibility, highPossibility))
        return randomGeneratedValues


def ShouldBuyStock(stock):
    return stock.volume[0] > 50 and stock.dailyOpen[0] < stock.dailyClose[0]

def ShouldSellStock(stock):
    return stock.volume[0] > 50 and stock.dailyOpen[0] > stock.dailyClose[0]

# In the future, we will update this so that it can generate an indicator based on how many days
#   we want to look back. This can then be used to determine the OBV as a momentum indicator.
# https://www.investopedia.com/terms/o/onbalancevolume.asp
def OnBalanceVolume(stock):
    currentDayIndex = len(stock.dailyClose) - 1
    previousDayIndex = currentDayIndex - 1
    closingPriceChange = stock.dailyClose[currentDayIndex] - stock.dailyClose[previousDayIndex]
    onBalanceVolume = 0 # Initial OBV
    if (closingPriceChange < 0):
        onBalanceVolume = onBalanceVolume - stock.volume[currentDayIndex]
    else if (closingPriceChange > 0):
        onBalanceVolume = onBalanceVolume + stock.volume[currentDayIndex]
    return onBalanceVolume


# Recognize Technical Patterns
# Determine support and resistance
# Determine stop loss and what the profit should be (order strategy to hit profit target)
# Plan to win 50%-60% of the time -- ensure wins overcome losses

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