from Stock import Stock
from BackTester import BackTest

portfolioValues = BackTest()
print(portfolioValues)

print('--------------------------------------')
print('--------------------------------------')
print('--------------------------------------')
print('--------------------------------------')

appleStock = Stock('Apple', 'AAPL')
print(appleStock.dailyClose)