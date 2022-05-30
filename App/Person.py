import sqlite3 as sq

import Connect_DB as c_DB


class Person:
    """
    have class Person method and properties ID, First Name, Father, Last Name.......
    and Get, Set All Properties
    """

    def __init__(self, fn, father, ls, gender, by, address):
        # if  len(fn) > 1 and len(father) > 1 and len(ls) > 1 and len(address) > 1 and (gender == "male" or "female") and (by is not None):
        # self.__Id = id
        # self.__first_name = fn
        # self.__father = father
        # self.__last_name = ls
        # self.__gender = gender
        # self.__birth_year = by
        # self.__address = address
        self.set_first_name(fn.strip())
        self.set_father(father.strip())
        self.set_last_name(ls.strip())
        self.set_gender(gender.strip())
        self.set_birth_year(by.strip())
        self.set_address(address.strip())

    # else:

    def __str__(self):
        # print(f'Name Object: {self}')
        print(f'First Name: {self.__first_name}\n'
              f'Father: {self.__father}\n'
              f'Last Name: {self.__last_name}\n'
              f'Gender: {self.__gender}\n'
              f'Birth Year: {self.__birth_year}\n'
              f'Address: {self.__address}')

    # def get_id(self):
    #     return self.__Id
    #
    # def set_id(self, id):
    #     if id <= 0:
    #         raise ValueError("Error: from person id")
    #     else:
    #         self.__Id = id


    def add_person(self):
        """Add person to DataBase and check all Values"""
        global db
        try:
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Person('first_name', 'father', 'last_name', 'gender', 'birth_year', 'address')
                      VALUES (?, ?, ?, ?, ?, ?)"""
            temp_val = [self.get_first_name(), self.get_father(), self.get_last_name(),
                        self.get_gender(), self.get_birth_year(), self.get_address()]
            cu = db.cursor()
            cu.execute(temp_str, temp_val)
            db.commit()
            print("Sent Values Person successfully")
        # except sq.Error as ex:
        #     print("Error Database from add person", ex)
        except Exception as ex:
            print(ex)
        finally:
            if db:
                db.close()
                print("Closed DataBase from add person")

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, fn: str):
        if c_DB.check(fn, "Error: from person first name"):
            self.__first_name = fn
        # if len(fn) <= 1:
        #     raise ValueError("Error: from person first name")
        # else:
        #     self.__first_name = fn

    def get_father(self):
        return self.__father

    def set_father(self, f: str):
        if c_DB.check(f, "Error: from person father"):
            self.__father = f
        # if len(f) <= 1:
        #     raise ValueError("Error: from person father")
        # else:
        #     self.__father = f

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, ln: str):
        if c_DB.check(ln, "Error: from person last name"):
            self.__last_name = ln
        # if len(ln) <= 1:
        #     raise ValueError("Error: from person last name")
        # else:
        #     self.__last_name = ln

    def get_gender(self):
        return self.__gender

    def set_gender(self, g: str):
        if g != "male" and g != "female":
            raise ValueError("Error: from person gender")
        else:
            self.__gender = g

    def get_birth_year(self):
        return self.__birth_year

    def set_birth_year(self, by: str):
        if c_DB.check(by, "Error: from person birth year"):
            self.__birth_year = by
        # if len(by) <= 3:
        #     raise ValueError("Error: from person birth year")
        # else:
        #     self.__birth_year = by

    def get_address(self):
        return self.__address

    def set_address(self, a: str):
        if c_DB.check(a, "Error: from person address"):
            self.__address = a
        # if len(a) <= 2:
        #     raise ValueError("Error: from person address")
        # else:
        #     self.__address = a
