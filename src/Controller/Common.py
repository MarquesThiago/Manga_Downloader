import  os, sys
sys.path.insert(0, "/src/")
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import JavascriptException
from Tools.Error.alternate_page import (ErrorIncorrectParseKey, ErrorButtonAlternate)
from Tools.Error.Common import ErrorUnknown

def find_element(driver, button, index = 0):
    
    try:
        return driver.find_elements_by_css_selector(button)[index]
    except IndexError:
        ErrorButtonAlternate()
    except Exception:
        ErrorUnknown()
    
def click_button(driver, selector, index = 0):
    try:
        button = find_element(driver, selector, index)
        button.click()
        return True
    except ElementNotInteractableException:
        try:
            driver.execute_script(f'(document.querySelectorAll("{selector}"))[{index}].click()')
            return True
        except: 
            raise ElementNotInteractableException()
    except IndexError:
        ErrorButtonAlternate()
    except Exception:
        ErrorUnknown()