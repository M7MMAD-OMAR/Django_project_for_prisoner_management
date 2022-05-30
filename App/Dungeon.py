import Connect_DB as c_DB


class Dungeon:
    """
    have class Dungeon method and properties ID, Name, Size.......
    and Get, Set All Properties
    """

    def __init__(self, name: str, size: int):
        self.set_name(name.strip())
        self.set_size(size)

        # Add dungeon
        # if len(name) > 1:


        # if size > 0 and len(name) > 1:
        #     # self.__Id = id
        #     # self.__name = name
        #     # self.__size = size
        #
        # else:
        #     raise Exception("Error from Dungeon constructor")

    def __str__(self):
        print(f'Name: {self.get_name()}\n'
              f'Size: {self.get_size()}\n')

    def add_dungeon(self, name: str, size: int):
        """Add dungeon in DB"""
        global db
        try:
            d = Dungeon(name, size)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Dungeon('name', 'size') VALUES(?, ?)"""
            temp_val = (self.get_name(), self.get_size())
            cu = db.cursor()
            cu.execute(temp_str, temp_val)
            db.commit()
            print("Sent values in add dungeon Successfully")
        except Exception as ex:
            print("Error: from add dungeon")
        finally:
            if db:
                db.close()
                print("close DataBase from add dungeon")

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
        """change name and check name is in DB then not change name
        or name is not created in DB then change name """
        global db
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT name FROM Dungeon WHERE name=:name"""
            cu = db.cursor()
            cu.execute(temp_str, {"name": name})
            if len(name) > 1:
                if not (cu.fetchone()):
                    self.__name = name
                else:
                    raise c_DB.sq.ProgrammingError("Error: Dungeon name is already defined, Please change value name")
            else:
                raise ValueError("Error: length name is a few char")
        except c_DB.sq.ProgrammingError as ex:
            print(ex)
        except ValueError as ex:
            print(ex)
        except Exception:
            print("Error: from Dungeon set name")
        finally:
            if db:
                db.close()
                print("close DataBase from dungeon Set name")
        # if c_DB.check(name, "Error from Dungeon name"):
        #     self.__name = name
        # if len(name) <= 1:
        #     raise ValueError("Error from Dungeon name")
        # else:
        #     self.__name = name

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if size <= 0:
            raise ValueError("Error: Size must be greater then Zero")
        else:
            self.__size = size
