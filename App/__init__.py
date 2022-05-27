import sqlite3 as sq
from datetime import date
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
    insert_value = ('''INSERT INTO Person('first_name', 'father', 'last_name', 'gender', 'birth_year', 'address')
            VALUES(?, ?, ?, ?, ?, ?)''')
    d = date(2003, 2, 15)
    temp = ("name", "fatheer", "lastName", "male", d, "Azaz")

    cr.execute(insert_value, temp)
    db.commit()
    print("sent values")

    selectAll = '''SELECT * FROM Person'''
    cr.execute(selectAll)
    records = cr.fetchall()
    
    for row in records:
        print(f'id {row[0]}\n'
              f'Full Name: {row[1]}\n'
              f'Father: {row[2]}\n'
              f'Last Name: {row[3]}\n'
              f'Gender: {row[4]}\n'
              f'Birth Year: {row[5]} type {type(row[5])}\n'
              f'Address: {row[6]}')
        print("*" * 40)

        cr.close()

except sq.Error as error:
    print("Error while working with SQLite", error)
finally:
    if (db):
        db.close()
        print("sqlite connection is closed")



# print values

