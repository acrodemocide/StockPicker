import csv
import random

# Generate Initial Data -- This will be replaced with actual data
class Stock:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.dates = []
        self.dailyHigh = []
        self.dailyLow = []
        self.dailyOpen = []
        self.dailyClose = []
        self.adjustedClose = []
        self.volume = []
        self.onBalanceVolume = []
        
        with open('AAPL.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                currentDate = row[0]
                currentOpen = row[1]
                currentHigh = row[2]
                currentLow = row[3]
                currentClose = row[4]
                currentAdjustedClose = row[5]
                currentVolume = row[6]
                if line_count > 0:
                    self.dates.append(currentDate)
                    self.dailyOpen.append(currentOpen)
                    self.dailyHigh.append(currentHigh)
                    self.dailyLow.append(currentLow)
                    self.dailyClose.append(currentClose)
                    self.adjustedClose.append(currentAdjustedClose)
                    self.volume.append(currentVolume)
                if (line_count == 1):
                    self.onBalanceVolume.append(0)
                elif(line_count > 1):
                    previousDayIndex = line_count - 2
                    currentDayIndex = line_count - 1
                    previousDayClosingPrice = float(self.dailyClose[previousDayIndex])
                    currentDayClosingPrice = float(self.dailyClose[currentDayIndex])
                    previousDayVolume = int(self.volume[previousDayIndex])
                    currentDayVolume = int(self.volume[currentDayIndex])

                    closingPriceChange = currentDayClosingPrice - previousDayClosingPrice
                    onBalanceVolumeFactor = -1 if closingPriceChange < 0 else 1 if closingPriceChange > 0 else 0
                    volumeToAdd = currentDayVolume * onBalanceVolumeFactor

                    self.onBalanceVolume.append(previousDayVolume + volumeToAdd)
                line_count += 1