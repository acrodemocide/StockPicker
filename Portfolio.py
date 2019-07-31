from Data.StockRepository import StockRepository

class Portfolio:
    def __init__(self, startingCash):
        self.cash = startingCash
        self.stockValue = 0
        self.numberOfStocksHeld = 0
        self.heldStocks = {}    # key = stockTicker, value = number owned
        self.stockRepository = StockRepository()
    
    def GetTotalValue(self):
        accumulatedPortfolioValue = 0
        for stockTickerSymbol, quantity in self.heldStocks.items():
            stockMarketValue = self.stockRepository.GetCurrentStockPrice(stockTickerSymbol)
            totalStockInvestmentValue = stockMarketValue * quantity
            accumulatedPortfolioValue += totalStockInvestmentValue
        accumulatedPortfolioValue += self.cash
        return accumulatedPortfolioValue
    
    def Buy(self, stockTickerSymbol, quantity):
        stockMarketPrice = self.stockRepository.GetCurrentStockPrice(stockTickerSymbol)
        orderTotal = stockMarketPrice * quantity
        if (orderTotal > self.cash):
            maxNumberOfSharesToBuy = self.cash // stockMarketPrice
            orderTotal = stockMarketPrice * maxNumberOfSharesToBuy
        self.cash -= orderTotal
        self.heldStocks[stockTickerSymbol] = quantity

    
    # This assumes that we're selling all of our shares held
    def Sell(self, stockTickerSymbol, quantity):
        if (stockTickerSymbol in self.heldStocks):
            currentMarketValue = self.stockRepository.GetCurrentStockPrice(stockTickerSymbol)
            if (quantity > self.heldStocks[stockTickerSymbol]):
                quantity = self.heldStocks[stockTickerSymbol]
            totalSellValue = currentMarketValue * quantity
            self.cash += totalSellValue
            self.heldStocks[stockTickerSymbol] -= quantity
    
    # Tech Debt: We need to determine a better way to simulate the stock
    #   market
    def UpdateStockValue(self, stockValue):
        self.stockValue = stockValue