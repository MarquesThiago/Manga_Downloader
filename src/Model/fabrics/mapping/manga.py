
import os, sys
sys.path.insert(0, "..\..\..\..")
from datetime import datetime as dt
from src.Model.mapping.mapping import from_to as to

def manga(
    name, last_cap = 1, read = None, cod = None, favorite = False, rank = None, status = "in_process"):

    date = dt.now()

    def status_read(cod = None , read = None):

        cod_read = to("cod_read")

        def obj(id, status):
            return {"cod": id, "state": status}

        def default():
            coding = 0
            reading = cod_read[(cod_read["cod"] == coding)]["state"].iloc[0]
            return obj(coding, reading)
        
        if cod  not in  (None, False):
            
            try: 
                reading = cod_read[(cod_read["cod"] == cod)]["state"].iloc[0]
                return obj(cod, reading)
            except:
                if read not in (None, False):
                   return status_read(read = read) 
                else:
                   return default()
        
        elif read not in (None, False):
            
            try: 
                coding = cod_read[(cod_read["state"] == read)]["cod"].iloc[0]
                return obj(coding, read)
            except:
                return default()

    def is_complete(value):
        try:
            if value.lower() == "completo":
                return "complet"
        except:
            pass
        
        return "in process"
        
    read = status_read(cod, read)

    manga = {
        "title": name,
        "last_chapther": last_cap,
        "cod_read": read["cod"],
        "read": read["state"],
        "is_favorite": favorite,
        "ranking": rank,
        "status": is_complete(status),
        "dt_update": f"{date.year}-{date.month}-{date.day}",
        "dt_update_stamp": f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}"
    }


    
    return manga
    

    
# fast test with any params
# if __name__ == "__main__":

#     print(manga("test", 12, read = "lerei", rank = 1.25, status = "Completo") )
#     print(manga("test", 12, read = "lido", cod = 3,rank = 1.25, favorite = True) )
     