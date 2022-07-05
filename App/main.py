from datetime import time, date
import Connect_DB as c_DB
import Visits as v

import Convicts as c
import Dungeon as d, Person as p, Visits as v, Offense as o, Dungeon_Moves as dm

# import Convicts as c
# import Dungeon as d, Person as p, Visits as v, Offense as o, Dungeon_Moves as dm
if __name__ == '__main__':
    try:
        """ Person """
        """Add person in Database and json file"""
        # p.Person.add_person(' maroa  ', ' ali  ', ' saleem  ', "  female   ", date(2000, 8, 11), 'Aziz')
        # p.Person.add_person('mona  ', ' omar', 'khaled  ', "female", date(2001, 11, 8), 'Turkey, Istanbul')
        # p.Person.add_person('   amane   ', '  muhammad  ', ' hamdo ', "     female", date(1199, 1, 1), 'istanbul')

        """Print All person in console with Database only"""
        # p.Person.__str__()

        """
        Delete person or persons in Database and json file
        Warning: if person id referencing other tables, you can't delete person 
        """
        # p.Person.delete_persons_by_id(114, 116, 152)

        """Reset all Person data in json file, then get data from database"""
        # p.Person.reset_json_by_database()

        """Print all Person data in console by json file"""
        # p.Person.print_all_data_by_json()


        """ Convicts """
        """Add convicts in Database and json file"""
        # c.Convicts.add_convicts(date(2003, 10, 20), date(2020, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2004, 11, 3), date(2050, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2000, 5, 7), date(2030, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2005, 6, 8), date(2020, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2019, 7, 5), date(2070, 1, 1), 117, 4)

        """Print All convicts in console with Database only"""
        # c.Convicts.__str__()

        """Return persons by offense id and print offense name"""
        # c.Convicts.select_persons_by_offense_id(4)

        """Return Persons between tow date first and second date"""
        # c.Convicts.select_persons_between_date(date(2004, 11, 3), date(2005, 6, 8))

        """Delete Convicts in Database and json file"""
        # c.Convicts.delete_convicts_by_id(39)

        """Print all Convicts data in console by json file only"""
        # c.Convicts.print_all_data_by_json()

        """Reset all Convicts data in json file, then get data from database"""
        # c.Convicts.reset_json_by_database()







        """ Visits """
        """Add Visits in Database and json file"""
        # v.Visits.add_Visiting(date(1199, 1, 1), 115, "karam", time(3, 40))
        # v.Visits.add_Visiting(date(2001, 11, 8), 116, "amera", time(5, 50))
        # v.Visits.add_Visiting(date(2011, 11, 8), 115, "fatema", time(6, 00))
        # v.Visits.add_Visiting(date(2021, 10, 1), 117, "osama", time(20, 20))

        """
        Select visitor by date and time (first data, second data, first time, second time)
        Warning: No problem if change first data, time and second data, time
        """
        # v.Visits.select_visitor_by_datetime(date(2011, 11, 8), date(1199, 1, 8), time(23, 00), time(1, 00))

        """
        Select visitor by date only (first date, second date
        Warning: No problem if change first data and second data
        """
        # v.Visits.select_visitor_by_datetime(date(2011, 11, 8), date(1199, 1, 8))
        # v.Visits.select_visitor_by_datetime(date(1199, 1, 8), date(2011, 11, 8))

        """Print All Visits in console with Database only"""
        # v.Visits.__str__()

        """Reset all Visits data in json file, then get data from database"""
        # v.Visits.reset_json_by_database()


        """Print all Visits data in console by json file only"""
        # v.Visits.print_all_data_by_json()


        """Delete Visits in Database and json file"""
        # v.Visits.delete_visitor_by_id(33)





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

        #

    except c_DB.sq.ProgrammingError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
