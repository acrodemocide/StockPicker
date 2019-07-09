# TODO: Write unit tests for Technical Analyzer (this was taken from an online template)
# Python code to demonstrate working of unittest 
import unittest 
from TechnicalAnalyzer import OnBalanceVolume
from Stock import Stock
  
class TestTechnicalAnalyzerMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
    
    # Returns True if On Balance Volume is calculated correctly
    def test_OnBalanceVolume_IncreasingPrice(self):
        testStock = Stock('Apple', 'AAPL')
        testStock.dailyClose = []
        testStock.dailyClose.append(10)
        testStock.dailyClose.append(20)
        testStock.volume = []
        testStock.volume.append(10000)
        testStock.volume.append(20000)
        OBV = OnBalanceVolume(testStock)
        self.assertEqual(OBV, 20000)
    
    # Returns True if On Balance Volume is calculated correctly
    def test_OnBalanceVolume_DecreasingPrice(self):
        testStock = Stock('Apple', 'AAPL')
        testStock.dailyClose = []
        testStock.dailyClose.append(20)
        testStock.dailyClose.append(10)
        testStock.volume = []
        testStock.volume.append(10000)
        testStock.volume.append(20000)
        OBV = OnBalanceVolume(testStock)
        self.assertEqual(OBV, -20000)
    
    def test_OnBalanceVolume_NoChange(self):
        testStock = Stock('Apple', 'AAPL')
        testStock.dailyClose = []
        testStock.dailyClose.append(10)
        testStock.dailyClose.append(10)
        testStock.volume = []
        testStock.volume.append(10000)
        testStock.volume.append(20000)
        OBV = OnBalanceVolume(testStock)
        self.assertEqual(OBV, 0)
  
if __name__ == '__main__': 
    unittest.main()