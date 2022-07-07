import json

import Connect_DB as c_DB
from App.Abstract_JSON import Abstract_JSON


class Visits(Abstract_JSON):
    """
    have class Visits method and properties ID, Date Visited, Person ID, Visitor Name.......
    and Get, Set All Properties
    """

    __json_file = "../JSON/Visits.js ' %}on"

    def __init__(self, date_visited: c_DB.d, person_id: int, visitor_name: str, mountIn_minutes):
        self.date_visited = date_visited
        self.person_id = person_id
        self.visitor_name = visitor_name.strip()
        self.mount_in_minutes = mountIn_minutes

    @classmethod
    def __str__(cls):
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Visits"""
            # result Format
            count = 0
            print("#".center(7, ' '), end=' | ')
            print("ID".center(7, ' '), end=' | ')
            print("Date Visited".center(14, ' '), end=' | ')
            print("Person ID".center(5, ' '), end=' | ')
            print("Visitor Name".center(50, ' '), end=' | ')
            print("Mount in Minutes".center(7, ' '), end=' | \n')
            print("-" * 130)
            for row in db.cursor().execute(temp_str).fetchall():
                count += 1
                print(f' {count} '.center(7, ' '),
                      f' {row[0]} '.center(12, ' '),
                      f' {row[1]} '.center(10, ' '),
                      f' {row[2]} '.center(16, ' '),
                      f' {row[3]} '.center(45, ' '),
                      f' {row[4]} '.center(25, ' '))
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def add_visited(cls, date_visited: c_DB.d, person_id: int, visitor_name: str, mountIn_minutes):
        """Add visitor in DB and check values"""
        db = None
        try:
            v = Visits(date_visited, person_id, visitor_name, mountIn_minutes)
            db = c_DB.connect_DB()
            cu = db.cursor()

            temp_str = """INSERT INTO Visits('date_visited', 'person_id', 'visitor_name', 'mount_in_minutes')
                      VALUES (?, ?, ?, ?)"""
            temp_sql_select = """SELECT Id FROM Visits ORDER BY Id DESC LIMIT 1;"""

            temp_val = (v.date_visited, v.person_id, v.visitor_name, v.mount_in_minutes)
            cu.execute(temp_str, temp_val)
            db.commit()

            cu.execute(temp_sql_select)
            visit_id = cu.fetchone()

            # Convert Visits id to Integer
            visit_id = int(visit_id[0])

            # Open Convicts.js ' %}on file and add convicts
            with open(Visits.__json_file) as jf:
                data = json.load(jf)
            temp = data
            temp.append(
                {"Id": visit_id, "date_visited": str(v.date_visited), "person_id": v.person_id,
                 "visitor_name": v.visitor_name,
                 "mount_in_minutes": str(v.mount_in_minutes)})

            #   write json file and added change
            c_DB.write_json(data, Visits.__json_file)

            print("Added Visits in json file and Database successfully")

        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def delete_visitor_by_id(cls, *visits_ids):
        """
        delete Visits from database by id
        and delete Visits in Visits.js ' %}on file by id
        """

        db = None
        try:
            db = c_DB.connect_DB()
            cu = db.cursor()

            temp_sql_select = """SELECT Id from Visits WHERE Id = :id;"""
            temp_sql_delete = """DELETE FROM Visits WHERE Id = :id;"""

            for visit_id in visits_ids:

                #   select Visits by id in order to check  Visits id
                cu.execute(temp_sql_select, {"id": visit_id})
                if not cu.fetchone():
                    raise ValueError(f"Error: Visits ID {visit_id} is not found in your data, please try again!")

                # delete the Visits by id
                cu.execute(temp_sql_delete, {"id": visit_id})
                db.commit()

                # Delete Visits in Visits.js ' %}on file, by Visits ID
                new_visits_data = []
                with open(Visits.__json_file, "r") as jf:
                    data = json.load(jf)

                # if id in json file keep change
                # else append Visits json in new_visits_data
                # finally update Visits.js ' %}on file by new_visits_data
                for row in data:
                    if row["Id"] == visit_id:
                        pass
                    else:
                        new_visits_data.append(row)
                c_DB.write_json(new_visits_data, Visits.__json_file)

            print("Delete Visit's in json file and Database successfully")




        except ValueError as ex:
            raise ex
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    @classmethod
    def select_visitor_by_datetime(cls, first_date, last_date, first_time=c_DB.t(00, 00), last_time=c_DB.t(23, 59)):
        """Results all values if date and time inside range"""
        db = None
        try:
            db = c_DB.connect_DB()
            if first_date > last_date:
                #   convert first_date and last_date
                first_date, last_date = last_date, first_date

            if first_time > last_time:
                #   convert first_time and last_time
                first_time, last_time = last_time, first_time

            temp_str = """SELECT * FROM Visits WHERE (date_visited BETWEEN :fd AND :ld)
                                                    AND (mount_in_minutes BETWEEN :ft AND :lt) ORDER BY date_visited"""
            temp_val = (
                {"fd": first_date, "ld": last_date, "ft": first_time.strftime("%H:%M"),
                 "lt": last_time.strftime("%H:%M")})
            # result Format
            count = 0
            print("#".center(7, ' '), end=' | ')
            print("ID".center(7, ' '), end=' | ')
            print("Date Visited".center(14, ' '), end=' | ')
            print("Person ID".center(5, ' '), end=' | ')
            print("Visitor Name".center(50, ' '), end=' | ')
            print("Mount in Minutes".center(7, ' '), end=' | \n')
            print("-" * 130)
            for row in db.cursor().execute(temp_str, temp_val).fetchall():
                count += 1
                print(f' {count} '.center(7, ' '),
                      f' {row[0]} '.center(12, ' '),
                      f' {row[1]} '.center(10, ' '),
                      f' {row[2]} '.center(16, ' '),
                      f' {row[3]} '.center(45, ' '),
                      f' {row[4]} '.center(20, ' '))
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def reset_json_by_database(cls):
        """
        Connect DB and select all Visits
        loading json file and append values to new json file
        finally clear json file and add all values with DB
        Warning: This method will delete all old values in json files then add Visits with DB
        """
        db = None
        try:
            db = c_DB.connect_DB()
            temp_sql_select = """SELECT * FROM Visits"""
            data = []
            for row in db.cursor().execute(temp_sql_select).fetchall():
                data.append(
                    {"Id": row[0], "date_visited": str(row[1]), "person_id": row[2],
                     "visitor_name": row[3], "mount_in_minutes": str(row[4])})
            c_DB.write_json(data, Visits.__json_file)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.commit()
                db.close()

    @classmethod
    def print_all_data_by_json(cls):
        """Print Visits data in console by json file only"""
        with open(Visits.__json_file, "r") as jf:
            data = json.load(jf)

        # result Format
        count = 0
        print("#".center(7, ' '), end=' | ')
        print("ID".center(7, ' '), end=' | ')
        print("Date Visited".center(14, ' '), end=' | ')
        print("Person ID".center(5, ' '), end=' | ')
        print("Visitor Name".center(50, ' '), end=' | ')
        print("Mount in Minutes".center(7, ' '), end=' | \n')
        print("-" * 130)
        for row in data:
            count += 1
            print(f' {count} '.center(7, ' '),
                  f' {row["Id"]} '.center(12, ' '),
                  f' {row["date_visited"]} '.center(10, ' '),
                  f' {row["person_id"]} '.center(16, ' '),
                  f' {row["visitor_name"]} '.center(45, ' '),
                  f' {row["mount_in_minutes"]} '.center(25, ' '))

    """Start Getter and Setter Properties."""

    @property
    def date_visited(self):
        return self.__date_visited

    @date_visited.setter
    def date_visited(self, dv):
        try:
            temp_date = c_DB.d(dv.year, dv.month, dv.day)
            date_now = c_DB.d.today()
            if temp_date > date_now:
                raise ValueError(
                    f'Error: From Date Visited must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
            else:
                if temp_date < c_DB.d(1000, 1, 1):
                    raise ValueError("Error: Date Visited must be greater than 1000:01:01")
                else:
                    self.__date_visited = dv
        except Exception as ex:
            raise Exception(ex)

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, pi: int):
        if pi <= 0:
            raise ValueError("Error: Person ID must be greater than Zero")
        else:
            db = None
            try:
                db = c_DB.connect_DB()
                temp_sql_select = """SELECT Id FROM Person WHERE Id=:id"""
                cu = db.cursor()
                if cu.execute(temp_sql_select, {"id": pi}).fetchone():
                    self.__person_id = pi
                else:
                    raise ValueError("Error: Person ID is not defined")
            except c_DB.sq.ProgrammingError as ex:
                raise c_DB.sq.ProgrammingError(ex)
            except ValueError as ex:
                raise ValueError(ex)
            finally:
                if db:
                    db.close()

    @property
    def visitor_name(self):
        return self.__visitor_name

    @visitor_name.setter
    def visitor_name(self, vn):
        if len(vn) <= 1:
            raise ValueError("Error: Visitor name must be greater than one Character")
        else:
            self.__visitor_name = vn

    @property
    def mount_in_minutes(self):
        return self.__mount_in_minutes.strftime("%H:%M")

    @mount_in_minutes.setter
    def mount_in_minutes(self, mm):
        try:
            self.__mount_in_minutes = mm
        except Exception as ex:
            raise Exception(ex.__class__)

    """End Getter and Setter Properties."""
