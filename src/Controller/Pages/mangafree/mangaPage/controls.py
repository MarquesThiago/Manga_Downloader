import sys, os 
sys.path.insert(0, ".\..\..\..\..\..")
from time import sleep
from src.Controller.Common import (click_button, find_element)
from src.Tools.Message.messages import message_failed


def check_vision(driver, model = "vertical"):

    methods = {
        "vertical": [ ".change-to-vertical", ".change-to-horizontal"], 
        "horizontal": [".change-to-horizontal", ".change-to-vertical"] }
    
    if model not in methods.keys():
        model = "vertical"
    
    print(methods[model][0], r"display: inline;", methods[model][1])

    change = change_vision(driver, methods[model][0], r"display: inline;", methods[model][1])
    verifed_big_age(driver)
    sleep(5)
    return change

def change_vision(driver, on , state, to):

    model = find_element(driver, on)
    now_state = model.get_attribute("style")

    if now_state != state:
        button =click_button(driver, to) 
        sleep(10)
        return button

def verifed_big_age(driver):
    try:
        click_button(driver, ".eighteen-but")
        return True
    except:
        return False

def controller_pages(driver,flag = 0):
        try: 
            check_vision(driver)
            sleep(3)
            navigator =  find_element(driver, ".page-navigation span")
            number = int((find_element(navigator, "em", index = flag)).text)
        except:
            message_failed("Errror on trasformation number page")
            return 0
        return number

def verify_total_pages(driver, total):
    if total == 0:
        driver.refresh()
        sleep(10)
        return (controller_pages(driver, flag= 1))
    return total

def find_image(driver, selector):
    image = find_element(driver, selector)
    url_img = image.get_attribute("src")
    return url_img