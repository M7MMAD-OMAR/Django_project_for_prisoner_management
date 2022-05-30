from datetime import datetime as dt

import Connect_DB as c_DB


class Person:
    """
    have class Person method and properties ID, First Name, Father, Last Name.......
    and Get, Set All Properties
    """

    def __init__(self, fn: str, father: str, ls: str, gender: str, by: str, address: str):
        self.set_first_name(fn.strip())
        self.set_father(father.strip())
        self.set_last_name(ls.strip())
        self.set_gender(gender.strip())
        self.set_birth_year(by.strip())
        self.set_address(address.strip())

    def __str__(self):
        print(f'First Name: {self.__first_name}\n'
              f'Father: {self.__father}\n'
              f'Last Name: {self.__last_name}\n'
              f'Gender: {self.__gender}\n'
              f'Birth Year: {self.__birth_year}\n'
              f'Address: {self.__address}')

    def add_person(self, fn: str, father: str, ls: str, gender: str, by: str, address: str):
        """Add person to DataBase and check all Values"""
        global db
        try:
            p = Person(fn, father, ls, gender, by, address)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Person('first_name', 'father', 'last_name', 'gender', 'birth_year', 'address')
                      VALUES (?, ?, ?, ?, ?, ?)"""
            temp_val = (self.get_first_name(), self.get_father(), self.get_last_name(),
                        self.get_gender(), self.get_birth_year(), self.get_address())
            cu = db.cursor()
            cu.execute(temp_str, temp_val)
            db.commit()
            print("Sent Values Person successfully")
        except Exception as ex:
            print(ex)
        finally:
            if db:
                db.close()
                print("Closed DataBase from add person")

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, fn: str):
        if c_DB.check(fn, "Error: First Name must be greater than one Character"):
            self.__first_name = fn

    def get_father(self):
        return self.__father

    def set_father(self, f: str):
        if c_DB.check(f, "Error: Father must be greater than one Character"):
            self.__father = f

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, ln: str):
        if c_DB.check(ln, "Error: Last Name must be greater than one Character"):
            self.__last_name = ln

    def get_gender(self):
        return self.__gender

    def set_gender(self, g: str):
        if g != "male" and g != "female":
            raise ValueError("Error: Gender must be 'male' or 'female'")
        else:
            self.__gender = g

    def get_birth_year(self):
        return self.__birth_year

    def set_birth_year(self, by: str):
        if not (by.__contains__(' ')):
            temp = dt.strptime(by, "%d-%m-%Y")
            date_now = dt.now()
            if temp > dt.now():
                raise ValueError(
                    f'Error: Birth Year must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
            else:
                self.__birth_year = by
        else:
            raise ValueError("Error: Birth Year must be don't contain space")

    def get_address(self):
        return self.__address

    def set_address(self, a: str):
        if c_DB.check(a, "Error: Address must be greater than one Character"):
            self.__address = a
