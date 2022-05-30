import sqlite3 as sq


def connect_DB():
    """Connect DataBase"""
    try:
        # con = sqlite3.connect("file:nosuchdb.db?mode=rw", uri=True)
        db = sq.connect("file:../DB/DataBase.db?mode=rw", uri=True, detect_types=sq.PARSE_DECLTYPES)
        print("Connected DataBase successfully")
        return db
    except sq.OperationalError as ex:
        print("Error: The DataBase is not here, Please try again")
    except sq.Error as ex:
        print("Error: while working with SQLite", ex.__class__)



def check(s: str, message: str):
    """check String values and raise ValueError
    if value false return raise Error
    else value true return true
    """
    if len(s) <= 1:
        raise ValueError(message)
    else:
        return True
