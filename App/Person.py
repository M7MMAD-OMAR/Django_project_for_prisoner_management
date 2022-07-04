import json

import Connect_DB as c_DB





class Person:
    """
    have class Person method and properties First Name, Father, Last Name.......
    and Get, Set All Properties
    """
    __json_file = "../JSON/person.json"

    def __init__(self, fn: str, father: str, ls: str, gender: str, by, address: str):
        self.first_name = fn.strip()
        self.father = father.strip()
        self.last_name = ls.strip()
        self.gender = gender.strip()
        self.birth_year = by
        self.address = address.strip()

    @classmethod
    def __str__(cls):
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Person"""
            count = 0
            for row in db.cursor().execute(temp_str).fetchall():
                count += 1
                print(str(count), "".center(50, '-'))
                print(f'ID:         {row[0]}\n'
                      f'First Name: {row[1]}\n'
                      f'Father:     {row[2]}\n'
                      f'Last Name:  {row[3]}\n'
                      f'Gender:     {row[4]}\n'
                      f'Birth Year: {row[5]}\n'
                      f'Address:    {row[6]}')
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.commit()
                db.close()


    @classmethod
    def __write_json(cls, date):
        """Write data in person.json file"""
        with open(Person.__json_file, "w") as jf:
            json.dump(date, jf, indent=4)


    @classmethod
    def add_person(cls, fn: str, father: str, ls: str, gender: str, by, address: str):
        """Add person to DataBase and person.json file and check all Values"""
        db = None
        try:
            p = Person(fn, father, ls, gender, by, address)
            db = c_DB.connect_DB()
            temp_sql_insert = """INSERT INTO Person('first_name', 'father', 'last_name', 'gender', 'birth_year', 'address')
                      VALUES (:fn, :f, :ls, :g, :by, :a)"""
            temp_sql_select = """SELECT  Id FROM Person ORDER BY Id DESC LIMIT 1"""
            temp_val = {"fn": p.first_name, "f": p.father, "ls": p.last_name, "g": p.gender, "by": p.birth_year,
                        "a": p.address}
            cu = db.cursor()
            cu.execute(temp_sql_insert, temp_val)
            db.commit()
            print("Sent Values Person successfully")


            # Add person in person.json file by id person inserted.
            cu.execute(temp_sql_select)

            id = cu.fetchone()
            # Convert person id to Integer
            id = int(id[0])

            # Open person.json file and add person
            with open(Person.__json_file) as jf:
                date = json.load(jf)
                temp = date["persons"]
                temp.append({"Id": id, "first_name": p.first_name, "father": p.father, "last_name": p.last_name,
                             "gender": p.gender, "birth_year": str(p.birth_year), "address": p.address})
                Person.__write_json(date)
            print("Added Person in json file successfully")
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    """Start Getter and Setter Properties."""

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
            self.__father = f.strip()

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
    def birth_year(self, by: c_DB.d):
        try:
            temp_date = c_DB.d(by.year, by.month, by.day)
            date_now = c_DB.d.today()
            if temp_date > date_now:
                raise ValueError(
                    f'Error: Birth Year must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
            else:
                if temp_date < c_DB.d(1000, 1, 1):
                    raise ValueError("Error: Birth Year must be greater than 1000:01:01")
                else:
                    self.__birth_year = by
        except Exception as ex:
            raise Exception(ex)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, a: str):
        if c_DB.check(a, "Error: Address must be greater than one Character"):
            self.__address = a

    """End Getter and Setter Properties."""
