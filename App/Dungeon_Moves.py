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
        # if dungeon_id > 0 and person_id > 0 and len(from_date) > 0:
        #     # self.__Id = id
        #     self.__dungeon_id = dungeon_id
        #     self.__person_id = person_id
        #     self.__from_date = from_date
        # else:
        #     raise Exception("Error from Dungeon Moves constructor")

    def __str__(self):
        print(f'Dungeon ID: {self.__dungeon_id}\n'
              f'Person ID: {self.__person_id}\n'
              f'From Date: {self.__from_date}')

    # def get_id(self):
    #     return self.__Id
    #
    # def set_id(self, id):
    #     if id <= 0:
    #         raise ValueError("Error from Dungeon Moves ID")
    #     else:
    #         self.__Id = id

    def get_dungeon_id(self):
        return self.__dungeon_id

    def set_dungeon_id(self, di):
        global db
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT Id FROM Dungeon WHERE Id=?"""
            cu = db.cursor()
            cu.execute(temp_str, di)
            if cu.fetchone():
                self.__dungeon_id = di
            else:
                raise Exception("Dungeon ID is not defined")
        except Exception as ex:
            print(ex)
        finally:
            if db:
                db.close()
                print("Closed DataBase from Dungeon Moves")
        # if c_DB.check(di, "Error from Dungeon Moves Dungeon ID"):
        #     self.__dungeon_id = di
        # if di <= 0:
        #     raise ValueError("Error from Dungeon Moves Dungeon ID")
        # else:
        #     self.__dungeon_id = di

    def get_person_id(self):
        return self.__person_id

    def set_person_id(self, pi):
        if pi <= 0:
            raise ValueError("Error from Dungeon Moves Person ID")
        else:
            self.__person_id = pi

    def get_from_date(self):
        return self.__from_date

    def set_from_date(self, fd):
        if c_DB.check(fd, "Error from Dungeon Moves From Date"):
            self.__from_date = fd
        # if fd is None:
        #     raise ValueError("Error from Dungeon Moves From Date")
        # else:
        #     self.__from_date = fd
