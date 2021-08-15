import sys, os
sys.path.insert(0, "../../../../..")
from src.Controller.Pages.mangafree.login.login import check_logged
from src.Tools.Error.login import ErrorNotLogged

def state_mapping(driver, state):

    if not check_logged:
        ErrorNotLogged()
    
    

    return True
