class StockDataReader:
    def GetStockData(self, stockSymbol):
        # TODO: Pick the correct file based on the stockSymbol
        f = open('AAPL.csv', 'r')
        f1 = f.readlines()
        stockData = []
        for x in f1:
            stockData.append(x)
        return stockData