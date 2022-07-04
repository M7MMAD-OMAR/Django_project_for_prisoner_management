import Connect_DB as c_DB


class Offense:
    """
    have class Offense method and properties name.......
    and Get, Set All Properties
    """

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def __str__(cls):
        db = None
        try:
            db = c_DB.connect_DB()
            temp_str = """SELECT * FROM Offense"""
            for row in db.cursor().execute(temp_str).fetchall():
                print(f'ID:         {row[0]}\n'
                      f'Name:  {row[1]}')
        except Exception as ex:
            raise Exception(ex)
        finally:
            if db:
                db.close()

    @classmethod
    def add_offense(cls, name: str):
        """Add Offense name In DB and check value"""
        db = None
        try:
            o = Offense(name)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Offense('name') VALUES(:n)"""
            db.cursor().execute(temp_str, {"n": o.name})
            db.commit()
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    """Start Getter and Setter Properties."""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if len(n) <= 1:
            raise ValueError("Error: Offense name must be greater than one Character")
        else:
            db = None
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT name FROM Offense WHERE name=:n"""
                if db.cursor().execute(temp_str, {"n": n}).fetchone():
                    raise ValueError("Error: Offense Name is already defined")
                else:
                    self.__name = n
            except ValueError as ex:
                raise ex
            except Exception as ex:
                raise ex
            finally:
                if db:
                    db.close()

    """End Getter and Setter Properties."""
