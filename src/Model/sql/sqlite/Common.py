import sys, os 
sys.path.insert(0, "..\..\..\..")
import sqlite3 as sql
from src.Model.mapping.mapping import BASE
from src.Tools.Router.path import abstract_path



def connect(name):
    print(BASE)
    con = sql.connect(BASE + "\\{}".format(name))
    return con


def create_table(connect, name_table, fiels = {"test": "varchar(255)"}):
    cursor = connect.cursor()

    columns = ""
    for key, value in fiels.items():
        columns +=f"{key} {value},"

    query = f"CREATE TABLE IF NOT EXISTS {name_table} ( {columns[:-1]} )"     

    cursor.execute(query)
    connect.commit()
    return True

def consult_fast(connect, name_table):
    cursor = connect.cursor()
    query = f"SELECT * FROM {name_table}"
    cursor.execute(query)
    return cursor.fetchall()
    
def describe(connect, name_table):
    cursor = connect.cursor()
    query = f"SELECT sql FROM sqlite_master WHERE name = '{name_table}';"
    cursor.execute(query)
    return cursor.fetchall()
    

# if __name__ == "__main__":
#     con = connect("test.db")
#     create_table(con, "rato", {"esquilo": "integer", "cam": "varcjar(255)"})
#     desc = describe(con, "rato")
#     print(desc)
#     con.close()