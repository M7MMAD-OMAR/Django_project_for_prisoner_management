class Offense:
    def __init__(self, name):
        if len(name) > 1:
            # self.__Id = id
            self.__name = name
        else:
            raise Exception("Error from Offense Constructor")

    def __str__(self):
        print(f'Name: {self.__name}')

    # def get_id(self):
    #     return self.__Id
    #
    # def set_id(self, id):
    #     if id <= 0:
    #         raise ValueError("Error from Offense id")
    #     else:
    #         self.__Id = id

    def get_name(self):
        return self.__name

    def set_name(self, n):
        if len(n) <= 1:
            raise ValueError("Error from Offense name")
        else:
            self.__name = n
