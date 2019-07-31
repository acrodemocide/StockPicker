import requests

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