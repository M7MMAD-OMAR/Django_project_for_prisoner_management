import json

import Connect_DB as c_DB
from App.Abstract_JSON import Abstract_JSON


class Dungeon_Moves(Abstract_JSON):
    """
    have class Dungeon_Moves method and properties Dungeon ID, Person ID, From Date.......
    and Get, Set All Properties
    """
    __json_file = "../JSON/Dungeon_Moves.json"
    def __init__(self, dungeon_id: int, person_id: int, from_date):
        self.dungeon_id = dungeon_id
        self.person_id = person_id
        self.from_date = from_date

    @classmethod
    def __str__(cls):
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Dungeon_Moves"""
            # Result Format
            print("#".center(8, ' '), end=' | ')
            print("ID".center(8, ' '), end=' | ')
            print("Dungeon ID".center(8, ' '), end=' | ')
            print("Person ID".center(8, ' '), end=' | ')
            print("From Date".center(14, ' '), end=' | \n')
            print("-" * 70)
            count = 0
            for row in db.cursor().execute(temp_str).fetchall():
                count += 1
                print(f' {str(count).zfill(3)} '.center(7, ' '),
                      f' {row[0]} '.center(13, ' '),
                      f' {row[1]} '.center(10, ' '),
                      f' {row[2]} '.center(13, ' '),
                      f' {row[3]} '.center(14, ' '))
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def add_dungeon_moves(cls, dungeon_id: int, person_id: int, from_date):
        """Add Dungeon Moves to DB and Dungeon_Moves.json file and check all values"""
        db = None
        try:
            dm = Dungeon_Moves(dungeon_id, person_id, from_date)
            db = c_DB.connect_DB()
            cu = db.cursor()
            temp_sql_insert = """INSERT INTO Dungeon_Moves('dungeon_id', 'person_id', 'from_date') VALUES(?, ?, ?)"""
            temp_sql_select = """SELECT Id FROM Dungeon_Moves ORDER BY Id DESC LIMIT 1;"""

            temp_val = (dm.dungeon_id, dm.person_id, dm.from_date)
            cu.execute(temp_sql_insert, temp_val)
            db.commit()

            cu.execute(temp_sql_select)
            dungeon_moves_id = cu.fetchone()

            # Convert Dungeon Moves id to Integer
            convicts_id = int(dungeon_moves_id[0])

            # Open Dungeon_Moves.json file and add Dungeon Moves
            with open(Dungeon_Moves.__json_file) as jf:
                data = json.load(jf)
            temp = data
            temp.append(
                {"Id": convicts_id, "dungeon_id": dm.dungeon_id, "person_id": dm.person_id, "from_date": str(dm.from_date)})

            #   write json file and added change
            c_DB.write_json(data, Dungeon_Moves.__json_file)

            print("Added Dungeon Moves in json file and Database successfully")



        except c_DB.sq.ProgrammingError as ex:
            raise ex
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()


    @classmethod
    def delete_dungeon_moves_by_id(cls, *dungeon_moves_ids):
        """
        delete Dungeon Moves from database by id
        and delete Dungeon Moves in Dungeon_Moves.json file by id
        """

        db = None
        try:
            db = c_DB.connect_DB()
            cu = db.cursor()

            temp_sql_select = """SELECT Id from Dungeon_Moves WHERE Id = :id;"""
            temp_sql_delete = """DELETE FROM Dungeon_Moves WHERE Id = :id;"""

            for dungeon_moves_id in dungeon_moves_ids:

                #   select Dungeon Moves by id in order to check  Dungeon Moves id
                cu.execute(temp_sql_select, {"id": dungeon_moves_id})
                if not cu.fetchone():
                    raise ValueError(f"Error: Convicts ID {dungeon_moves_id} is not found in your data, please try again!")

                # delete the Dungeon Moves by id
                cu.execute(temp_sql_delete, {"id": dungeon_moves_id})
                db.commit()

                # Delete Dungeon Moves in Dungeon Moves.json file, by Dungeon Moves ID
                new_dungeon_moves_data = []
                with open(Dungeon_Moves.__json_file, "r") as jf:
                    data = json.load(jf)

                # if id in json file keep change
                # else append Dungeon Moves json in new_dungeon_moves_data
                # finally update Dungeon Moves.json file by new_dungeon_moves_data
                for row in data:
                    if row["Id"] == dungeon_moves_id:
                        pass
                    else:
                        new_dungeon_moves_data.append(row)
                c_DB.write_json(new_dungeon_moves_data, Dungeon_Moves.__json_file)

            print("Delete Dungeon Move's in json file and Database successfully")


        except ValueError as ex:
            raise ex
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()



    @classmethod
    def select_person_inside_dungeons(cls, person_id):
        """Results the person inside dungeon by person id And print all results"""
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Dungeon_Moves WHERE person_id= :p_id ORDER BY from_date"""
            cu = db.cursor()
            if not (cu.execute(temp_str, {"p_id": person_id})):
                raise ValueError("Warning: Person ID is not defined inside any dungeon")
            else:
                # Result Format
                print("#".center(8, ' '), end=' | ')
                print("ID".center(8, ' '), end=' | ')
                print("Dungeon ID".center(8, ' '), end=' | ')
                print("Person ID".center(8, ' '), end=' | ')
                print("From Date".center(14, ' '), end=' | \n')
                print("-" * 70)
                count = 0
                for row in cu.fetchall():
                    count += 1
                    print(f' {str(count).zfill(3)} '.center(7, ' '),
                          f' {row[0]} '.center(13, ' '),
                          f' {row[1]} '.center(10, ' '),
                          f' {row[2]} '.center(13, ' '),
                          f' {row[3]} '.center(14, ' '))
        except c_DB.sq.ProgrammingError as ex:
            raise ex
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()


    @classmethod
    def reset_json_by_database(cls):
        """
        Connect DB and select all Dungeon Moves
        loading json file and append values to new json file
        finally clear json file and add all values with DB
        Warning: This method will delete all old values in json files then add Dungeon Moves with DB
        """
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Dungeon_Moves"""
            data = []
            for row in db.cursor().execute(temp_str).fetchall():
                data.append(
                    {"Id": row[0], "dungeon_id": row[1], "person_id": row[2],
                     "from_date": str(row[3])})

            c_DB.write_json(data, Dungeon_Moves.__json_file)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.commit()
                db.close()

    @classmethod
    def print_all_data_by_json(cls):
        """Print Dungeon Moves data in json file only"""
        with open(Dungeon_Moves.__json_file, "r") as jf:
            data = json.load(jf)
            # Result Format
            print("#".center(8, ' '), end=' | ')
            print("ID".center(8, ' '), end=' | ')
            print("Dungeon ID".center(8, ' '), end=' | ')
            print("Person ID".center(8, ' '), end=' | ')
            print("From Date".center(14, ' '), end=' | \n')
            print("-" * 70)
            count = 0
            for row in data:
                count += 1
                print(f' {str(count).zfill(3)} '.center(7, ' '),
                      f' {row["Id"]} '.center(13, ' '),
                      f' {row["dungeon_id"]} '.center(10, ' '),
                      f' {row["person_id"]} '.center(13, ' '),
                      f' {row["from_date"]} '.center(14, ' '))




    """Start Getter and Setter Properties."""

    @property
    def dungeon_id(self):
        return self.__dungeon_id

    @dungeon_id.setter
    def dungeon_id(self, di):
        if di <= 0:
            raise ValueError("Error: Dungeon ID must be greater than Zero")
        else:
            db = None
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT Id FROM Dungeon WHERE Id=:id"""
                cu = db.cursor()
                if cu.execute(temp_str, {"id": di}).fetchone():
                    self.__dungeon_id = di
                else:
                    raise ValueError("Error: Dungeon ID is not defined")
            except c_DB.sq.ProgrammingError as ex:
                raise ex
            except ValueError as ex:
                raise ex
            finally:
                if db:
                    db.close()

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, pi):
        if pi <= 0:
            raise ValueError("Error: Person ID must be greater than Zero")
        else:
            db = None
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT Id FROM Person WHERE Id=:id"""
                cu = db.cursor()
                if cu.execute(temp_str, {"id": pi}).fetchone():
                    self.__person_id = pi
                else:
                    raise ValueError("Error: Person ID is not defined")
            except c_DB.sq.ProgrammingError as ex:
                raise ex
            except ValueError as ex:
                raise ex
            finally:
                if db:
                    db.close()

    @property
    def from_date(self):
        return self.__from_date

    @from_date.setter
    def from_date(self, fd):
        try:
            temp_date = c_DB.d(fd.year, fd.month, fd.day)
            date_now = c_DB.d.today()
            if temp_date > date_now:
                raise ValueError(
                    f'Error: From Date must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
            else:
                if temp_date < c_DB.d(1000, 1, 1):
                    raise ValueError("Error: From Date must be greater than 1000:01:01")
                else:
                    self.__from_date = fd
        except Exception as ex:
            raise Exception(ex)

    """End Getter and Setter Properties."""
