import sys, os 
sys.path.insert(0, './../../../src/')
from selenium.webdriver import Edge
from Connection.generalize import *
from Tools.Error.Connection import * 
from msedge.selenium_tools import EdgeOptions
from Tools.Router.path import abstract_path as path_abs


def connect():
    path = path_abs(__file__,'../../../Utils/Webdriver/Edge/msedgedriver.exe')

    verified_driver(path)
    
    driver = Edge(path,verbose = False)

    return driver 