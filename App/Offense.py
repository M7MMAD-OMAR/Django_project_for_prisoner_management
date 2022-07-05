import json

import Connect_DB as c_DB
from App.Abstract_JSON import Abstract_JSON


class Offense(Abstract_JSON):
    """
    have class Offense method and properties name.......
    and Get, Set All Properties
    """

    __json_file = "../JSON/Offense.json"

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def __str__(cls):
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Offense"""
            # Result Format
            count = 0
            print("#".center(8, ' '), end=' | ')
            print("ID".center(9, ' '), end=' | ')
            print("Name".center(30, ' '), end=' | \n')
            print("-" * 60)
            for row in db.cursor().execute(temp_str).fetchall():
                count += 1
                print(f' {str(count).zfill(3)} '.center(7, ' '),
                      f' {row[0]} '.center(15, ' '),
                      f' {row[1]} '.center(28, ' '))
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def add_offense(cls, name: str):
        """
        Add Offense value In DB and check value
        and Add offense value in json file
        """
        db = None
        try:
            o = Offense(name)
            db = c_DB.connect_DB()
            cu = db.cursor()
            temp_str = """INSERT INTO Offense('name') VALUES(:n)"""
            #   this query get last inserted person then person add in json file
            temp_sql_select = """SELECT Id FROM Offense ORDER BY Id DESC LIMIT 1;"""
            cu.execute(temp_str, {"n": o.name})
            db.commit()

            # Add Offense in Offense.json file by id Offense inserted.
            cu.execute(temp_sql_select)

            offense_id = cu.fetchone()

            # Convert Offense id to Integer
            offense_id = int(offense_id[0])

            # Open Offense.json file and add Offense
            with open(Offense.__json_file) as jf:
                data = json.load(jf)
            temp = data
            temp.append({"Id": offense_id, "name": o.name})
            c_DB.write_json(temp, Offense.__json_file)
            print("Added Offense in json file and Database successfully")


        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    @classmethod
    def delete_offense_by_id(cls, *offense_ids):
        """
        delete Offense from database by id
        and delete Offense in Offense.json file by id
        Warning: if Offense id referencing other tables, you can't delete Offense
        """
        db = None
        try:
            db = c_DB.connect_DB()

            temp_sql_select = """SELECT Id from Offense WHERE Id = :id;"""
            temp_sql_delete = """DELETE FROM Offense WHERE Id = :id;"""

            #   This Queries because check
            #   if There is data show warning in order to delete Offense
            #   else delete Offense only
            temp_sql_select_inner_join = """SELECT  o.Id, c.Id FROM Offense AS o 
                            INNER JOIN Convicts AS c ON o.id = c.offense_id WHERE o.Id = :o_id LIMIT 1"""


            cu = db.cursor()

            for offense_id in offense_ids:

                #   select Offense by id in order to check find Offense id
                cu.execute(temp_sql_select, {"id": offense_id})
                if not cu.fetchone():
                    raise ValueError(f"Error: Offense ID {offense_id} is not found in your data, please try again!")

                # Check Offense if referencing other tables raise error else cancel this and delete value
                cu.execute(temp_sql_select_inner_join, {"o_id": offense_id})
                if cu.fetchone():
                    raise ValueError(
                        f"Error: Offense {offense_id} referencing in Convicts table, You can't delete this Offense")

                # delete the Offense by id
                cu.execute(temp_sql_delete, {"id": offense_id})
                db.commit()

                # Delete Offense in Offense.json file, by Offense ID
                new_offense_data = []
                with open(Offense.__json_file, "r") as jf:
                    data = json.load(jf)

                # if id in json file keep change
                # else append Offense json in new_offense_data
                # finally update Offense.json file by new_offense_data
                for row in data:
                    if row["Id"] == offense_id:
                        pass
                    else:
                        new_offense_data.append(row)
                c_DB.write_json(new_offense_data, Offense.__json_file)

            print("Delete Offense's in json file and Database successfully")

        except ValueError as ex:
            raise ex
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()


    @classmethod
    def reset_json_by_database(cls):
        """
        Connect DB and select all Offense
        loading json file and append values to new json file
        finally clear json file and add all values with DB
        Warning: This method will delete all old values in json files then add Offense with DB
        """
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Offense"""
            data = []
            for row in db.cursor().execute(temp_str).fetchall():
                data.append({"Id": row[0], "name": row[1]})
            c_DB.write_json(data, Offense.__json_file)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.commit()
                db.close()

    @classmethod
    def print_all_data_by_json(cls):
        """Print Offense data in json file only"""
        with open(Offense.__json_file, "r") as jf:
            data = json.load(jf)
        # Result Format
        count = 0
        print("#".center(8, ' '), end=' | ')
        print("ID".center(9, ' '), end=' | ')
        print("Name".center(30, ' '), end=' | \n')
        print("-" * 60)
        for row in data:
            count += 1
            print(f' {str(count).zfill(3)} '.center(7, ' '),
                  f' {row["Id"]} '.center(15, ' '),
                  f' {row["name"]} '.center(28, ' '))




    """Start Getter and Setter Properties."""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if len(n) <= 1:
            raise ValueError("Error: Offense name must be greater than one Character")
        else:
            db = None
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT name FROM Offense WHERE name=:n"""
                if db.cursor().execute(temp_str, {"n": n}).fetchone():
                    raise ValueError("Error: Offense Name is already defined")
                else:
                    self.__name = n
            except ValueError as ex:
                raise ex
            except Exception as ex:
                raise ex
            finally:
                if db:
                    db.close()

    """End Getter and Setter Properties."""
