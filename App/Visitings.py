import Connect_DB as c_DB


class Visitings:
    """
    have class Visitings method and properties ID, Date Visited, Person ID, Visitor Name.......
    and Get, Set All Properties
    """

    cls = None

    def __init__(self, date_visited: str, person_id: int, visitor_name: str, mountIn_minutes: str):
        cls = self
        self.date_visited = date_visited.strip()
        self.person_id = person_id
        self.visitor_name = visitor_name.strip()
        self.mountIn_minutes = mountIn_minutes.strip()

    def __str__(self):
        print(f'Date Visited: {self.date_visited}\n'
              f'Person Id: {self.person_id}\n'
              f'Visitor Name: {self.visitor_name}\n'
              f'Mountin Minutes: {self.mountIn_minutes}')

    def add_Visiting(self, date_visited: str, person_id: int, visitor_name: str, mountIn_minutes: str):
        global db
        try:
            Visitings(date_visited, person_id, visitor_name, mountIn_minutes)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Visitings('date_visited', 'person_id', 'visitor_name', 'mountin_minuts')
                      VALUES (?, ?, ?, ?)"""
            temp_val = (date_visited, person_id, visitor_name, mountIn_minutes)
            db.cursor().execute(temp_str, temp_val)
            db.commit()
            print("added Visitings")
        except Exception as ex:
            raise Exception(ex)

    @property
    def date_visited(self):
        return self.__date_visited

    @date_visited.setter
    def date_visited(self, dv):
        if len(dv) <= 0:
            raise ValueError("Error: No value entered for the Date Visited")
        else:
            temp_split = dv.split(', ')
            temp_date = c_DB.dt.strptime(temp_split[0], "%d-%m-%Y")
            c_DB.dt.strptime(temp_split[1], "%H:%M")
            date_now = c_DB.dt.now()
            if temp_date > c_DB.dt.now():
                raise ValueError(
                    f'Error: From Date Visited must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
            else:
                self.__date_visited = dv

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, pi):
        if pi <= 0:
            raise ValueError("Error: Person ID must be greater than Zero")
        else:
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
                raise c_DB.sq.ProgrammingError(ex)
            except ValueError as ex:
                raise ValueError(ex)
            finally:
                if db:
                    db.close()

    @property
    def visitor_name(self):
        return self.__visitor_name

    @visitor_name.setter
    def visitor_name(self, vn):
        if len(vn) <= 1:
            raise ValueError("Error: Visitor name must be greater than one Character")
        else:
            self.__visitor_name = vn

    @property
    def mountIn_minutes(self):
        return self.mountIn_minutes

    @mountIn_minutes.setter
    def mountIn_minutes(self, mm):
        try:
            if len(mm) <= 0:
                raise ValueError("Error: No value entered for the date")
            else:
                c_DB.dt.strptime(mm, "%H:%M")
                self.__mountIn_minutes = mm
        except ValueError as ex:
            raise ValueError(ex)
