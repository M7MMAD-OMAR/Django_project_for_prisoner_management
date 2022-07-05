import json

import Connect_DB as c_DB


class Convicts:
    """
    have class Convicts method and properties From date, To date, Person ID.......
    and Get, Set All Properties
    """

    __json_file = "../JSON/Convicts.json"

    def __init__(self, from_date, to_date: str, person_id: int, offense_id: int):
        self.from_date = from_date
        self.to_date = to_date
        self.person_id = person_id
        self.offense_id = offense_id

    @classmethod
    def __str__(cls):
        db = None
        try:
            db = c_DB.connect_DB()
            temp_sql_select = """SELECT * FROM Convicts"""
            # result Format
            count = 0
            print("#".center(8, ' '), end=' | ')
            print("ID".center(8, ' '), end=' | ')
            print("From Date".center(15, ' '), end=' | ')
            print("To Date".center(15, ' '), end=' | ')
            print("Person ID".center(8, ' '), end=' | ')
            print("Offense ID".center(8, ' '), end=' | \n')
            print("-" * 100)
            for row in db.cursor().execute(temp_sql_select).fetchall():
                count += 1
                print(f' {str(count).zfill(3)} '.center(7, ' '),
                      f' {row[0]} '.center(14, ' '),
                      f' {row[1]} '.center(12, ' '),
                      f' {row[2]} '.center(21, ' '),
                      f' {row[3]} '.center(10, ' '),
                      f' {row[4]} '.center(12, ' '))
            # count = 0
            # for row in db.cursor().execute(temp_sql_select).fetchall():
            #     count+=1
            #     print(str(count), "".center(50, '-'))
            #     print(f'ID:           {row[0]}\n'
            #           f'From Date:    {row[1]}\n'
            #           f'To Date:      {row[2]}\n'
            #           f'Person ID:    {row[3]}\n'
            #           f'Offense ID:   {row[4]}')
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def add_convicts(cls, from_date, to_date, person_id, offense_id):
        """Add convicts to DB and Convicts.json file and check all values"""
        db = None
        try:
            db = c_DB.connect_DB()
            c = Convicts(from_date, to_date, person_id, offense_id)
            db = c_DB.connect_DB()
            temp_sql_insert = """INSERT INTO Convicts('from_date', 'to_date', 'person_id', 'offense_id') VALUES(?, ?, ?, ?)"""
            temp_sql_select = """SELECT Id FROM Convicts ORDER BY Id DESC LIMIT 1;"""
            temp_val = (c.from_date, c.to_date, c.person_id, c.offense_id)
            cu = db.cursor()
            cu.execute(temp_sql_insert, temp_val)
            db.commit()

            cu.execute(temp_sql_select)
            convicts_id = cu.fetchone()

            # Convert convicts id to Integer
            convicts_id = int(convicts_id[0])

            # Open Convicts.json file and add convicts
            with open(Convicts.__json_file) as jf:
                data = json.load(jf)
            temp = data
            temp.append(
                {"Id": convicts_id, "from_date": str(c.from_date), "to_date": str(c.to_date), "person_id": c.person_id,
                 "offense_id": c.offense_id})

            #   write json file and added change
            c_DB.write_json(data, Convicts.__json_file)

            print("Added Convicts in json file and Database successfully")

        except c_DB.sq.ProgrammingError as ex:
            raise ex
        except NameError as ex:
            raise ex
        except ValueError as ex:
            raise ex
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    @classmethod
    def select_persons_by_offense_id(cls, offense_id):
        """select all persons by offense id and print all results"""
        db = None
        try:
            db = c_DB.connect_DB()
            temp_sql_select_offense_id = """SELECT Offense.name FROM Offense WHERE Id = :o_id"""
            temp_sql_select = """SELECT * FROM Person WHERE Id in (SELECT DISTINCT person_id FROM Convicts WHERE offense_id=:o_id)"""
            cu = db.cursor()

            #   if offense id is not valued raise error else print persons by offense name
            if not (cu.execute(temp_sql_select, {"o_id": offense_id})):
                raise ValueError("Warning: Don't Results")
            else:
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
                for row in cu.fetchall():
                    count += 1
                    print(f' {str(count).zfill(3)} '.center(7, ' '),
                          f' {row[0]} '.center(14, ' '),
                          f' {row[1]} '.center(12, ' '),
                          f' {row[2]} '.center(23, ' '),
                          f' {row[3]} '.center(20, ' '),
                          f' {row[4]} '.center(20, ' '),
                          f' {row[5]} '.center(20, ' '),
                          f' {row[6]} '.center(28, ' '))

                # Execute temp_sql_select_offense_id in order to print offense name
                cu.execute(temp_sql_select_offense_id, {"o_id": offense_id})
                offense_name = cu.fetchone()
                print(f'\nOffense Name: {offense_name[0]}')

        except c_DB.sq.OperationalError as ex:
            raise c_DB.sq.OperationalError(ex)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def select_persons_between_date(cls, first_date, last_date):
        """Results person if person date between the two dates"""
        db = None
        try:
            db = c_DB.connect_DB()
            if first_date > last_date:
                first_date, last_date = last_date, first_date
            temp_sql_select = """SELECT * FROM Convicts WHERE from_date BETWEEN (?) and (?) ORDER BY from_date"""
            temp_val = (first_date, last_date)
            # result Format
            count = 0
            print("#".center(8, ' '), end=' | ')
            print("ID".center(8, ' '), end=' | ')
            print("From Date".center(15, ' '), end=' | ')
            print("To Date".center(15, ' '), end=' | ')
            print("Person ID".center(8, ' '), end=' | ')
            print("Offense ID".center(8, ' '), end=' | \n')
            print("-" * 100)
            for row in db.cursor().execute(temp_sql_select, temp_val).fetchall():
                count += 1
                print(f' {str(count).zfill(3)} '.center(7, ' '),
                      f' {row[0]} '.center(14, ' '),
                      f' {row[1]} '.center(12, ' '),
                      f' {row[2]} '.center(21, ' '),
                      f' {row[3]} '.center(10, ' '),
                      f' {row[4]} '.center(12, ' '))
        except c_DB.sq.OperationalError as ex:
            raise c_DB.sq.OperationalError(ex)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def delete_convicts_by_id(cls, *convicts_ids):
        """
        delete convicts from database by id
        and delete convicts in Convicts.json file by id
        """

        db = None
        try:
            db = c_DB.connect_DB()
            cu = db.cursor()

            temp_sql_select = """SELECT Id from Convicts WHERE Id = :id;"""
            temp_sql_delete = """DELETE FROM Convicts WHERE Id = :id;"""

            for convict_id in convicts_ids:

                #   select Convicts by id in order to check  Convicts id
                cu.execute(temp_sql_select, {"id": convict_id})
                if not cu.fetchone():
                    raise ValueError(f"Error: Convicts ID {convict_id} is not found in your data, please try again!")

                # delete the Convicts by id
                cu.execute(temp_sql_delete, {"id": convict_id})
                db.commit()

                # Delete Convicts in Convicts.json file, by Convicts ID
                new_convicts_data = []
                with open(Convicts.__json_file, "r") as jf:
                    data = json.load(jf)

                # if id in json file keep change
                # else append Convicts json in new_convicts_data
                # finally update Convicts.json file by new_convicts_data
                for row in data:
                    if row["Id"] == convict_id:
                        pass
                    else:
                        new_convicts_data.append(row)
                c_DB.write_json(new_convicts_data, Convicts.__json_file)

            print("Delete Convict's in json file and Database successfully")




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
        Connect DB and select all Convicts
        loading json file and append values to new json file
        finally clear json file and add all values with DB
        Warning: This method will delete all old values in json files then add Convicts with DB
        """
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Convicts"""
            data = []
            for row in db.cursor().execute(temp_str).fetchall():
                data.append(
                    {"Id": row[0], "from_date": str(row[1]), "to_date": str(row[2]),
                     "person_id": row[3],
                     "offense_id": row[4]})
            c_DB.write_json(data, Convicts.__json_file)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.commit()
                db.close()

    @classmethod
    def print_all_data_by_json(cls):
        """Print Convicts data in json file only"""
        with open(Convicts.__json_file, "r") as jf:
            data = json.load(jf)

        # result Format
        count = 0
        print("#".center(8, ' '), end=' | ')
        print("ID".center(8, ' '), end=' | ')
        print("From Date".center(15, ' '), end=' | ')
        print("To Date".center(15, ' '), end=' | ')
        print("Person ID".center(8, ' '), end=' | ')
        print("Offense ID".center(8, ' '), end=' | \n')
        print("-" * 100)
        for row in data:
            count += 1
            print(f' {str(count).zfill(3)} '.center(7, ' '),
                  f' {row["Id"]} '.center(14, ' '),
                  f' {row["from_date"]} '.center(12, ' '),
                  f' {row["to_date"]} '.center(21, ' '),
                  f' {row["person_id"]} '.center(10, ' '),
                  f' {row["offense_id"]} '.center(12, ' '))

    """Start Getter and Setter Properties."""

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

    @property
    def to_date(self):
        return self.__to_date

    @to_date.setter
    def to_date(self, td):
        try:
            temp_date = c_DB.d(td.year, td.month, td.day)
            date_now = c_DB.d.today()
            if temp_date < c_DB.d(1000, 1, 1):
                raise ValueError("Error: To Date must be greater than 1000:01:01")
            else:
                if self.from_date > temp_date:
                    raise ValueError("Error: 'From Date' must be smaller than 'To Date'")
                self.__to_date = td
        except Exception as ex:
            raise Exception(ex)

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, pi):
        db = None
        if pi <= 0:
            raise ValueError("Error: Person ID must be greater than Zero")
        else:
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
    def offense_id(self):
        return self.__offense_id

    @offense_id.setter
    def offense_id(self, oi):
        db = None
        if oi <= 0:
            raise ValueError("Error: Offense ID must be greater than Zero")
        else:
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT Id FROM Offense WHERE Id=:id"""
                cu = db.cursor()
                if cu.execute(temp_str, {"id": oi}).fetchone():
                    self.__offense_id = oi
                else:
                    raise ValueError("Error: Offense ID is not defined")
            except c_DB.sq.ProgrammingError as ex:
                raise ex
            except ValueError as ex:
                raise ex
            finally:
                if db:
                    db.close()

    """End Getter and Setter Properties."""
