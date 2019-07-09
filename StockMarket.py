from Stock import Stock

class StockMarket:
    def __init__(self):
        self.__market = {}
        self.__market['AAPL'] = Stock('Apple', 'AAPL')
        self.__market['MSFT'] = Stock('Microsoft', 'MSFT')
        self.__market['GOOGL'] = Stock('Google', "GOOGL")
    
    def GetStock(self, symbol):
        return self.__market[symbol]