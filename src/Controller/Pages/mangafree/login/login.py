import sys, os 
from time import (time, sleep)
sys.path.insert(0, "..\..\..\..\..")
from src.Controller.Common import (find_element, click_button)

HOME = "https://mangalivre.net/"

def login(driver,  user, password, type = "mp"):

    driver.get(HOME)
    sleep(10)

    is_logged = check_logged(driver)

    if not is_logged:
        
        click_button(driver, ".login")
        click_button(driver, f".{type}")
        form = find_element(driver, ".login-form")
        email = find_element(form, "input")
        passwrd = find_element(form, "input", index = 1)
        email.send_keys(user)
        passwrd.send_keys(password)

        click_button(form, "button")

        init = time()
        while True:

            if check_logged(driver):
                return True
            elif (time() - init) >= (60 * 6):
                return False 
            else:
                sleep(30)
    return False

def check_logged(driver):

    logged = find_element(driver, ".user-menu")
    login  = find_element(driver, ".login")

    if logged == None and login != None:
        return False
    

    return True

