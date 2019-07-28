from Stock import Stock

# Recognize Technical Patterns
# Determine support and resistance
# Determine stop loss and what the profit should be (order strategy to hit profit target)
# Plan to win 50%-60% of the time -- ensure wins overcome losses
def FirstAlgorithm(previousDayClose, currentDayClose):
    if (currentDayClose < previousDayClose):
        return 'sell'
    elif (currentDayClose >= previousDayClose):
        return 'buy'
