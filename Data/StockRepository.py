from Data.Stock import Stock
import csv
from datetime import datetime

class StockRepository:
    def __init__(self):
        self.stockLookupTable = {
            'AAPL': './Data/AAPL.csv',
            'GOOG': './Data/GOOG.csv',
            'MSFT': './Data/MSFT.csv'
        }
        self.cachedStock = {}

    def GetStockByTicker(self, stockTickerSymbol):
        stock = None
        if (stockTickerSymbol not in self.cachedStock):
            stockDataFile = self.stockLookupTable[stockTickerSymbol]
            stock = self.__ReadStockFromCSV(stockDataFile)
            self.cachedStock[stockTickerSymbol] = stock
        else:
            stock = self.cachedStock[stockTickerSymbol]
        return stock
    
    def GetCurrentStockPrice(self, stockTickerSymbol):
        stock = self.GetStockByTicker(stockTickerSymbol)
        # Stocks are loaded in chronological order with the most recent being
        #   loaded last
        mostRecentIndex = len(stock.dates) - 1
        # With our limited data, for now, we're just going to use the closingPrice
        #   for the most current day
        stockPrice = stock.dailyClose[mostRecentIndex]
        return stockPrice
    
    def __ReadStockFromCSV(self, fileName):
        stock = Stock('')
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    currentDate = datetime.strptime(row[0], '%Y-%m-%d')
                    currentOpen = float(row[1])
                    currentHigh = float(row[2])
                    currentLow = float(row[3])
                    currentClose = float(row[4])
                    currentAdjustedClose = float(row[5])
                    currentVolume = int(row[6])

                    stock.dates.append(currentDate)
                    stock.dailyOpen.append(currentOpen)
                    stock.dailyHigh.append(currentHigh)
                    stock.dailyLow.append(currentLow)
                    stock.dailyClose.append(currentClose)
                    stock.adjustedClose.append(currentAdjustedClose)
                    stock.volume.append(currentVolume)
                if (line_count == 1):
                    stock.onBalanceVolume.append(0)
                elif(line_count > 1):
                    previousDayIndex = line_count - 2
                    currentDayIndex = line_count - 1
                    previousDayClosingPrice = float(stock.dailyClose[previousDayIndex])
                    currentDayClosingPrice = float(stock.dailyClose[currentDayIndex])
                    previousDayVolume = int(stock.volume[previousDayIndex])
                    currentDayVolume = int(stock.volume[currentDayIndex])

                    closingPriceChange = currentDayClosingPrice - previousDayClosingPrice
                    onBalanceVolumeFactor = -1 if closingPriceChange < 0 else 1 if closingPriceChange > 0 else 0
                    volumeToAdd = currentDayVolume * onBalanceVolumeFactor

                    stock.onBalanceVolume.append(previousDayVolume + volumeToAdd)
                line_count += 1
        return stock
