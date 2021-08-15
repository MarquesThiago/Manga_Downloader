import os, sys
sys.path.insert(0, './../..')
from src.Tools.Error.Connection import *
from selenium.common.exceptions import SessionNotCreatedException

 
def verified_driver(path):
    if not os.path.isfile(path):
        errorMotFoundDriver()

def configured_driver(browser, path,options = None):
    
    def firts(browser, path, options):
        try: 
            if options is not None:
                driver = browser(path, options = options)
            else:           
                driver = browser(path)
            return driver 
        except SessionNotCreatedException:
            if options is not None: 
                return firts(browser, path)
            else: 
                errorNotFoundBrowser()
        except Exception: 
            errorNotFoundBrowser()

    try:
        return firts(browser, path, options)
    except SessionNotCreatedException as error:
        print(f"\n\n\n\n\n{error.args}")
        errorbrowserNotSupported()
        