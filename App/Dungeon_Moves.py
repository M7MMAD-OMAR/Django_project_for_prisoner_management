import Connect_DB as c_DB


class Dungeon_Moves:
    """
    have class Dungeon_Moves method and properties ID, Dungeon ID, Person ID, From Date.......
    and Get, Set All Properties
    """

    def __init__(self, dungeon_id: int, person_id: int, from_date: str):
        self.set_dungeon_id(dungeon_id)
        self.set_person_id(person_id)
        self.set_from_date(from_date.strip())

    def __str__(self):
        print(f'Dungeon ID: {self.__dungeon_id}\n'
              f'Person ID: {self.__person_id}\n'
              f'From Date: {self.__from_date}')

    def get_dungeon_id(self):
        return self.__dungeon_id

    def set_dungeon_id(self, di):
        if di > 0:
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
                print(ex)
            except ValueError as ex:
                print(ex)
            finally:
                if db:
                    db.close()
                    print("Closed DataBase from Dungeon Moves")
        else:
            raise ValueError("Error: Dungeon ID must be greater than Zero")

    def get_person_id(self):
        return self.__person_id

    def set_person_id(self, pi):

        if pi > 0:
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
                print(ex)
            except ValueError as ex:
                print(ex)
            finally:
                if db:
                    db.close()
                    print("Closed DataBase from Dungeon Moves [Person]")
        else:
            raise ValueError("Error: Person ID must be greater than Zero")



    def get_from_date(self):
        return self.__from_date

    def set_from_date(self, fd):
        try:
            if len(fd) <= 0:
                raise ValueError("Error: No value entered for the date")
            else:
                temp_split = fd.split(', ')
                temp_date = c_DB.dt.strptime(temp_split[0], "%d-%m-%Y")
                temp_time = c_DB.dt.strptime(temp_split[1], "%H:%M")
                date_now = c_DB.dt.now()
                if temp_date > c_DB.dt.now():
                    raise ValueError(
                        f'Error: From Date must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
                else:
                    self.__from_date = fd
        except ValueError:
            print("Error: Value From Date is False ")



