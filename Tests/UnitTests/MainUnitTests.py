import unittest 
import sys
sys.path.append('../')
# from TradingAlgorithms.OnBalanceVolume import OnBalanceVolumeOverTime, OnBalanceVolume
# from Data.Stock import Stock

class MainUnitTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_FirstTest(self):
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()