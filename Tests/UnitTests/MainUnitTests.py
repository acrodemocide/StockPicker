import unittest 
import sys
sys.path.append('../')
# from TradingAlgorithms.OnBalanceVolume import OnBalanceVolumeOverTime, OnBalanceVolume
# from Data.Stock import Stock

# It seems that there is no clear way to unit test the python main module,
#   so it should be kept logically simple enough that no unit tests are
#   needed to test it. We can write an automated test to test the main
#   method if it is essential that we do so.
class MainUnitTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_FirstTest(self):
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()