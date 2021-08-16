import sys, os 
sys.path.insert(0, "..\..\..\..")
import pandas as pd
import sqlite3 as sql
from src.Model.mapping.mapping import BASE
from src.Tools.Router.path import abstract_path



def connect(name):
    print(BASE)
    con = sql.connect(BASE + "\\{}".format(name))
    return con


def create_table(connect, name_table, fields = {"test": "varchar(255)"}):
    cursor = connect.cursor()

    columns = ""
    for key, value in fields.items():
        columns +=f"{key} {value},"

    query = f"CREATE TABLE IF NOT EXISTS {name_table} ( {columns[:-1]} )"     

    cursor.execute(query)
    connect.commit()
    return True

def insert_values(connect, name_table, fiels):
    cursor = connect.cursor()

    columns = ""
    data = ""
    for key, value in fields.items():
        columns +=f"{key},"
        data += f"{value},"

    query = f"INSERT INTO {name_table} ( {columns[:-1]} ) VALUES ( {data[:-1]} )"     

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

def save_sql(connect, name, data):
    data.to_sql(name, con = connect, if_exists='append')
    return True    

# if __name__ == "__main__":
#     con = connect("test.db")
#     create_table(con, "rato", {"esquilo": "integer", "cam": "varcjar(255)"})
#     desc = describe(con, "rato")
#     print(desc)
#     con.close()