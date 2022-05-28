import sqlite3 as sq
from datetime import datetime
import time
import numpy as np
# db = sq.connect("../DB/DataBase.db")
# print("connected dataBase")
#
# cu = db.cursor()
# d = date(2002, 12, 31)
# cu.execute(f"INSERT INTO Person(Id, first_name, father, last_name, gender, birth_year, address) VALUES(1, 'm7mmad', 'omar', 'haj hamdo', 'male', {d}, 'Azaz'")
#
# db.commit()
#
# db.close()
# print("closed DataBase")

try:
    db = sq.connect("../DB/DataBase.db", detect_types=sq.PARSE_DECLTYPES)
    cr = db.cursor()
    print("connected dataBase")
    insert_value = '''INSERT INTO Visitings('date_visited', 'person_id', 'visitor_name', 'mountin_minuts')
                      VALUES(?, ?, ?, ?)'''


    # YYYY-MM-DD HH:MI:SS
    # "%Y-%m-%d, %H:%M:%S"
    d = datetime(2003, 2, 15, 4, 20, 00).strftime("%d-%m-%Y, %H:%M:%S")
    print(type(d))
    print(d)
    dd = datetime.strptime("15-2-2004, 05:05:05", "%d-%m-%Y, %H:%M:%S")
    print(type(dd))
    print(dd)
    # date_var = time.strptime("07:33:44", '%H:%M:%S')
    date_var = datetime.strptime("07:33:44", '%H:%M:%S')
    date_var = date_var.time()
    print(date_var)
    print(type(date_var))

    temp = (d, 2, "zzzzzzzzzzz", date_var)

    cr.execute(insert_value, temp)
    db.commit()
    print("sent values")

    selectAll = '''SELECT * FROM Visitings'''
    cr.execute(selectAll)
    records = cr.fetchall()
    # db.commit()
    convert = None
    for row in records:
        print(f'id {row[0]}\n'
              f'date_visited: {row[1]} type {type(row[1])}\n'
              f'person_id: {row[2]}\n'
              f'visitor_name: {row[3]}\n'
              f'mountin_minuts: {row[4]}, type {type(row[4])}\n')
        convert = row[1]
        print("*" * 40)
    print("$" * 40)
    print("$" * 40)
    convert = datetime.strptime(convert, '%Y-%m-%d, %H:%M:%S')
    print(type(convert))


    cr.close()

except sq.Error as error:
    print("Error while working with SQLite", error)
finally:
    if (db):
        db.close()
        print("sqlite connection is closed")


