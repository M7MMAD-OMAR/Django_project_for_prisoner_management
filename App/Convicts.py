import Connect_DB as c_DB


class Convicts:
    """
    have class Convicts method and properties From date, To date, Person ID.......
    and Get, Set All Properties
    """
    cls = None

    def __init__(self, from_date, to_date: str, person_id: int, offense_id: int):
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

    @classmethod
    def add_convicts(cls, from_date, to_date, person_id, offense_id):
        global db
        try:
            db = c_DB.connect_DB()
            c = Convicts(from_date, to_date, person_id, offense_id)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Convicts('from_date', 'to_date', 'person_id', 'offense_id') VALUES(?, ?, ?, ?)"""
            temp_val = (c.from_date, c.to_date, c.person_id, c.offense_id)
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

    @classmethod
    def select_persons_between_date(cls, first_date, second_date):
        global db
        try:
            db = c_DB.connect_DB()
            # temp_str = """SELECT * FROM Convicts WHERE from_date >= (?) and from_date <= (?)"""
            temp_str = """SELECT * FROM Convicts WHERE from_date BETWEEN (?) and (?)"""
            temp_val = (first_date, second_date)
            count = 0
            for row in db.cursor().execute(temp_str, temp_val).fetchall():
                count+=1
                print(str(count), "".center(50, '-'))
                print(f'ID:          {row[0]}\n'
                      f'From Date:   {row[1]}\n'
                      f'To Date:     {row[2]}\n'
                      f'Person ID:   {row[3]}\n'
                      f'Offense ID:  {row[4]}')
        except c_DB.sq.OperationalError as ex:
            raise c_DB.sq.OperationalError(ex)
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

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
    """End Getter and Setter Properties."""