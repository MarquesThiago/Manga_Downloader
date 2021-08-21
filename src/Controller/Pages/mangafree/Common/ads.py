import sys, os
sys.path.insert(0, "../../../../..")
from src.Model.mapping.mapping import (from_to as to, consult)
from src.Controller.Common import (click_button, find_element, find_element_all, find_js)


def remove_message_widget(driver):

    data   = to("card-map")
    selector_message = consult(data, "name", "mapping", "ad_widget-warning")

    try:
        if None is not find_element(driver, selector_message):
            click_button(driver, selector_message)
        else:
            return False
    except:
        return False
    return True