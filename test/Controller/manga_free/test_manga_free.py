import sys, os 
import unittest
from time import sleep
sys.path.insert(0,'./../../../src/')
from src.Connection.connect import connect
from src.Controller.Pages.mangafree.manga_page import walk

class TestPatternAlternative(unittest.TestCase):

    def setUp(self):
        self.driver = connect()
    
    def setDown(self):
        self.driver.quit()

    def test_information_extract(self):

        info = walk(self.driver, "https://mangalivre.net/ler/hinowa-ga-yuku/online/310236/capitulo-27#/!page0")
        print(info)

        self.assertTrue(type(info)== dict)
    
if __name__ == "__main__":
    unittest.main()