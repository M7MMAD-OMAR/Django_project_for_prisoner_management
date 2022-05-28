class Dungeon_Moves:
    """
    have class Dungeon_Moves method and properties ID, Dungeon ID, Person ID, From Date.......
    and Get, Set All Properties
    """
    def __init__(self, id, dungeon_id, person_id, from_date):
        if (id and dungeon_id and person_id > 0) and from_date is not None:
            self.__Id = id
            self.__dungeon_id = dungeon_id
            self.__person_id = person_id
            self.__from_date = from_date
        else:
            raise Exception("Error from Dungeon Moves constructor")

    def __str__(self):
        print(f'ID: {self.__Id}\n'
              f'Dungeon ID: {self.__dungeon_id}\n'
              f'Person ID: {self.__person_id}\n'
              f'From Date: {self.__from_date}')

    def get_id(self):
        return self.__Id

    def set_id(self, id):
        if id <= 0:
            raise ValueError("Error from Dungeon Moves ID")
        else:
            self.__Id = id

    def get_dungeon_id(self):
        return self.__dungeon_id

    def set_dungeon_id(self, di):
        if di <= 0:
            raise ValueError("Error from Dungeon Moves Dungeon ID")
        else:
            self.__dungeon_id = di

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
        if fd is None:
            raise ValueError("Error from Dungeon Moves From Date")
        else:
            self.__from_date = fd
