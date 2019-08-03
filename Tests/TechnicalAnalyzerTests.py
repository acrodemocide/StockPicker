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
        previousDayClose =10
        currentDayClose = 20
        currentDayVolume = 20000
        OBV = OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume)
        self.assertEqual(OBV, 20000)
    
    # Returns True if On Balance Volume is calculated correctly
    def test_OnBalanceVolume_DecreasingPrice(self):
        previousDayClose =20
        currentDayClose = 10
        currentDayVolume = 20000
        OBV = OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume)
        self.assertEqual(OBV, -20000)
    
    def test_OnBalanceVolume_NoChange(self):
        previousDayClose =10
        currentDayClose = 10
        currentDayVolume = 20000
        OBV = OnBalanceVolume(previousDayClose, currentDayClose, currentDayVolume)
        self.assertEqual(OBV, 0)
  
if __name__ == '__main__': 
    unittest.main()