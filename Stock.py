import random

# Generate Initial Data -- This will be replaced with actual data
class Stock:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.dailyHigh = []
        self.dailyLow = []
        self.dailyOpen = []
        self.dailyClose = []
        self.volume = []
        # Replace the below function with something that gets the actual data
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