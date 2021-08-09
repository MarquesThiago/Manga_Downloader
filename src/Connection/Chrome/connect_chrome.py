import sys, os 
sys.path.insert(0, './../../../src/')
from selenium.webdriver import Chrome
from Connection.generalize import *
from Tools.Error.Connection import * 
from selenium.webdriver import ChromeOptions 
from selenium.common.exceptions import SessionNotCreatedException
from Tools.Router.path import abstract_path as path_abs


def connect():

    return connect_win() 


def connect_win():


    def configured_options():
        options = ChromeOptions()
        options.binary_location = check_chrome()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        return options

    
    path = path_abs(__file__,'../../../Utils/Webdriver/Chrome/Windows/chromedriver.exe')

    verified_driver(path)
    options = configured_options()
    
    driver = configured_driver(Chrome, path,options = options)

    return driver 

def check_chrome():            
    path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    if os.path.isfile(path):
        return path
    elif os.path.isfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
        return r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    else:
        errorNotFoundBrowser() 