import Connect_DB as c_DB


class Dungeon:
    """
    have class Dungeon method and properties ID, Name, Size.......
    and Get, Set All Properties
    """

    def __init__(self, name, size):
        self.set_name(name.strip())
        self.set_size(size)
        # if size > 0 and len(name) > 1:
        #     # self.__Id = id
        #     # self.__name = name
        #     # self.__size = size
        #
        # else:
        #     raise Exception("Error from Dungeon constructor")

    def __str__(self):
        print(f'Name: {self.__name}\n'
              f'Size: {self.__size}\n')

    def add_dungeon(self):
        global db
        try:
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Dungeon('name', 'size') VALUES(?, ?)"""
            temp_val = (self.__name, self.__size)
            cu = db.cursor()
            cu.execute(temp_str, temp_val)
            db.commit()
            print("Sent values in add dungeon Successfully")
        except Exception as ex:
            print(ex)
        finally:
            if db:
                db.close()
                print("close DataBase from dungeon")

    # def get_id(self):
    #     return self.__Id
    #
    # def set_id(self, id):
    #     if id <= 0:
    #         raise ValueError("Error from Dungeon id")
    #     else:
    #         self.__Id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if c_DB.check(name, "Error from Dungeon name"):
            self.__name = name
        # if len(name) <= 1:
        #     raise ValueError("Error from Dungeon name")
        # else:
        #     self.__name = name

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if size <= 0:
            raise ValueError("Error from Dungeon size")
        else:
            self.__size = size
