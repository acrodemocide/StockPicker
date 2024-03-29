from Portfolio import Portfolio
from Data.StockRepository import StockRepository, BackTestStockRepository

class StockBroker:
    def __init__(self, initialCashDeposit, stockRepository):
        self.__portfolio = Portfolio(initialCashDeposit, stockRepository)
        self.stockRepository = stockRepository
    
    def MarketBuy(self, stockTickerSymbol, quantity):
        self.__portfolio.Buy(stockTickerSymbol, quantity)
    
    def MarketSell(self, stockTickerSymbol, quantity):
        self.__portfolio.Sell(stockTickerSymbol, quantity)
    
    # Set order to buy a stock if it hits a certain price.
    def LimitBuy(self, stockTickerSymbol, quantity, buyLimit):
        return 'Not yet implemented'
    
    # Set order to sell a stock if it hits a certain price.
    def LimitSell(self, stockTickerSymbol, quantity, sellLimit):
        return 'Not yet implemented'
    
    # Set order to buy a stock at market price, then sell if it hits the
    #   sellPrice
    def StopLoss(self, stockTickerSymbol, quantity, sellPrice):
        return 'Not yet implemented'
    
    def GetPortfolio(self):
        return self.__portfolio