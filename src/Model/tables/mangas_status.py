import sys, os 
sys.path.insert(0, "..\..\..")
from src.Model.sql.sqlite.Common import (connect, create_table, describe)


def manga_status():
    conn = connect("db_grod.db")

    field = {
        "title": " TEXT NOT NULL PRIMARY KEY",
        "last_chapther": "FLOAT",
        "cod_read": "INT",
        "read": "VARCHAR(20)",
        "is_favorite": "BOOLEAN",
        "ranking": "VARCHAR(8)",
        "status": "VARCHAR(30)",
        "dt_update": "DATE",
        "dt_update_stamp": "DATETIME"
    }


    create_table(conn, "manga_status", fields = field)
    desc = describe(conn, "manga_status")
    conn.close()
    return desc

# if __name__ == "__main__":
#     print(manga_status())