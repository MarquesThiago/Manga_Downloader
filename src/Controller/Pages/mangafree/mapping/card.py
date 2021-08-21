import sys, os
import re
sys.path.insert(0, "../../../../..")
from time import sleep
from src.Model.simple import trasnform_data
from selenium.webdriver.common.keys import Keys
from src.Controller.Pages.mangafree.Common.ads import remove_message_widget
from src.Controller.Pages.mangafree.login.login import check_logged
from src.Controller.Common import (click_button, find_element, find_element_all, find_js)
from src.Model.mapping.mapping import (from_to as to, consult)
from src.Model.fabrics.mapping.manga import manga
from src.Tools.Error.login import ErrorNotLogged

data_variables = to("card-map")
data = to('card')
url = None

def state_mapping(driver, state):
    
    url = driver.current_url

    pattern = re.compile(r"\d+")

    def remove_hashe(value): 
        divided = r"{}".format(value).split("\\")
        new_state = " ".join(divided)
        return new_state
    
    state_selector = consult(data, "state", "selector_common", state)

    container_selector = consult(data_variables, "name", "mapping", "container")
    items_selector = consult(data_variables, "name", "mapping", "items")

    print("\n\n\n\n clickando no state\n\n\n\n")

    print(state_selector)

    sleep(15)
    remove_message_widget(driver)
    total_element = driver.execute_script(f' return (document.querySelector("{state_selector}"))') 
    total_txt = total_element.text

    remove_message_widget(driver)
    while None == find_js(driver, f"{state_selector}.active"):
        try: 
            total_element.click()
        except:
            click_button(driver,state_selector)
        sleep(6)
   
    print(total_txt)
    # total_txt = (find_element(driver, state_selector).text)
    
    total = int(pattern.findall(total_txt.strip())[0])
    

    if state == "lerei" and total < 58:
        total = 58

    print("\n\n\n\ntentado o scrool\n\n\n\n")

    # if url.__eq__(driver.current_url):
    #     print(f"\n\n\n\n\n\n\n{url},\n {driver.current_url}")
    #     sleep(10)
    #     driver.back()
    #     raise ValueError("Page redicted")

    scrooling(driver, container_selector, total)
    rest = check_submited(driver, items_selector, total)

    if rest > 0:
        scrooling(driver, container_selector, total)

    mapping = map_info(driver, items_selector)
    data_map = trasnform_data(mapping)

    return data_map

def scrooling(driver, container, total, submited = 14):

    url =  driver.current_url
        
    ITEM_PER_SECTION = submited

    remove_message_widget(driver)

    # if url.__eq__(driver.current_url):
       
    #     driver.back()
    #     raise ValueError("Page directed")
    
    if total > ITEM_PER_SECTION:
        qtd_scrool = 1 + int(total / ITEM_PER_SECTION)
    else:
        qtd_scrool = 1 + 1 

    click_button(driver, "#mp-menu")
    body = find_element(driver, "body")

    for i in range(qtd_scrool):
        body.send_keys(Keys.END)
        sleep(30)
        body.send_keys(Keys.END)
        sleep(20)

    return True

def check_submited(driver, selector, total):

    qtd_items_listed = len(find_element_all(driver, selector))
    
    rest = total - qtd_items_listed
    return rest

def map_info(driver, selector): 

    pattern = re.compile(r"\d+")

    state_selector = consult(data_variables, "name", "mapping", "status")
    title_selector = consult(data_variables, "name", "mapping", "title")
    chapter_selector  = consult(data_variables, "name", "mapping", "chapter")
    is_favorite_selector = consult(data_variables, "name", "mapping", "favorited")
    image_selector =  consult(data_variables, "name", "mapping", "image")

    total  = len(find_element_all(driver, selector))
    state  = find_element(driver, state_selector)
    manga_listed = []

    for index in range(total):

        item = find_element(driver, selector, index = index)

        title =  find_element(item, title_selector).text
        chapter_text =  find_element(item, chapter_selector).text
        chapter = pattern.findall(chapter_text)[0]
        favorited = find_element(item, is_favorite_selector)
        image_url = find_element(item, image_selector).value_of_css_property("background-image")
        image = image_url[4:-1]

        manga_ = manga( title, last_cap = chapter, read = state, favorite = favorited, image = image)
        manga_listed.append(manga_)
    
    return manga_listed

