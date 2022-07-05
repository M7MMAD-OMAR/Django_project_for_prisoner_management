import json

import Connect_DB as c_DB


class Person:
    """
    have class Person method and properties First Name, Father, Last Name.......
    and Get, Set All Properties
    """
    __json_file = "../JSON/Person.json"

    def __init__(self, fn: str, father: str, ls: str, gender: str, by, address: str):
        self.first_name = fn.strip()
        self.father = father.strip()
        self.last_name = ls.strip()
        self.gender = gender.strip()
        self.birth_year = by
        self.address = address.strip()

    @classmethod
    def __str__(cls):
        """Print all person values by DB"""
        db = None
        try:
            db = c_DB.connect_DB()
            temp_sql_select = """SELECT * FROM Person"""

            # result Format
            count = 0
            print("#".center(8, ' '), end=' | ')
            print("ID".center(8, ' '), end=' | ')
            print("First Name".center(15, ' '), end=' | ')
            print("Father".center(16, ' '), end=' | ')
            print("Last Name".center(20, ' '), end=' | ')
            print("Gender".center(15, ' '), end=' | ')
            print("Birth Year".center(20, ' '), end=' | ')
            print("Address".center(25, ' '), end=' | \n')
            print("-" * 150)
            for row in db.cursor().execute(temp_sql_select).fetchall():
                count += 1
                print(f' {str(count).zfill(3)} '.center(7, ' '),
                      f' {row[0]} '.center(14, ' '),
                      f' {row[1]} '.center(12, ' '),
                      f' {row[2]} '.center(23, ' '),
                      f' {row[3]} '.center(20, ' '),
                      f' {row[4]} '.center(20, ' '),
                      f' {row[5]} '.center(20, ' '),
                      f' {row[6]} '.center(28, ' '))
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.commit()
                db.close()

    @classmethod
    def delete_persons_by_id(cls, *persons_ids):
        """
        delete person from database by id
        and delete person in Person.json file by id
        """
        db = None
        try:
            db = c_DB.connect_DB()
            temp_sql_select = """SELECT Id from Person WHERE Id = :id;"""
            temp_sql_delete = """DELETE FROM Person WHERE Id = :id;"""

            for person_id in persons_ids:
                # select person by id in order to check find person id
                cu = db.cursor()
                cu.execute(temp_sql_select, {"id": person_id})
                if not cu.fetchone():
                    raise ValueError(f"Error: Person ID {person_id} is not found in your data, please try again!")

                # it's True! delete the person by id
                cu = db.cursor()
                cu.execute(temp_sql_delete, {"id": person_id})
                db.commit()

                # Delete person in Person.json file, by person ID
                new_person_data = []
                with open(Person.__json_file, "r") as jf:
                    data = json.load(jf)

                # if id in json file keep change
                # else append person json in new_person_data
                # finally update Person.json file by new_person_data
                for row in data:
                    if row["Id"] == person_id:
                        pass
                    else:
                        new_person_data.append(row)
                c_DB.write_json(new_person_data, Person.__json_file)
            print("Delete Person's in json file and Database successfully")

        except ValueError as ex:
            raise ex
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    @classmethod
    def add_person(cls, fn: str, father: str, ls: str, gender: str, by, address: str):
        """Add person to DataBase and Person.json file and check all Values"""
        db = None
        try:
            p = Person(fn, father, ls, gender, by, address)
            db = c_DB.connect_DB()
            temp_sql_insert = """INSERT INTO Person('first_name', 'father', 'last_name', 'gender', 'birth_year', 'address')
                          VALUES (:fn, :f, :ls, :g, :by, :a);"""
            temp_sql_select = """SELECT  Id FROM Person ORDER BY Id DESC LIMIT 1;"""
            temp_val = {"fn": p.first_name, "f": p.father, "ls": p.last_name, "g": p.gender, "by": p.birth_year,
                        "a": p.address}
            cu = db.cursor()
            cu.execute(temp_sql_insert, temp_val)
            db.commit()

            # Add person in Person.json file by id person inserted.
            cu.execute(temp_sql_select)

            person_id = cu.fetchone()

            # Convert person id to Integer
            person_id = int(person_id[0])

            # Open Person.json file and add person
            with open(Person.__json_file) as jf:
                data = json.load(jf)
            temp = data
            temp.append({"Id": person_id, "first_name": p.first_name, "father": p.father, "last_name": p.last_name,
                         "gender": p.gender, "birth_year": str(p.birth_year), "address": p.address})
            c_DB.write_json(temp, Person.__json_file)
            print("Added Person in json file and Database successfully")

        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()


    @classmethod
    def reset_json_by_database(cls):
        """
        Connect DB and select all persons
        loading json file and append values to new json file
        finally clear json file and add all values with DB
        Warning: This method will delete all old values in json files then add persons with DB
        """
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Person"""
            data = []
            for row in db.cursor().execute(temp_str).fetchall():
                data.append({"Id": row[0], "first_name": row[1], "father": row[2], "last_name": row[3],
                             "gender": row[4], "birth_year": str(row[5]), "address": row[6]})
            c_DB.write_json(data, Person.__json_file)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.commit()
                db.close()

    @classmethod
    def print_all_data_by_json(cls):
        """Print Person data in json file only"""
        with open(Person.__json_file, "r") as jf:
            data = json.load(jf)
        # Format result
        count = 0
        print("#".center(8, ' '), end=' | ')
        print("ID".center(8, ' '), end=' | ')
        print("First Name".center(15, ' '), end=' | ')
        print("Father".center(16, ' '), end=' | ')
        print("Last Name".center(20, ' '), end=' | ')
        print("Gender".center(15, ' '), end=' | ')
        print("Birth Year".center(20, ' '), end=' | ')
        print("Address".center(25, ' '), end=' | \n')
        print("-" * 150)
        for row in data:
            count += 1
            print(f' {str(count).zfill(3)} '.center(7, ' '),
                  f' {row["Id"]} '.center(14, ' '),
                  f' {row["first_name"]} '.center(12, ' '),
                  f' {row["father"]} '.center(23, ' '),
                  f' {row["last_name"]} '.center(20, ' '),
                  f' {row["gender"]} '.center(20, ' '),
                  f' {row["birth_year"]} '.center(20, ' '),
                  f' {row["address"]} '.center(28, ' '))

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
