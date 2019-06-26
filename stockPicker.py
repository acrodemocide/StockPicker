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