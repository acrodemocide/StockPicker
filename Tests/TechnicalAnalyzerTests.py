# TODO: Write unit tests for Technical Analyzer (this was taken from an online template)
# Python code to demonstrate working of unittest 
import unittest 
import sys
sys.path.append('../')
from TradingAlgorithms.OnBalanceVolume import OnBalanceVolumeOverTime, OnBalanceVolume
from Data.Stock import Stock


  
class TestTechnicalAnalyzerMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
    
    # Returns True if On Balance Volume is calculated correctly
    def test_OnBalanceVolume_IncreasingPrice(self):
        previousDayClose = 10
        currentDayClose = 20
        currentDayVolume = 20000
        OBV = OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume)
        self.assertEqual(OBV, 20000)
    
    # Returns True if On Balance Volume is calculated correctly
    def test_OnBalanceVolume_DecreasingPrice(self):
        previousDayClose = 20
        currentDayClose = 10
        currentDayVolume = 20000
        OBV = OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume)
        self.assertEqual(OBV, -20000)
    
    def test_OnBalanceVolume_NoChange(self):
        previousDayClose = 10
        currentDayClose = 10
        currentDayVolume = 20000
        OBV = OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume)
        self.assertEqual(OBV, 0)
    
    def test_OnBalanceVolumeOverTime_OneQuote(self):
        testStock = Stock('AAPL')
        testStock.dailyClose = [10]
        testStock.volume = [10000]
        OBV = OnBalanceVolumeOverTime(testStock)
        self.assertEqual(OBV, 0)
    
    def test_OnBalanceVolumeOverTime_ThreeQuotesIncreasing(self):
        testStock = Stock('AAPL')
        testStock.dailyClose = [10, 20, 30]
        testStock.volume = [10000, 5000, 8000]
        OBV = OnBalanceVolumeOverTime(testStock)
        self.assertEqual(OBV, 13000)
    
    def test_OnBalanceVolumeOverTime_ThreeQuotesDecreasing(self):
        testStock = Stock('AAPL')
        testStock.dailyClose = [30, 20, 10]
        testStock.volume = [10000, 5000, 8000]
        OBV = OnBalanceVolumeOverTime(testStock)
        self.assertEqual(OBV, -13000)
    
    def test_OnBalanceVolumeOverTime_FiveQuotesVarying(self):
        testStock = Stock('AAPL')
        testStock.dailyClose = [25, 18, 32, 12, 96]
        testStock.volume = [10000, 5000, 8000, 12000, 6000]
        OBV = OnBalanceVolumeOverTime(testStock)
        self.assertEqual(OBV, -3000)
  
if __name__ == '__main__': 
    unittest.main()