import Connect_DB as c_DB


class Convicts:
    """
    have class Convicts method and properties From date, To date, Person ID.......
    and Get, Set All Properties
    """

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
            temp_str = """SELECT * FROM Convicts"""
            count = 0
            for row in db.cursor().execute(temp_str).fetchall():
                count+=1
                print(str(count), "".center(50, '-'))
                print(f'ID:           {row[0]}\n'
                      f'From Date:    {row[1]}\n'
                      f'To Date:      {row[2]}\n'
                      f'Person ID:    {row[3]}\n'
                      f'Offense ID:   {row[4]}')
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()


    @classmethod
    def add_convicts(cls, from_date, to_date, person_id, offense_id):
        """Add convicts to DB and check all values"""
        db = None
        try:
            db = c_DB.connect_DB()
            c = Convicts(from_date, to_date, person_id, offense_id)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Convicts('from_date', 'to_date', 'person_id', 'offense_id') VALUES(?, ?, ?, ?)"""
            temp_val = (c.from_date, c.to_date, c.person_id, c.offense_id)
            db.cursor().execute(temp_str, temp_val)
            db.commit()
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
    def select_persons_by_offense(cls, offense_id):
        """selec all persons by offense id and print all results"""
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Person WHERE Id in 
                       (SELECT DISTINCT person_id FROM Convicts WHERE offense_id=:oID)"""
            cu = db.cursor()
            if not (cu.execute(temp_str, {"oID":offense_id})):
                raise ValueError("Warning: Don't Results")
            else:
                count = 0
                for row in cu.fetchall():
                    count += 1
                    print(str(count), "".center(50, '-'))
                    print(f'ID:         {row[0]}\n'
                          f'First Name: {row[1]}\n'
                          f'Father:     {row[2]}\n'
                          f'Last Name:  {row[3]}\n'
                          f'Gender:     {row[4]}\n'
                          f'Birth Year: {row[5]}\n'
                          f'Address:    {row[6]}')
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
            temp_str = """SELECT * FROM Convicts WHERE from_date BETWEEN (?) and (?)"""
            temp_val = (first_date, last_date)
            # Format result
            count = 0
            print("#".center(8, ' '), end=' | ')
            print("ID".center(8, ' '), end=' | ')
            print("From Date".center(15, ' '), end=' | ')
            print("To Date".center(15, ' '), end=' | ')
            print("Person ID".center(8, ' '), end=' | ')
            print("Offense ID".center(8, ' '), end=' | \n')
            print("-" * 100)
            for row in db.cursor().execute(temp_str, temp_val).fetchall():
                count += 1
                print(f' {count} '.center(7, ' '),
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
