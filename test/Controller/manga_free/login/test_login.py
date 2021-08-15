import sys, os 
import unittest
sys.path.insert(0, "..\..\..\..")
from src.Connection.connect import connect
from src.Controller.Pages.mangafree.login.login import (check_logged, HOME, login) 
from src.Tools.Error.Pattern.Common import (NotFoundElement)

class TestLogin (unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def setDown(self):
        pass

    def test_check_login(self):

        driver = connect()
        driver.get(HOME)

        test = check_logged(driver)

        self.assertTrue(not test)
    
    def test_login(self):

        driver = connect()
        log = login(driver, "thiagomarques1999@gmail.com", "Script07")
        self.assertTrue(log)

if __name__ == "__main__":
    unittest.main()