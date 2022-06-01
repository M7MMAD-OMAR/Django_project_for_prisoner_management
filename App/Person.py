import Connect_DB as c_DB


class Person:
    """
    have class Person method and properties First Name, Father, Last Name.......
    and Get, Set All Properties
    """

    cls = None

    def __init__(self, fn: str, father: str, ls: str, gender: str, by: str, address: str):
        cls = self
        self.first_name = fn.strip()
        self.father = father.strip()
        self.last_name = ls.strip()
        self.gender = gender.strip()
        self.birth_year = by.strip()
        self.address = address.strip()

    def __str__(self):
        print(f'First Name: {self.first_name}\n'
              f'Father: {self.father}\n'
              f'Last Name: {self.last_name}\n'
              f'Gender: {self.gender}\n'
              f'Birth Year: {self.birth_year}\n'
              f'Address: {self.address}')

    def add_person(self, fn: str, father: str, ls: str, gender: str, by: str, address: str):
        """Add person to DataBase and check all Values"""
        global db
        try:
            Person(fn, father, ls, gender, by, address)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Person('first_name', 'father', 'last_name', 'gender', 'birth_year', 'address')
                      VALUES (?, ?, ?, ?, ?, ?)"""
            temp_val = (fn, father, ls, gender, by, address)
            cu = db.cursor()
            cu.execute(temp_str, temp_val)
            db.commit()
            print("Sent Values Person successfully")
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, fn: str):
        if c_DB.check(fn, "Error: First Name must be greater than one Character"):
            self.__first_name = fn

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, f: str):
        if c_DB.check(f, "Error: Father must be greater than one Character"):
            self.__father = f

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, ln: str):
        if c_DB.check(ln, "Error: Last Name must be greater than one Character"):
            self.__last_name = ln

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, g: str):
        if g != "male" and g != "female":
            raise ValueError("Error: Gender must be 'male' or 'female'")
        else:
            self.__gender = g

    @property
    def birth_year(self):
        return self.__birth_year

    @birth_year.setter
    def birth_year(self, by: str):
        if by.__contains__(' '):
            raise ValueError("Error: Birth Year must be don't contain space")
        else:
            if len(by) > 10:
                raise ValueError("Error: Birth Year is correct")
            else:
                try:
                    temp = c_DB.dt.strptime(by, "%d-%m-%Y")
                    date_now = c_DB.dt.now()
                    if temp > date_now:
                        raise TypeError(
                            f'Error: Birth Year must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
                    else:
                        self.__birth_year = by
                except TypeError as ex:
                    raise TypeError(ex)
        # if not (by.__contains__(' ')):
        #     temp = c_DB.dt.strptime(by, "%d-%m-%Y")
        #     date_now = c_DB.dt.now()
        #     if temp > c_DB.dt.now():
        #         raise ValueError(
        #             f'Error: Birth Year must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
        #     else:
        #         self.__birth_year = by
        # else:
        #     raise ValueError("Error: Birth Year must be don't contain space")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, a: str):
        if c_DB.check(a, "Error: Address must be greater than one Character"):
            self.__address = a
