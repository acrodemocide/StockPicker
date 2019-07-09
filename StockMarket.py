from Stock import Stock

class StockMarket:
    def __init__(self):
        self.market = {}
        self.market['AAPL'] = Stock('Apple', 'AAPL')
        self.market['MSFT'] = Stock('Microsoft', 'MSFT')
        self.market['GOOGL'] = Stock('Google', "GOOGL")
    
    def GetStock(self, symbol):
        return self.market[symbol]