import unittest
from unittest.mock import MagicMock
import sys
sys.path.append('../')
from Portfolio import Portfolio
from Data.StockRepository import BackTestStockRepository

# Pytest requires "test_" prefix to consider a function a test to run
class PortfolioTests(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_GetTotalValue_InitialSetup(self):
        stockRepository = BackTestStockRepository()
        startingCash = 1000
        portfolio = Portfolio(startingCash, stockRepository)
        totalValue = portfolio.GetTotalValue()
        self.assertEqual(totalValue, startingCash)
    
    def test_GetTotalValue_ThreeSharesOfApple(self):
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 200)
        startingCash = 1000
        portfolio = Portfolio(startingCash, mockStockRepository)
        portfolio.heldStocks['AAPL'] = 3
        expectedValue = 1600
        actualValue = portfolio.GetTotalValue()
        self.assertEqual(expectedValue, actualValue)
    
    def test_GetTotalValue_ThreeSharesOfApple_ThreeSharesOfMicrosoft(self):
        # Arrange
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 200)
        startingCash = 1000
        portfolio = Portfolio(startingCash, mockStockRepository)
        portfolio.heldStocks['AAPL'] = 3
        portfolio.heldStocks['MSFT'] = 3
        expectedValue = 2200
        # Act
        actualValue = portfolio.GetTotalValue()
        # Assert
        self.assertEqual(expectedValue, actualValue)
    
    def test_Buy_CashGreaterThanPurchasePrice(self):
        # Arrange
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 200)
        startingCash = 1000
        portfolio = Portfolio(startingCash, mockStockRepository)
        expectedPortfolioValue = 1000
        expectedStockHeldQuantity = 3
        numberOfStocksToPurchase = 3
        # Act
        portfolio.Buy('AAPL', numberOfStocksToPurchase)
        # Assert
        actualValue = portfolio.GetTotalValue()
        self.assertEqual(actualValue, expectedPortfolioValue)
        self.assertEqual(expectedStockHeldQuantity, portfolio.heldStocks['AAPL'])

    def test_Buy_CashEqualToPurchaseprice(self):
        # Arrange
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 200)
        startingCash = 600
        portfolio = Portfolio(startingCash, mockStockRepository)
        expectedPortfolioValue = 600
        expectedStockHeldQuantity = 3
        numberOfStocksToPurchase = 3
        # Act
        portfolio.Buy('AAPL', numberOfStocksToPurchase)
        # Assert
        actualValue = portfolio.GetTotalValue()
        self.assertEqual(actualValue, expectedPortfolioValue)
        self.assertEqual(expectedStockHeldQuantity, portfolio.heldStocks['AAPL'])

    def test_Buy_CashLessThanPurchasePrice(self):
        # Arrange
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 200)
        startingCash = 1000
        portfolio = Portfolio(startingCash, mockStockRepository)
        expectedPortfolioValue = 1000
        expectedStockHeldQuantity = 5
        numberOfStocksToPurchase = 6
        # Act
        portfolio.Buy('AAPL', numberOfStocksToPurchase)
        # Assert
        actualValue = portfolio.GetTotalValue()
        self.assertEqual(actualValue, expectedPortfolioValue)
        self.assertEqual(expectedStockHeldQuantity, portfolio.heldStocks['AAPL'])

    def test_Buy_CashLessThanPurchasePrice_RemainderCashAfterPurchase(self):
        # Arrange
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 300)
        startingCash = 1000
        portfolio = Portfolio(startingCash, mockStockRepository)
        expectedPortfolioValue = 1000
        expectedStockHeldQuantity = 3
        numberOfStocksToPurchase = 6
        # Act
        portfolio.Buy('AAPL', numberOfStocksToPurchase)
        # Assert
        actualValue = portfolio.GetTotalValue()
        self.assertEqual(actualValue, expectedPortfolioValue)
        self.assertEqual(expectedStockHeldQuantity, portfolio.heldStocks['AAPL'])
    
    def test_SellAllStocks(self):
        # Arrange
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 300)
        startingCash = 1000
        portfolio = Portfolio(startingCash, mockStockRepository)
        portfolio.heldStocks['AAPL'] = 10
        numberOfStocksToSell = 10
        expectedStockHeldQuantity = 0
        expectedPortfolioValue = 4000
        # Act
        portfolio.Sell('AAPL', numberOfStocksToSell)
        # Assert
        actualValue = portfolio.GetTotalValue()
        self.assertEqual(expectedPortfolioValue, actualValue)
        self.assertEqual(expectedStockHeldQuantity, portfolio.heldStocks['AAPL'])

    def test_SellAllStocks_SellOrderGreaterThanHeldQuantity(self):
        # Arrange
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 300)
        startingCash = 1000
        portfolio = Portfolio(startingCash, mockStockRepository)
        portfolio.heldStocks['AAPL'] = 10
        numberOfStocksToSell = 11
        expectedStockHeldQuantity = 0
        expectedPortfolioValue = 4000
        # Act
        portfolio.Sell('AAPL', numberOfStocksToSell)
        # Assert
        actualValue = portfolio.GetTotalValue()
        self.assertEqual(expectedPortfolioValue, actualValue)
        self.assertEqual(expectedStockHeldQuantity, portfolio.heldStocks['AAPL'])
    
    def test_SellAllStocks_SellOrderLessThanHeldQuantity(self):
        # Arrange
        mockStockRepository = BackTestStockRepository()
        mockStockRepository.GetCurrentStockPrice = MagicMock(return_value = 300)
        startingCash = 1000
        portfolio = Portfolio(startingCash, mockStockRepository)
        portfolio.heldStocks['AAPL'] = 10
        numberOfStocksToSell = 5
        expectedStockHeldQuantity = 5
        expectedPortfolioValue = 4000
        # Act
        portfolio.Sell('AAPL', numberOfStocksToSell)
        # Assert
        actualValue = portfolio.GetTotalValue()
        self.assertEqual(expectedPortfolioValue, actualValue)
        self.assertEqual(expectedStockHeldQuantity, portfolio.heldStocks['AAPL'])
    
if __name__ == '__main__': 
    unittest.main()