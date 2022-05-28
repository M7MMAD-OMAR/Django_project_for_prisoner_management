class Person:
    """
    have class Person method and properties ID, First Name, Father, Last Name.......
    and Get, Set All Properties
    """

    def __init__(self, id, fn, father, ls, gender, by, address):
        if id > 0 and len(fn and father and ls and address) > 1 and (gender == "male" or "female") and (by is not None):
            self.__Id = id
            self.__first_name = fn
            self.__father = father
            self.__last_name = ls
            self.__gender = gender
            self.__birth_year = by
            self.__address = address
        else:
            raise Exception("Error in Person parameter constructor")

    def __str__(self):
        print(f'Name Object: {self}')
        print(f'ID: {self.__Id}\n'
              f'First Name: {self.__first_name}\n'
              f'Father: {self.__father}\n'
              f'Last Name: {self.__last_name}\n'
              f'Gender: {self.__gender}\n'
              f'Birth Year: {self.__birth_year}\n'
              f'Address: {self.__address}')

    def get_id(self):
        return self.__Id

    def set_id(self, id):
        if id <= 0:
            raise ValueError("Error: from person id")
        else:
            self.__Id = id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, fn):
        if len(fn) <= 1:
            raise ValueError("Error: from person first name")
        else:
            self.__first_name = fn

    def get_father(self):
        return self.__father

    def set_father(self, f):
        if len(f) <= 1:
            raise ValueError("Error: from person father")
        else:
            self.__father = f

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, ln):
        if len(ln) <= 1:
            raise ValueError("Error: from person last name")
        else:
            self.__last_name = ln

    def get_gender(self):
        return self.__gender

    def set_gender(self, g):
        if g != "male" or "female":
            raise ValueError("Error: from person gender")
        else:
            self.__gender = g

    def get_birth_year(self):
        return self.__birth_year

    def set_birth_year(self, by):
        if by is None:
            raise ValueError("Error: from person birth year")
        else:
            self.__birth_year = by

    def get_address(self):
        return self.__address

    def set_address(self, a):
        if len(a) <= 1:
            raise ValueError("Error: from person address")
        else:
            self.__address = a
