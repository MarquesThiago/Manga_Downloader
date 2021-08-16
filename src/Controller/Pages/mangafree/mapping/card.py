import sys, os
sys.path.insert(0, "../../../../..")
from src.Controller.Pages.mangafree.login.login import check_logged
from src.Controller.Common import (click_button, find_element)
from src.Model.mapping.mapping import (from_to as to, consult)
from src.Tools.Error.login import ErrorNotLogged

def state_mapping(driver, state):

    ITEM_PER_SECTION = 14
    

    if not check_logged:
        ErrorNotLogged()
    
    data = to('card')
    result = consult(data, "state", "selector_common", state )

    click_button(driver,result)
    

    
    

    return True
