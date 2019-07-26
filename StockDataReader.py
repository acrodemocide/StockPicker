import csv
from Stock import Stock

class StockDataReader:
    @staticmethod
    def GetStockData(stockSymbol):
        # # TODO: Pick the correct file based on the stockSymbol
        # f = open('AAPL.csv', 'r')
        # f1 = f.readlines()
        # # Just a note that we are going to populate stock data here
        # stock.dailyClose = stock.dailyClose
        # # End note
        # stockData = []
        # for x in f1:
        #     stockData.append(x)
        # return stockData

        stock = Stock("Apple", "AAPL")
        stock.name = stockSymbol
        stock.symbol = stockSymbol
        with open('AAPL.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    stock.dailyOpen.append(row[1])
                    stock.dailyHigh.append(row[2])
                    stock.dailyLow.append(row[3])
                    stock.dailyClose.append(row[4])
                    stock.volume.append(row[6])
                    line_count += 1

        
        # stock.dailyHigh = [
        #     10716.98,
        #     10736.84,
        #     9963.13,
        #     10996.63,
        #     11052.77,
        #     11451.20,
        #     11841.96,
        #     11905.49,
        #     12144.62,
        #     13129.53
        # ]
        # stock.dailyLow = []
        # stock.dailyOpen = []
        # stock.dailyClose = [
        #     10530.73,
        #     10666.48,
        #     9693.80,
        #     9477.64,
        #     10895.09,
        #     10256.06,
        #     11392.38,
        #     11815.99,
        #     11358.66,
        #     12156.51
        # ]
        # stock.volume = [
        #     20727426310,
        #     25187024648,
        #     24569921549,
        #     24151199070,
        #     25384047207,
        #     22486000001,
        #     21042616384,
        #     23534692797,
        #     28595327690,
        #     33627574244
        # ]
        return stock