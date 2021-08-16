import os, sys
import requests
sys.path.insert(0, "./../..")
from src.Tools.Message.messages import (message_information, message_sucess, message_failed, message_warning)


def download_images(url, name, page, name_destiny):

    counter = 0

    def save(url, name, page, name_destiny = None):
        if name_destiny == None:
            name_destiny = name

        response = requests.get(url = url)
        destiny  = created_path(name_destiny)
        path = destiny + f"\\{name}_0{page}.jpg"
        
        if response.status_code is requests.codes.OK:
            with open(path,"wb") as image:
                image.write(response.content)
            zero_counter()
        else:
            message_warning("Error in writer image")
            if counter < 3:
                counter += 1
                download_images(url, name, page, name_destiny)
            elif counter >= 3:
                message_failed("Sorry, Really no Found")
                zero_counter()
                return False
        return True    

    def _created_path( name):
        destiny = path_abs(__file__,'../../Media/images/{name}')
        if not os.path.exists(destiny):
            os.makedirs(destiny)
        return destiny

    def _zero_counter():
        counter = 0
    
    return save(url, name, page, name_destiny)