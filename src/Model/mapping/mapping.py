import os, sys
sys.path.insert(0, "..\..\..")
from pandas import read_csv as csv
from src.Tools.Router.path import abstract_path

BASE = abstract_path(__file__, r"..\..\..\Database")

def from_to(name):
    base_map = BASE + r"\mapping.csv"
    base_from_to = BASE+ r"\from_to"
    
    try:
        data = csv(base_map)
        name = data[(data["name"] == name) & (data["type"] == "from_to" )]["file"].iloc[0]
        return csv(base_from_to + r"\{}".format(name))
    except:
        raise NameError("Not Mappied value")

def consult(data, from_, to, value):
    result = data[(data[from_] == value)][to].iloc[0]
    return result

# fast test function 
if __name__ == "__main__":
    valeu = input("entry from verify:\n")
    terms = int(input("qtd. terms:\n"))
    print(from_to(value).head(terms))