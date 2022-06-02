import sqlite3 as sq
from datetime import datetime as dt, date as d, time as t


#   from datetime import datetime as dt, date as d
def connect_DB():
    """Connect DataBase"""
    try:
        db = sq.connect("file:../DB/DataBase.db?mode=rw", uri=True, detect_types=sq.PARSE_DECLTYPES)
        print("Connected DataBase successfully")
        return db
    except sq.OperationalError:
        raise "Error: The DataBase is not here, Please try again"
    except sq.Error:
        raise "Error: while working with SQLite"


def check(s: str, message: str):
    """check String values and raise ValueError
    if value false return raise Error
    else value true return true
    """
    if len(s) <= 1:
        raise ValueError(message)
    else:
        return True


# def print_data(str_sql, message, *args):
#     print(message.center(50, '_'))
#     global db
#     try:
#         db = connect_DB()
#         for args, row in zip(args, db.cursor().execute(str_sql).fetchall()):
#
#     except Exception as ex:
#         raise ex
#     finally:
#         if db:
#             db.close()