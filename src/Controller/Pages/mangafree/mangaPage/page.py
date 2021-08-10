import sys, os 
sys.path.insert(0, ".\..\..\..\..\..")
from time import sleep
from src.Connection.connect import connect
from src.Controller.Common import (find_element)
# from src.Tools.Message.messages import message_failed
from src.Controller.Pages.mangafree.mangaPage.info import sumarize_info
from src.Controller.Pages.mangafree.mangaPage.controls import (verifed_big_age, controller_pages, check_vision)

def walk (driver, page):

    def init(driver, page):
        driver.get(page)
        sleep(2)
        info = sumarize_info(driver)
        check_vision(driver , "horizontal")
        return info
    
    def slide_page(driver): 

        return True
   

    return init(driver, page)
