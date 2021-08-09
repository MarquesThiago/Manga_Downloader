import os, sys
sys.path.insert(0 , "./../../../src/")
from Controller.Common import (find_element, click_button)
from selenium.webdriver.common.keys import Keys
from Tools.Error.Common import ErrorUnknown
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from Tools.Error.alternate_page import (ErrorIncorrectParseKey, ErrorButtonAlternate)


def alternate_page(driver, button = None, index = 0, key = None):

    def check_driver(driver):
        if type(driver) == WebDriver:
            page = driver.find_element(driver, "body")
            return page
        elif type(driver) == WebElement:
            return driver
        else:
            raise TypeError

    def priority(driver, button, index, key):
        if key is not None:
            try:
                page = check_driver(driver)
                page.send_keys(key)
                return True
            except:
                ErrorIncorrectParseKey()
        elif button is not None:
            button = click_button(driver, button, index)
            return True
        else:
            page = check_driver(driver)
            page.send_keys(Keys.RIGHT)
            return True

    return priority(driver, button, index, key)
