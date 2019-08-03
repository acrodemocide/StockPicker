import sys
sys.path.append('../')
from Data.Stock import Stock

# In the future, we will update this so that it can generate an indicator based on how many days
#   we want to look back. This can then be used to determine the OBV as a momentum indicator.
# https://www.investopedia.com/terms/o/onbalancevolume.asp
def OnBalanceVolumeOverTime(stock):
    lookBack = 5
    accumulatedOBV = 0
    numberOfDays = len(stock.dailyClose)
    startingIndex = numberOfDays - lookBack - 1
    if startingIndex < 0:
        startingIndex = 0
    currentIndex = startingIndex
    while currentIndex < numberOfDays:
        previousDayClose = stock.dailyClose[currentIndex - 1]
        currentDayClose = stock.dailyClose[currentIndex]
        currentDayVolume = stock.volume[currentIndex]
        accumulatedOBV = accumulatedOBV + OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume)
        currentIndex = currentIndex + 1
    return accumulatedOBV


def OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume):
    difference = currentDayClose - previousDayClose
    if (difference < 0):
        return currentDayVolume * -1
    elif (difference > 0):
        return currentDayVolume
    else:
        return 0