import sys, os 
import unittest
from time import sleep
sys.path.insert(0,'./../../../src/')
from src.Connection.connect import connect
from src.Tools.Router.path import abstract_path
from src.Controller.Pages.mangafree.login.login import login
from src.Controller.Pages.mangafree.mapping.card import state_mapping
from src.Controller.Common import (click_button, find_element, find_element_all)

class TestMapping(unittest.TestCase):

    def setUp(self):
        self.user = input("email: ")
        self.password = input("password: ")
        self.driver = connect()
        
    
    def setDown(self):
        self.driver.quit()

    def test_information_extract(self):

        info =login(self.driver, self.user, self.password)
        print(info)

        click_button(self.driver, ".user-menu")

        data = state_mapping(self.driver, "lido")

        path = abstract_path(__file__, r"..\..\..\..\Database\test.xlsx")

        data.to_excel(path, sheet_name = "lido")

        self.assertTrue(True)
    
if __name__ == "__main__":
    unittest.main()