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
  
    # Returns True if the string contains 4 a. 
    def test_strings_a(self): 
        self.assertEqual( 'a'*4, 'aaaa') 
  
    # Returns True if the string is in upper case. 
    def test_upper(self):         
        self.assertEqual('foo'.upper(), 'FOO') 
  
    # Returns TRUE if the string is in uppercase 
    # else returns False. 
    def test_isupper(self):         
        self.assertTrue('FOO'.isupper()) 
        self.assertFalse('Foo'.isupper()) 
  
    # Returns true if the string is stripped and  
    # matches the given output. 
    def test_strip(self):         
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks') 
  
    # Returns true if the string splits and matches 
    # the given output. 
    def test_split(self):         
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world']) 
        with self.assertRaises(TypeError): 
            s.split(2) 
  
if __name__ == '__main__': 
    unittest.main()