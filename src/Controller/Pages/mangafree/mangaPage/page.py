import sys, os 
sys.path.insert(0, ".\..\..\..\..\..")
from time import sleep
from src.Connection.connect import connect
from src.Controller.Common import (find_element)
# from src.Tools.Message.messages import message_failed
from src.Controller.Pages.mangafree.mangaPage.info import sumarize_info
from src.Controller.Pages.mangafree.mangaPage.walk import walk
from src.Controller.Pages.mangafree.mangaPage.controls import (verifed_big_age, controller_pages, check_vision)

def walk (driver, page):

    def init(driver, page):
        driver.get(page)
        sleep(2)
        info = sumarize_info(driver)
        return info

    info = init(driver, page)
    init_page =  controller_pages(driver)


    is_walk = walk(driver, init_page, info["total-pages"], info["name-file"], info["name_folder"]) 
   

    return is_walk