import sys, os 
sys.path.insert(0, ".\..\..\..")
from src.Connection.connect import connect
from src.Controller.Common import (find_element)
from src.Tools.Message.messages import message_failed

def walk (driver, page):

    driver.get(page)

    def informations_manga(driver): 
        title = find_element(driver, ".title").text
        chapter = find_element(driver, ".current-chapter em").text
        total_pages = controller_pages(driver, flag= 1)
        return {"title": title, "chapter": chapter, "total-pages": total_pages}

    def controller_pages(driver,flag = 0):
        navigator =  find_element(driver, ".page-navigation span")
        
        try: 
            number = int((find_element(navigator, "em", index = flag)).text)
        except:
            message_failed("Errror on trasformation number page")
        return number

    return informations_manga(driver)
