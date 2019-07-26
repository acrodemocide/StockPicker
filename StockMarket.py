from Stock import Stock
from StockDataReader import StockDataReader

class StockMarket:
    def __init__(self):
        self.__market = {}
        self.__market['AAPL'] = Stock('Apple', 'AAPL')
        self.__market['MSFT'] = Stock('Microsoft', 'MSFT')
        self.__market['GOOGL'] = Stock('Google', "GOOGL")
        for stockSymbol in self.__market:
            StockDataReader.GetStockData(self.__market[stockSymbol])
    
    def GetStock(self, symbol):
        return self.__market[symbol]