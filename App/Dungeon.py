import Connect_DB as c_DB


class Dungeon:
    """
    have class Dungeon method and properties ID, Name, Size.......
    and Get, Set All Properties
    """

    def __init__(self, name: str, size: int):
        self.set_name(name.strip())
        self.set_size(size)

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
            temp_val = (d.get_name(), d.get_size())
            cu = db.cursor()
            cu.execute(temp_str, temp_val)
            db.commit()
            print("Sent values in add dungeon Successfully")
        except AttributeError as ex:
            raise ex
        finally:
            if db:
                db.close()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        """change name and check name is in DB then not change name
        or name is not created in DB then change name"""
        if len(name) <= 1:
            raise ValueError("Error: length name is a few char")
        else:
            global db
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT name FROM Dungeon WHERE name=:name"""
                cu = db.cursor()
                cu.execute(temp_str, {"name": name})
                if not (cu.fetchone()):
                    self.__name = name
                    print("Name is Available")
                else:
                    raise c_DB.sq.ProgrammingError("Error: Dungeon name is already defined, Please change value name")
            except c_DB.sq.ProgrammingError as ex:
                raise ex
            except ValueError as ex:
                raise ex
            except Exception as ex:
                raise ex
            finally:
                if db:
                    db.close()

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if size <= 0:
            raise ValueError("Error: Size must be greater then Zero")
        else:
            self.__size = size
