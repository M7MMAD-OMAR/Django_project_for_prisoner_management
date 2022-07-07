import json

import Connect_DB as c_DB
from App.Abstract_JSON import Abstract_JSON


class Dungeon(Abstract_JSON):
    """
    have class Dungeon method and properties Name, Size.......
    and Get, Set All Properties
    """

    __json_file = "../JSON/Dungeon.js ' %}on"

    def __init__(self, name: str, size: int):
        self.name = name.strip()
        self.size = size

    @classmethod
    def __str__(cls):
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Dungeon"""
            # Result Format
            count = 0
            print("#".center(8, ' '), end=' | ')
            print("ID".center(9, ' '), end=' | ')
            print("Name".center(30, ' '), end=' | ')
            print("Size".center(10, ' '), end=' | \n')
            print("-" * 80)
            for row in db.cursor().execute(temp_str).fetchall():
                count += 1
                print(f' {str(count).zfill(3)} '.center(7, ' '),
                      f' {row[0]} '.center(15, ' '),
                      f' {row[1]} '.center(30, ' '),
                      f' {row[2]} '.center(11, ' '))
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def add_dungeon(cls, name: str, size: int):
        """Add dungeon in DB and add in json file and check all data"""
        db = None
        try:
            d = Dungeon(name, size)
            db = c_DB.connect_DB()
            cu = db.cursor()
            temp_sql_select = """SELECT Id FROM Dungeon ORDER BY Id DESC LIMIT 1;"""
            temp_sql_insert = """INSERT INTO Dungeon('name', 'size') VALUES(?, ?)"""
            temp_val = (d.name, d.size)
            cu.execute(temp_sql_insert, temp_val)
            db.commit()

            # Add Dungeon in Dungeon.js ' %}on file by id Dungeon inserted.
            cu.execute(temp_sql_select)

            dungeon_id = cu.fetchone()

            # Convert Dungeon id to Integer
            dungeon_id = int(dungeon_id[0])

            # Open Dungeon.js ' %}on file and add Dungeon
            with open(Dungeon.__json_file) as jf:
                data = json.load(jf)
            temp = data
            temp.append({"Id": dungeon_id, "name": d.name, "size": d.size})
            c_DB.write_json(temp, Dungeon.__json_file)
            print("Added Dungeon in json file and Database successfully")
        except AttributeError as ex:
            raise ex
        except ValueError as ex:
            raise ex
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    @classmethod
    def delete_dungeon_by_id(cls, *dungeons_ids):
        """
        delete Dungeon from database by id
        and delete Dungeon in Dungeon.js ' %}on file by id
        Warning: if Dungeon id referencing other tables, you can't delete Dungeon
        """
        db = None
        try:
            db = c_DB.connect_DB()
            cu = db.cursor()

            temp_sql_select = """SELECT Id from Dungeon WHERE Id = :id;"""
            temp_sql_delete = """DELETE FROM Dungeon WHERE Id = :id;"""

            #   This Queries because check
            #   if There is data show warning in order to delete Dungeon
            #   else delete Dungeon only
            temp_sql_select_inner_join = """SELECT  d.Id, dm.Id FROM Dungeon AS d
                            INNER JOIN Dungeon_Moves AS dm ON d.id = dm.dungeon_id WHERE d.Id = :d_id LIMIT 1"""

            for dungeon_id in dungeons_ids:

                #   select Dungeon by id in order to check find Dungeon id
                cu.execute(temp_sql_select, {"id": dungeon_id})
                if not cu.fetchone():
                    raise ValueError(f"Error: Dungeon ID {dungeon_id} is not found in your data, please try again!")

                # Check Dungeon if referencing other tables raise error else cancel this and delete value
                cu.execute(temp_sql_select_inner_join, {"d_id": dungeon_id})
                if cu.fetchone():
                    raise ValueError(
                        f"Error: Dungeon {dungeon_id} referencing in Dungeon Moves table, You can't delete this Offense")

                # delete the Dungeon by id
                cu.execute(temp_sql_delete, {"id": dungeon_id})
                db.commit()

                # Delete Dungeon in Dungeon.js ' %}on file, by Dungeon ID
                new_dungeon_data = []
                with open(Dungeon.__json_file, "r") as jf:
                    data = json.load(jf)

                # if id in json file keep change
                # else append Dungeon json in new_dungeon_data
                # finally update Dungeon.js ' %}on file by new_dungeon_data
                for row in data:
                    if row["Id"] == dungeon_id:
                        pass
                    else:
                        new_dungeon_data.append(row)
                c_DB.write_json(new_dungeon_data, Dungeon.__json_file)

            print("Delete Dungeon's in json file and Database successfully")

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
        Connect DB and select all Dungeon
        loading json file and append values to new json file
        finally clear json file and add all values with DB
        Warning: This method will delete all old values in json files then add Dungeon with DB
        """
        db = None
        try:
            db = c_DB.connect_DB()
            temp_sql_select = """SELECT * FROM Dungeon"""
            data = []
            for row in db.cursor().execute(temp_sql_select).fetchall():
                data.append({"Id": row[0], "name": row[1], "size": row[2]})
            c_DB.write_json(data, Dungeon.__json_file)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.commit()
                db.close()

    @classmethod
    def print_all_data_by_json(cls):
        """Print Dungeon data in json file only"""
        with open(Dungeon.__json_file, "r") as jf:
            data = json.load(jf)
        # Result Format
        count = 0
        print("#".center(8, ' '), end=' | ')
        print("ID".center(9, ' '), end=' | ')
        print("Name".center(30, ' '), end=' | ')
        print("Size".center(10, ' '), end=' | \n')
        print("-" * 80)
        for row in data:
            count += 1
            print(f' {str(count).zfill(3)} '.center(7, ' '),
                  f' {row["Id"]} '.center(15, ' '),
                  f' {row["name"]} '.center(30, ' '),
                  f' {row["size"]} '.center(11, ' '))

    """Start Getter and Setter Properties"""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """change name and check name is in DB then not change name
        or name is not created in DB then change name"""
        if len(name) <= 1:
            raise ValueError("Error: length name is a few char")
        else:
            db = None
            try:
                db = c_DB.connect_DB()
                temp_sql_select = """SELECT name FROM Dungeon WHERE name=:name"""
                cu = db.cursor()
                cu.execute(temp_sql_select, {"name": name})
                if not (cu.fetchone()):
                    self.__name = name.title()
                else:
                    raise c_DB.sq.ProgrammingError("Error: Dungeon name is already defined, Please change value name")
            except c_DB.sq.ProgrammingError as ex:
                raise ex
            except ValueError as ex:
                raise ex
            except Exception as ex:
                raise ex
            finally:
                if db:
                    db.close()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size <= 0:
            raise ValueError("Error: Size must be greater then Zero")
        else:
            self.__size = size

    """End Getter and Setter Properties"""
