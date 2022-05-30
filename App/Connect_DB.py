import sqlite3 as sq


def connect_DB():
    """Connect DataBase"""
    try:
        db = sq.connect("../DB/DataBase.db", detect_types=sq.PARSE_DECLTYPES)
        print("Connected DataBase successfully")
        return db
    except sq.Error as ex:
        # print("Error while working with SQLite", ex)
        return ex


def check(s: str, message: str):
    """check String values and raise ValueError
    if value false return raise Error
    else value true return true
    """
    if len(s) <= 1:
        raise ValueError(message)
    else:
        return True
