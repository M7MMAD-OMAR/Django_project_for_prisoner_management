import Connect_DB as c_DB


class Convicts:
    """
    have class Convicts method and properties From date, To date, Person ID.......
    and Get, Set All Properties
    """
    cls = None

    def __init__(self, from_date: str, to_date: str, person_id: int, offense_id: int):
        cls = self
        self.from_date = from_date
        self.to_date = to_date
        self.person_id = person_id
        self.offense_id = offense_id

    def __str__(self):
        print(f'From Date: {self.from_date}\n'
              f'To Date: {self.to_date}\n'
              f'Person ID: {self.person_id}\n'
              f'Offense ID: {self.offense_id}')

    def add_convicts(self, from_date, to_date, person_id, offense_id):
        global db
        try:
            db = c_DB.connect_DB()
            Convicts(from_date, to_date, person_id, offense_id)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Convicts('from_date', 'to_date', 'person_id', 'offense_id') VALUES(?, ?, ?, ?)"""
            temp_val = (from_date, to_date, person_id, offense_id)
            db.cursor().execute(temp_str, temp_val)
            db.commit()
            print("successfully inserted")
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

    @property
    def from_date(self):
        return self.__from_date

    @from_date.setter
    def from_date(self, fd: str):
        if fd.__contains__(' '):
            raise ValueError("Error: From Date must be don't contain space")
        else:
            if len(fd) > 10:
                raise ValueError("Error: From Date is correct")
            else:
                try:
                    temp = c_DB.dt.strptime(fd, "%d-%m-%Y")
                    date_now = c_DB.dt.now()
                    if temp > date_now:
                        raise TypeError(
                            f'Error: From Date must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
                    else:
                        self.__from_date = fd

                except TypeError as ex:
                    raise ex

    @property
    def to_date(self):
        return self.__to_date

    @to_date.setter
    def to_date(self, td):
        try:
            if td.__contains__(' '):
                raise ValueError("Error: To Date must be don't contain space")
            else:
                if len(td) > 10:
                    raise ValueError("Error: To Date is correct")
                else:
                    temp_td = c_DB.dt.strptime(td, "%d-%m-%Y")
                    temp_fd = c_DB.dt.strptime(self.from_date, "%d-%m-%Y")
                    if temp_fd > temp_td:
                        raise TypeError("Error: From Date don't must be greater than To Date ")
                    else:
                        self.__to_date = td
        except TypeError as ex:
            raise ex

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, pi):
        global db
        if pi <= 0:
            raise ValueError("Error: Person ID must be greater than Zero")
        else:
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT Id FROM Person WHERE Id=:id"""
                cu = db.cursor()
                if cu.execute(temp_str, {"id": pi}).fetchone():
                    self.__person_id = pi
                    print("Person ID is Available")
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
        global db
        if oi <= 0:
            raise ValueError("Error: Offense ID must be greater than Zero")
        else:
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT Id FROM Offense WHERE Id=:id"""
                cu = db.cursor()
                if cu.execute(temp_str, {"id": oi}).fetchone():
                    self.__offense_id = oi
                    print("Offense ID is Available")
                else:
                    raise ValueError("Error: Offense ID is not defined")
            except c_DB.sq.ProgrammingError as ex:
                raise ex
            except ValueError as ex:
                raise ex
            finally:
                if db:
                    db.close()
