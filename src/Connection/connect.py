import sys,os 
sys.path.insert(0, ".\..\..")
from src.Connection.Chrome import connect_chrome as Chrome 
from src.Connection.Edge import connect_edge as Edge
from src.Tools.Error.Connection import (errorNotFoundBrowser, errorFlagInvalied)
from src.Tools.Message.messages import *


def connect(flag = "--chrome"):

    priority = ["--edge", "--chrome"]

    def model_connect(browser):
        try: 
            return browser.connect()
        except Exception as error:
            message_warning(f"FAiled: {flag[2:]}Tentando com outro navegador")
            priority.remove(flag)
            if priority is not []:
                return set_browser(priority[0])
            else:
                errorNotFoundBrowser()

    def set_browser(flag):
        if flag == "--edge": 
            return   model_connect(Edge)
        elif flag == "--chrome":
            return model_connect(Chrome)
        else:
            errorFlagInvalied()
   
    return set_browser(flag)
        