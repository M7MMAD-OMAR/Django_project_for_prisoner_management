import Connect_DB as c_DB


class Dungeon_Moves:
    """
    have class Dungeon_Moves method and properties Dungeon ID, Person ID, From Date.......
    and Get, Set All Properties
    """

    cls = None

    def __init__(self, dungeon_id: int, person_id: int, from_date: str):
        cls = self
        self.dungeon_id = dungeon_id
        self.person_id = person_id
        self.from_date = from_date.strip()

    def __str__(self):
        print(f'Dungeon ID: {self.dungeon_id}\n'
              f'Person ID: {self.person_id}\n'
              f'From Date: {self.from_date}')

    def add_dungeon_moves(self, dungeon_id: int, person_id: int, from_date: str):
        global db
        try:
            Dungeon_Moves(dungeon_id, person_id, from_date)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Dungeon_Moves('dungeon_id', 'person_id', 'from_date') VALUES(?, ?, ?)"""
            temp_val = (dungeon_id, person_id, from_date)
            db.cursor().execute(temp_str, temp_val)
            db.commit()
        except c_DB.sq.ProgrammingError as ex:
            raise ex
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()



    @property
    def dungeon_id(self):
        return self.__dungeon_id

    @dungeon_id.setter
    def dungeon_id(self, di):
        if di <= 0:
            raise ValueError("Error: Dungeon ID must be greater than Zero")
        else:
            global db
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
            global db
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
        if len(fd) <= 0:
            raise ValueError("Error: No value entered for the date")
        else:
            try:
                temp_split = fd.split(', ')
                temp_date = c_DB.dt.strptime(temp_split[0], "%d-%m-%Y")
                c_DB.dt.strptime(temp_split[1], "%H:%M")
                date_now = c_DB.dt.now()
                if temp_date > c_DB.dt.now():
                    raise ValueError(
                        f'Error: From Date must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
                else:
                    self.__from_date = fd
            except ValueError:
                raise ValueError("Error: Value From Date is Correct")
