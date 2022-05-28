class Dungeon:
    """
    have class Dungeon method and properties ID, Name, Size.......
    and Get, Set All Properties
    """
    def __init__(self, id, name, size):
        if (id and size > 0) and len(name) > 1:
            self.__Id = id
            self.__name = name
            self.__size = size
        else:
            raise Exception("Error from Dungeon constructor")

    def __str__(self):
        print(f'ID: {self.__Id}\n'
              f'Name: {self.__name}\n'
              f'Size: {self.__size}\n')

    def get_id(self):
        return self.__Id

    def set_id(self, id):
        if id <= 0:
            raise ValueError("Error from Dungeon id")
        else:
            self.__Id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) <= 1:
            raise ValueError("Error from Dungeon name")
        else:
            self.__name = name

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if size <= 0:
            raise ValueError("Error from Dungeon size")
        else:
            self.__size = size
