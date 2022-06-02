from datetime import time, date
import Connect_DB as c_DB
import Visitings as v

"""SELECT * FROM Visitings WHERE mountin_minuts BETWEEN '06:00' and '21:00'"""

# import Convicts as c
# import Dungeon as d, Person as p, Visitings as v, Offense as o, Dungeon_Moves as dm
if __name__ == '__main__':
    try:
        # p.Person.add_person(' ali  ', ' omar  ', ' saleem  ', "  male", date(1199, 1, 1), 'Aziz')
        # p.Person.add_person('mona  ', ' omar', 'khaled  ', "female", date(2001, 11, 8), 'Turkey, Istanbul')
        # p.Person.add_person('   amane   ', '  muhammad  ', ' hamdo ', "     female", date(1199, 1, 1), 'istanbul')
        """Person(115, 116, 117)"""

        # c.Convicts.add_convicts(date(2003, 10, 20), date(2020, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2004, 11, 3), date(2050, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2000, 5, 7), date(2030, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2005, 6, 8), date(2020, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2019, 7, 5), date(2070, 1, 1), 117, 4)
        """Convicts(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"""
        # x = time(3, 40).strftime("%H:%M")
        v.Visitings.add_Visiting(date(1199, 1, 1), 115, "aliiiii", time(3, 40))
        # v.Visitings.__str__()
        v.Visitings.add_Visiting(date(2001, 11, 8), 116, "amera", time(5, 50))
        v.Visitings.add_Visiting(date(2011, 11, 8), 115, "fatema", time(6, 00))
        v.Visitings.add_Visiting(date(2021, 10, 1), 117, "osama", time(20, 20))

        # o.Offense.add_offense("sareka")
        # o.Offense.add_offense("test")
        """Offense(4, 5)"""
        # c.Convicts.select_persons_between_date(date(2003, 10, 20), date(2004, 1, 1) )
    except c_DB.sq.ProgrammingError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
