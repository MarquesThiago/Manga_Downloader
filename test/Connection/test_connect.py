import sys, os 
import unittest
sys.path.insert(0, './../../src/')
from Connection.connect import connect
from Connection.Edge.connect_edge import connect as Edge
from Connection.Chrome.connect_chrome import connect as Chrome

 
class TestConnection(unittest.TestCase):


    def setDown(self):
        pass

    def test_edge(self):
        self.driver = Edge()

        assertion = False
        if self.driver is not None:
            assertion  = True

        self.driver.quit()

        self.assertTrue(assertion)

    def test_chrome(self):
        self.driver = Chrome()

        assertion = False
        if self.driver is not None:
            assertion  = True
        
        self.driver.quit()

        self.assertTrue(assertion)

    def test_geral_connection(self):

        self.driver  = connect()

        assertion = False
        if self.driver is not None:
            assertion  = True
        
        self.driver.quit()

        self.assertTrue(assertion)

    def test_geral_connection_egde(self):
    
        self.driver  = connect("--edge")

        assertion = False
        if self.driver is not None:
            assertion  = True
        
        self.driver.quit()

        self.assertTrue(assertion)
    
    def test_geral_connection_chrome(self):
        
        self.driver  = connect("--chrome")

        assertion = False
        if self.driver is not None:
            assertion  = True
        
        self.driver.quit()

        self.assertTrue(assertion)

    def test_geral_connection_flag(self):
        
        self.driver  = connect("--chme")

        assertion = False
        if self.driver is not None:
            assertion  = True
        
        self.driver.quit()

        self.assertTrue(assertion)


if __name__ == '__main__':
    print("arart")
    unittest.main()