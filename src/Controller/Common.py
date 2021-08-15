import  os, sys
sys.path.insert(0, "..\..")
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import JavascriptException
from src.Tools.Error.Common import (ErrorUnknown, NotFoundElement)

def find_element(driver, button, index = 0):
    
    try:
        return driver.find_elements_by_css_selector(button)[index]
    except IndexError:
        NotFoundElement()
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
        NotFoundElement()
    except Exception:
        ErrorUnknown()