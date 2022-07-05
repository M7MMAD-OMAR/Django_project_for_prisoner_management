from datetime import time, date
import Connect_DB as c_DB
import Visitings as v

"""SELECT * FROM Visitings WHERE mountin_minuts BETWEEN '06:00' and '21:00'"""

import Convicts as c
import Dungeon as d, Person as p, Visitings as v, Offense as o, Dungeon_Moves as dm

# import Convicts as c
# import Dungeon as d, Person as p, Visitings as v, Offense as o, Dungeon_Moves as dm
if __name__ == '__main__':
    try:
        """Add person in Database and json file"""
        # p.Person.add_person(' yasmeen  ', ' ali  ', ' saleem  ', "  female   ", date(2000, 8, 11), 'Aziz')
        # p.Person.add_person('mona  ', ' omar', 'khaled  ', "female", date(2001, 11, 8), 'Turkey, Istanbul')
        # p.Person.add_person('   amane   ', '  muhammad  ', ' hamdo ', "     female", date(1199, 1, 1), 'istanbul')

        """Print All person in console with Database only"""
        # p.Person.__str__()

        """Delete person or persons in Database and json file"""
        # p.Person.delete_persons_by_id(142, 141, 140)

        """Reset all data in json file, then get data from database"""
        # p.Person.reset_json_by_database()

        """Print all data in console by json file"""
        p.Person.print_all_data_by_json()



        # c.Convicts.add_convicts(date(2003, 10, 20), date(2020, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2004, 11, 3), date(2050, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2000, 5, 7), date(2030, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2005, 6, 8), date(2020, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2019, 7, 5), date(2070, 1, 1), 117, 4)
        """Convicts(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"""

        # v.Visitings.add_Visiting(date(1199, 1, 1), 115, "aliiiii", time(3, 40))
        # v.Visitings.add_Visiting(date(2001, 11, 8), 116, "amera", time(5, 50))
        # v.Visitings.add_Visiting(date(2011, 11, 8), 115, "fatema", time(6, 00))
        # v.Visitings.add_Visiting(date(2021, 10, 1), 117, "osama", time(20, 20))
        """Visitings(23, 24, 25, 26"""

        # o.Offense.add_offense("sareka")
        # o.Offense.add_offense("test")
        """Offense(4, 5)"""

        # d.Dungeon.add_dungeon("zenzana 1   ", 10)
        # d.Dungeon.add_dungeon("zenzana 2   ", 1)
        # d.Dungeon.add_dungeon("zenzana 3   ", 5)
        """Dungeon(10, 11, 12)"""

        # dm.Dungeon_Moves.add_dungeon_moves(10, 115, date(2000, 10, 10))
        # dm.Dungeon_Moves.add_dungeon_moves(10, 116, date(2002, 10, 10))
        # dm.Dungeon_Moves.add_dungeon_moves(10, 116, date(2011, 10, 10))
        # dm.Dungeon_Moves.add_dungeon_moves(10, 115, date(2006, 10, 10))
        """Dungeon_Moves(6, 7, 8, 9, 10)"""
        # dm.Dungeon_Moves.select_person_inside_dungeons(116)
        # c.Convicts.select_persons_by_offense(4)
        # c.Convicts.select_persons_between_date(date(2020, 10, 19), date(2005, 6, 7))
        #
        # v.Visitings.select_visitor_by_dateTime(date(1199, 1, 1), date(2011, 11, 8)
        #                                             , time(3, 50), time(5, 51))
        # v.Visitings.select_visitor_by_dateTime(date(1199, 1, 1), date(2011, 11, 8))
    except c_DB.sq.ProgrammingError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
