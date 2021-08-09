import sys, os 
import unittest
from time import sleep
sys.path.insert(0, './../../../src/')
from Connection.connect import connect
from selenium.webdriver.common.keys import Keys
from Controller.Common import find_element
from Controller.pattern.horizontal import alternate_page as alter


class TestPatternAlternative(unittest.TestCase):


    def setUp (self):
        self.driver = connect()

    def SetDown (self):
        print("\n\n\nfechando")
        self.driver.quit()

    def test_alternat_page(self):
        url = "https://mangalivre.net/ler/mercenary-enrollment/online/318548/capitulo-43#/!page0"
        self.driver.get(url)
        sleep(5)
        print("\n\n\n")
        print(type(self.driver))
        page = find_element(self.driver, "body")
        print("\n\n\n")
        print(type(page))
        test = (alter(page, ".page-next", key = Keys.RIGHT)) 
        
        self.assertTrue(test)

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()