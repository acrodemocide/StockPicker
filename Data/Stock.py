class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.dates = []
        self.dailyHigh = []
        self.dailyLow = []
        self.dailyOpen = []
        self.dailyClose = []
        self.adjustedClose = []
        self.volume = []
        self.onBalanceVolume = []
        
    # Tech Debt -- We need to create a way where we get this information
    #   from the repository rather than just leaving it here
    def CopyToDate(self, date):
        totalNumberOfQuotes = len(self.dates)
        indexOfDesiredDate = 0
        while self.dates[indexOfDesiredDate] < date and indexOfDesiredDate < totalNumberOfQuotes:    
            indexOfDesiredDate += 1

        copyStock = Stock(self.symbol)
        copyStock.dates = self.dates[0:indexOfDesiredDate]
        copyStock.dailyOpen = self.dailyOpen[0:indexOfDesiredDate]
        copyStock.dailyHigh = self.dailyHigh[0:indexOfDesiredDate]
        copyStock.dailyLow = self.dailyLow[0:indexOfDesiredDate]
        copyStock.dailyClose = self.dailyClose[0:indexOfDesiredDate]
        copyStock.adjustedClose = self.adjustedClose[0:indexOfDesiredDate]
        copyStock.volume = self.volume[0:indexOfDesiredDate]
        copyStock.onBalanceVolume = self.onBalanceVolume[0:indexOfDesiredDate]

        return copyStock