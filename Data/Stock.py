class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.dates = []
        self.dailyHigh = []
        self.dailyLow = []
        self.dailyOpen = []
        self.dailyClose = []
        self.adjustedClose = []
        self.volume = []
        self.onBalanceVolume = []