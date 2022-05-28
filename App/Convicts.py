class Convicts:
    """
    have class Person method and properties ID, First Name, Father, Last Name.......
    and Get, Set All Properties
    """
    def __init__(self, id, from_date, to_date, person_id, offense_id):
        if (id and person_id and offense_id > 0) and (from_date and to_date is not None):
            self.__Id = id
            self.__from_date = from_date
            self.__to_date = to_date
            self.__person_id = person_id
            self.__offense_id = offense_id
        else:
            raise Exception("Error from Convicts constructor")

    def __str__(self):
        print(f'ID: {self.__Id}\n'
              f'From Date: {self.__from_date}\n'
              f'To Date: {self.__to_date}\n'
              f'Person ID: {self.__person_id}\n'
              f'Offense ID: {self.__offense_id}')

    def get_id(self):
        return self.__Id

    def set_id(self, id):
        if id <= 0:
            raise ValueError("Error from Convicts id")
        else:
            self.__Id = id

    def get_from_date(self):
        return self.__from_date

    def set_from_date(self, fd):
        if fd is None:
            raise ValueError("Error from Convicts from date")
        else:
            self.__from_date = fd

    def get_to_date(self):
        return self.__to_date

    def set_to_date(self, td):
        if td is None:
            raise ValueError("Error from Convicts to date")
        else:
            self.__to_date = td

    def get_person_id(self):
        return self.__person_id

    def set_person_id(self, pi):
        if pi <= 0:
            raise ValueError("Error from Convicts person id")
        else:
            self.__person_id = pi

    def get_offense_id(self):
        return self.__offense_id

    def set_offense_id(self, oi):
        if oi <= 0:
            raise ValueError("Error from Convicts offense id")
        else:
            self.__offense_id = oi
