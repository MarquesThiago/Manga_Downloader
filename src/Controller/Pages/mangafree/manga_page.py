import sys, os 
sys.path.insert(0, ".\..\..\..")
from time import sleep
from src.Connection.connect import connect
from src.Controller.Common import (find_element, click_button)
from src.Tools.Text.treatment import (simple_name, complete_name)
from src.Tools.Message.messages import message_failed

def walk (driver, page):

    def init(driver, page):
        driver.get(page)
        sleep(5)
        verifed_big_age(driver)
        info = sumarize_info(driver)
        return info
    
    def verifed_big_age(driver):
        try:
            click_button(driver, ".eighteen-but")
            return True
        except:
            return False

    def sumarize_info(driver):
        info = informations_manga(driver)
        treated_name = treat_name_file_on_f0lder(info["title"], info["chapter"])
        return {
            "title": info["title"],"chapter": info["chapter"], "total-pages": info["total-pages"], 
            "name-file": treated_name["name-file"], "name-folder": treated_name["name-folder"]
            }

    def informations_manga(driver): 
        title = find_element(driver, ".title").text
        chapter = find_element(driver, ".current-chapter em").text
        total_pages = controller_pages(driver, flag= 1)
        return {"title": title, "chapter": chapter, "total-pages": total_pages}

    def controller_pages(driver,flag = 0):
        try: 
            navigator =  find_element(driver, ".page-navigation span")
            number = int((find_element(navigator, "em", index = flag)).text) 
        except:
            message_failed("Errror on trasformation number page")
        return number

    def treat_name_file_on_f0lder(title, chapter):
        name_file = simple_name(title, chapter)
        folder_name = complete_name(title, chapter)
        return {"name-file": name_file, "name-folder": folder_name}
   

    return init(driver, page)
