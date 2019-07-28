class Portfolio:
    def __init__(self, startingCash):
        self.cash = startingCash
        self.stockValue = 0
        self.numberOfStocksHeld = 0
    
    def GetTotalValue(self):
        totalStockValue = self.stockValue * self.numberOfStocksHeld
        return totalStockValue + self.cash
    
    # This assumes we're putting all of our cash on the stock
    # This also assumes we can buy fractions of a share
    def Buy(self, stockValue):
        if (self.cash > 0):
            totalSharesToBuy = stockValue / self.cash
            self.stockValue = stockValue
            self.numberOfStocksHeld = totalSharesToBuy
            self.cash = 0
    
    # This assumes that we're selling all of our shares held
    def Sell(self, stockValue):
        if (self.numberOfStocksHeld > 0):
            self.cash = self.stockValue * self.numberOfStocksHeld
            self.numberOfStocksHeld = 0
            self.stockValue = 0