import sys, os
sys.path.insert(0, "..\..")
import pandas as pd

def trasnform_data(list_data):
    
    container_data = []

    try:
        for index in list_data:
            pack = pd.DataFrame(data = index)
            container_data.append(pack)
    except ValueError:
        new_data_list = prepared_data(list_data)
        return trasnform_data(new_data_list)
    
    data = pd.concat(container_data)
    return data 

def prepared_data(data_list, exception_keys = []):
    
    new_data_list = []

    for row in data_list:
        new_row = {}
        for key, value in row.items():
            if key not in (exception_keys):
                new_row[key] = [value]
            else:
                new_row[key] = value
        new_data_list.append(new_row)
    return new_data_list