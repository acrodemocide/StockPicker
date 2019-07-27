import requests
from Stock import Stock

# Recognize Technical Patterns
# Determine support and resistance
# Determine stop loss and what the profit should be (order strategy to hit profit target)
# Plan to win 50%-60% of the time -- ensure wins overcome losses

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
        # accumulatedOBV = accumulatedOBV + onBalanceVolume
        previousDayClose = float(stock.dailyClose[currentIndex - 1])
        currentDayClose = float(stock.dailyClose[currentIndex])
        currentDayVolume = int(stock.volume[currentIndex])
        accumulatedOBV = accumulatedOBV + OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume)
        currentIndex = currentIndex + 1
    return accumulatedOBV


def OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume):
    # currentDayIndex = len(stock.dailyClose) - 1
    # previousDayIndex = currentDayIndex - 1
    # closingPriceChange = stock.dailyClose[currentDayIndex] - stock.dailyClose[previousDayIndex]
    # onBalanceVolume = 0 # Initial OBV
    # if (closingPriceChange < 0):
    #     onBalanceVolume = onBalanceVolume - stock.volume[currentDayIndex]
    # elif (closingPriceChange > 0):
    #     onBalanceVolume = onBalanceVolume + stock.volume[currentDayIndex]
    # return onBalanceVolume
    difference = currentDayClose - previousDayClose
    if (difference < 0):
        return currentDayVolume * -1
    elif (difference > 0):
        return currentDayVolume
    else:
        return 0

# def ShouldBuy(stock):
#     return OnBalanceVolume(stock) > 0

# def ShouldSell(stock):
#     return OnBalanceVolume(stock) < 0

# https://www.alphavantage.co/query?function=OBV&symbol=MSFT&interval=weekly&apikey=demo
def OnBalanceVolumeApi(stock):
    # api-endpoint 
    # URL = "http://maps.googleapis.com/maps/api/geocode/json"
    # URL = "https://www.alphavantage.co/query?function=OBV&symbol=MSFT&interval=weekly&apikey=demo"
    URL = "https://www.alphavantage.co/query"
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {
        'function': 'OBV',
        'symbol': stock.symbol,
        'interval': 'weekly', # TODO: Have this passed in from the caller
        'apikey': 'O7LDD7RHT0FVHRZV'
    } 
    response = requests.get(url = URL, params = PARAMS)
    # extracting data in json format 
    data = response.json() 
    return data