import csv
import random

# Generate Initial Data -- This will be replaced with actual data
class Stock:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.dailyHigh = []
        self.dailyLow = []
        self.dailyOpen = []
        self.dailyClose = []
        self.volume = []
        
        with open('AAPL.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    self.dailyOpen.append(row[1])
                    self.dailyHigh.append(row[2])
                    self.dailyLow.append(row[3])
                    self.dailyClose.append(row[4])
                    self.volume.append(row[6])
                    line_count += 1

    # def GenerateDummyData(self):
    #     lowPossibility = 0
    #     highPossibility = 100
    #     numberOfValues = 100
    #     self.dailyHigh = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
    #     self.dailyLow = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
    #     self.dailyOpen = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
    #     self.dailyClose = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
    #     self.volume = self.GenerateRandomValues(lowPossibility, highPossibility, numberOfValues)
    
    # def GenerateRandomValues(self, lowPossibility, highPossibility, numberOfValues):
    #     randomGeneratedValues = []
    #     for x in range(numberOfValues):
    #         randomGeneratedValues.append(random.randint(lowPossibility, highPossibility))
    #     return randomGeneratedValues