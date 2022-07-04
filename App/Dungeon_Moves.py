import Connect_DB as c_DB


class Dungeon_Moves:
    """
    have class Dungeon_Moves method and properties Dungeon ID, Person ID, From Date.......
    and Get, Set All Properties
    """

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
            count = 0
            for row in db.cursor().execute(temp_str).fetchall():
                count += 1
                print(str(count), "".center(50, '-'))
                print(f'ID:         {row[0]}\n'
                      f'Dungeon ID: {row[2]}\n'
                      f'Person ID:  {row[1]}\n'
                      f'From Date:  {row[3]}')
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def add_dungeon_moves(cls, dungeon_id: int, person_id: int, from_date):
        db = None
        try:
            dm = Dungeon_Moves(dungeon_id, person_id, from_date)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Dungeon_Moves('dungeon_id', 'person_id', 'from_date') VALUES(?, ?, ?)"""
            temp_val = (dm.dungeon_id, dm.person_id, dm.from_date)
            db.cursor().execute(temp_str, temp_val)
            db.commit()
        except c_DB.sq.ProgrammingError as ex:
            raise ex
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def select_person_inside_dungeons(cls, person_id):
        """Results the person inside dungeon by person id And print all results"""
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Dungeon_Moves WHERE person_id=:pID"""
            cu = db.cursor()
            if not (cu.execute(temp_str, {"pID": person_id})):
                raise ValueError("Warning: Person ID is not defined inside any dungeon")
            else:
                # Format result
                print("#".center(8, ' '), end=' | ')
                print("ID".center(8, ' '), end=' | ')
                print("Dungeon ID".center(8, ' '), end=' | ')
                print("Person ID".center(8, ' '), end=' | ')
                print("From Date".center(14, ' '), end=' | \n')
                print("-" * 70)
                count = 0
                for row in cu.fetchall():
                    count += 1
                    print(f' {count} '.center(7, ' '),
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
                    print("Dungeon ID is Available")
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
