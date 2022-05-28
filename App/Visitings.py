class Visitings:
    """
    have class Visitings method and properties ID, Date Visited, Person ID, Visitor Name.......
    and Get, Set All Properties
    """
    def __int__(self, id, date_visited, person_id, visitor_name, mountin_minutes):
        if (id and person_id and mountin_minutes > 0) and (date_visited is not None) and len(visitor_name) > 0:
            self.__Id = id
            self.__date_visited = date_visited
            self.__person_id = person_id
            self.__visitor_name = visitor_name
            self.__mountin_minutes = mountin_minutes
        else:
            raise Exception("Error from Visitings constructor")

    def __str__(self):
        print(f'ID: {self.__Id}\n'
              f'Date Visited: {self.__date_visited}\n'
              f'Person Id: {self.__person_id}\n'
              f'Visitor Name: {self.__visitor_name}\n'
              f'Mountin Minutes: {self.__mountin_minutes}')

    def get_id(self):
        return self.__Id

    def set_id(self, id):
        if id <= 0:
            raise ValueError("Error from Visitings id")
        else:
            self.__Id = id

    def get_date_visited(self):
        return self.__date_visited

    def set_date_visited(self, dv):
        if dv is None:
            raise ValueError("Error from Visitings date visited")
        else:
            self.__date_visited = dv

    def get_person_id(self):
        return self.__person_id

    def set_person_id(self, pi):
        if pi <= 0:
            raise ValueError("Error from Visitings person id")
        else:
            self.__person_id = pi

    def get_visitor_name(self):
        return self.__visitor_name

    def set_visitor_name(self, vn):
        if len(vn) <= 1:
            raise ValueError("Error from Visitings visitor name")
        else:
            self.__visitor_name = vn

    def get_mountin_minutes(self):
        return self.__mountin_minutes

    def set_mountin_minutes(self, mm):
        if mm <= 0:
            raise ValueError("Error from Visitings mountin minutes")
        else:
            self.__mountin_minutes = mm
