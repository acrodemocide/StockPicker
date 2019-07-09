# Recognize Technical Patterns
# Determine support and resistance
# Determine stop loss and what the profit should be (order strategy to hit profit target)
# Plan to win 50%-60% of the time -- ensure wins overcome losses

# In the future, we will update this so that it can generate an indicator based on how many days
#   we want to look back. This can then be used to determine the OBV as a momentum indicator.
# https://www.investopedia.com/terms/o/onbalancevolume.asp
def OnBalanceVolumeOverTime(stock, daysBack):
    accumulatedOBV = 0
    numberOfDays = len(stock.dailyClose)
    startingIndex = numberOfDays - daysBack - 1
    currentIndex = startingIndex
    while currentIndex < numberOfDays:
        if currentIndex > startingIndex:
            previousIndex = currentIndex - 1
            closingPriceChange = stock.dailyClose[currentIndex] - stock.dailyClose[previousIndex]
            onBalanceVolume = 0
            if (closingPriceChange < 0):
                onBalanceVolume = onBalanceVolume - stock.volume[currentIndex]
            elif (closingPriceChange > 0):
                onBalanceVolume = onBalanceVolume + stock.volume[currentIndex]
            accumulatedOBV = accumulatedOBV + onBalanceVolume
        currentIndex = currentIndex + 1


def OnBalanceVolume(stock):
    currentDayIndex = len(stock.dailyClose) - 1
    previousDayIndex = currentDayIndex - 1
    closingPriceChange = stock.dailyClose[currentDayIndex] - stock.dailyClose[previousDayIndex]
    onBalanceVolume = 0 # Initial OBV
    if (closingPriceChange < 0):
        onBalanceVolume = onBalanceVolume - stock.volume[currentDayIndex]
    elif (closingPriceChange > 0):
        onBalanceVolume = onBalanceVolume + stock.volume[currentDayIndex]
    return onBalanceVolume

def OnBalanceVolumeShouldBuy(stock):
    return OnBalanceVolume(stock) > 0

def OnBalanceVolumeShouldSell(stock):
    return OnBalanceVolume(stock) < 0