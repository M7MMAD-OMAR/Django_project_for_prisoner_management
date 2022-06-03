import Connect_DB as c_DB


class Visitings:
    """
    have class Visitings method and properties ID, Date Visited, Person ID, Visitor Name.......
    and Get, Set All Properties
    """

    def __init__(self, date_visited: c_DB.d, person_id: int, visitor_name: str, mountIn_minutes):
        self.date_visited = date_visited
        self.person_id = person_id
        self.visitor_name = visitor_name.strip()
        self.mountIn_minutes = mountIn_minutes

    @classmethod
    def __str__(cls):
        global db
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Visitings"""
            count = 0
            for row in db.cursor().execute(temp_str).fetchall():
                count += 1
                print(str(count), "".center(50, '-'))
                print(f'ID:              {row[0]}\n'
                      f'Date Visited:    {row[1]}\n'
                      f'Person Id:       {row[2]}\n'
                      f'Visitor Name:    {row[3]}\n'
                      f'Mountin Minutes: {row[4]}')
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def add_Visiting(cls, date_visited: c_DB.d, person_id: int, visitor_name: str, mountIn_minutes):
        """Add visitor in DB and check values"""
        global db
        try:
            v = Visitings(date_visited, person_id, visitor_name, mountIn_minutes)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Visitings('date_visited', 'person_id', 'visitor_name', 'mountin_minuts')
                      VALUES (?, ?, ?, ?)"""
            temp_val = (v.date_visited, v.person_id, v.visitor_name, v.mountIn_minutes.strftime("%H:%M"))
            db.cursor().execute(temp_str, temp_val)
            db.commit()
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def select_visitor_by_dateTime(cls, first_date, last_date, first_time=c_DB.t(00, 00), last_time=c_DB.t(23, 59)):
        """Results all values if date and time inside range"""
        global db
        try:
            db = c_DB.connect_DB()
            if first_date > last_date:
                first_date, last_date = last_date, first_date
            temp_str = """SELECT * FROM Visitings WHERE (date_visited BETWEEN :fd AND :ld)
                                                    AND (mountin_minuts BETWEEN :ft AND :lt)"""
            temp_val = (
                {"fd": first_date, "ld": last_date, "ft": first_time.strftime("%H:%M"),
                 "lt": last_time.strftime("%H:%M")})
            # Format result
            count = 0
            print("#".center(7, ' '), end=' | ')
            print("ID".center(7, ' '), end=' | ')
            print("Date Visited".center(14, ' '), end=' | ')
            print("Person ID".center(5, ' '), end=' | ')
            print("Visitor Name".center(50, ' '), end=' | ')
            print("Mount in Minutes".center(7, ' '), end=' | \n')
            print("-" * 130)
            for row in db.cursor().execute(temp_str, temp_val).fetchall():
                count += 1
                print(f' {count} '.center(7, ' '),
                      f' {row[0]} '.center(12, ' '),
                      f' {row[1]} '.center(10, ' '),
                      f' {row[2]} '.center(16, ' '),
                      f' {row[3]} '.center(50, ' '),
                      f' {row[4]} '.center(20, ' '))
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    """Start Getter and Setter Properties."""

    @property
    def date_visited(self):
        return self.__date_visited

    @date_visited.setter
    def date_visited(self, dv):
        try:
            temp_date = c_DB.d(dv.year, dv.month, dv.day)
            date_now = c_DB.d.today()
            if temp_date > date_now:
                raise ValueError(
                    f'Error: From Date Visited must be smaller than {date_now.day}:{date_now.month}:{date_now.year}')
            else:
                if temp_date < c_DB.d(1000, 1, 1):
                    raise ValueError("Error: Date Visited must be greater than 1000:01:01")
                else:
                    self.__date_visited = dv
        except Exception as ex:
            raise Exception(ex)

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, pi: int):
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
        return self.__mountIn_minutes

    @mountIn_minutes.setter
    def mountIn_minutes(self, mm):
        try:
            self.__mountIn_minutes = mm
        except Exception as ex:
            raise Exception(ex.__class__)

    """End Getter and Setter Properties."""
