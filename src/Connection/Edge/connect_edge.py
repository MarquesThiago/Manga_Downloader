import sys, os 
sys.path.insert(0, './../../..')
from selenium.webdriver import Edge
from src.Connection.generalize import *
from src.Tools.Error.Connection import * 
from msedge.selenium_tools import EdgeOptions
from src.Tools.Router.path import abstract_path as path_abs


def connect():
    path = path_abs(__file__,'../../../Utils/Webdriver/Edge/msedgedriver.exe')

    verified_driver(path)
    
    driver = Edge(path,verbose = False)

    return driver 