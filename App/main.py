import Connect_DB as c_DB
from datetime import date


import Convicts as c
import Dungeon as d, Person as p, Visitings as v, Offense as o, Dungeon_Moves as dm

# import Convicts as c
# import Dungeon as d, Person as p, Visitings as v, Offense as o, Dungeon_Moves as dm
if __name__ == '__main__':
    try:
        # p.Person.__str__()
        # p.Person.print_data()
        # p.Person.add_person(' ali  ', ' omar  ', ' saleem  ', "  male", date(1199, 1, 1), 'Aziz')
        # p.Person.add_person('mona  ', ' omar', 'khaled  ', "female", date(2001, 11, 8), 'Turkey, Istanbul')
        # p.Person.add_person('   amane   ', '  muhammad  ', ' hamdo ', "     female", date(1199, 1, 1), 'istanbul')
        # o.Offense.add_offense(o.Offense.cls, 'serge')
        # o.Offense.add_offense(o.Offense.cls, 'kazeb')

        # c.Convicts.add_convicts(date(2003, 10, 20), date(2020, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2004, 11, 3), date(2050, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2000, 5, 7), date(2030, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2005, 6, 8), date(2020, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2019, 7, 5), date(2070, 1, 1), 117, 4)

        # v.Visitings.add_Visiting(date(1199, 1, 1), 1, "ali", '20:20')
        # v.Visitings.add_Visiting(date(2001, 11, 8), 101, "ali", '20:20')
        # v.Visitings.add_Visiting(date(2001, 11, 8), 101, "ali", '20:20')
        # v.Visitings.add_Visiting(date(2001, 11, 8), 101, "ali", '20:20')
        # v.Visitings.print_data()

        # o.Offense.add_offense("sareka")
        # o.Offense.add_offense("test")
        c.Convicts.select_persons_between_date(date(2003, 10, 20), date(2004, 1, 1) )
    except c_DB.sq.ProgrammingError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
