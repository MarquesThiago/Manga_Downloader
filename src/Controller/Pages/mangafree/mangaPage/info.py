import sys, os 
sys.path.insert(0, ".\..\..\..\..\..")
from time import sleep
from src.Controller.Common import (find_element, click_button)
from src.Tools.Text.treatment import (simple_name, complete_name)
from src.Controller.Pages.mangafree.mangaPage.controls import (controller_pages, verify_total_pages, check_vision)


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
    total_pages = verify_total_pages(driver, controller_pages(driver, flag= 1))
    return {"title": title, "chapter": chapter, "total-pages": total_pages}

def treat_name_file_on_f0lder(title, chapter):
    name_file = simple_name(title, chapter)
    folder_name = complete_name(title, chapter)
    return {"name-file": name_file, "name-folder": folder_name}
