import unittest
import sys
sys.path.append('../')
from Portfolio import Portfolio
from Data.StockRepository import BackTestStockRepository

# Pytest requires "test_" prefix to consider a function a test to run
class PortfolioTests(unittest.TestCase):
      
    def setUp(self): 
        pass
    
    def test_FirstTest(self):
        self.assertEqual(1, 1)
    
    def test_GetTotalValue_InitialSetup(self):
        stockRepository = BackTestStockRepository()
        startingCash = 1000
        portfolio = Portfolio(startingCash, stockRepository)
        totalValue = portfolio.GetTotalValue()
        self.assertEqual(totalValue, startingCash)
    
    # TODO: Create a mock repository to allow us to use predictable test data
    # def test_Buy(self):
    #     stockRepository = BackTestStockRepository()
    #     startingCash = 1000
    #     portfolio = Portfolio(startingCash, stockRepository)
    #     tickerSymbol = 'AAPL'
    #     portfolio.Buy(tickerSymbol, 3)
    #     self.assertEqual(1, 1)

    # This is my recording test asdfkasjldfkj aisndfkn
    # I like writing code, but this is all really comments
    
if __name__ == '__main__': 
    unittest.main()