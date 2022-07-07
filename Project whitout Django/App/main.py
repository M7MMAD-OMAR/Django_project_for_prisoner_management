import Connect_DB as c_DB

import Convicts as c
import Dungeon as d, Person as p, Visits as v, Offense as o, Dungeon_Moves as dm

# import Convicts as c
# import Dungeon as d, Person as p, Visits as v, Offense as o, Dungeon_Moves as dm
if __name__ == '__main__':
    try:
        """ Person Start """
        """Add person in Database and json file"""
        # p.Person.add_person(' maroa  ', ' ali  ', ' saleem  ', "  female   ", date(2000, 8, 11), 'Aziz')
        # p.Person.add_person('mona  ', ' omar', 'khaled  ', "female", date(2001, 11, 8), 'Turkey, Istanbul')
        # p.Person.add_person('   amane   ', '  muhammad  ', ' hamdo ', "     female", date(1199, 1, 1), 'istanbul')

        """
        Delete person or persons in Database and json file
        You can delete more than person or delete one person 
        Warning: if person id referencing other tables, you can't delete person 
        """
        # p.Person.delete_persons_by_id(114, 116, 152)

        """Print All person in console with Database only"""
        # p.Person.__str__()

        """Reset all Person data in json file, then get data from database"""
        # p.Person.reset_json_by_database()

        """Print all Person data in console by json file"""
        # p.Person.print_all_data_by_json()

        """ Person End """




        """ Convicts Start """
        """Add convicts in Database and json file"""
        # c.Convicts.add_convicts(date(2003, 10, 20), date(2020, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2004, 11, 3), date(2050, 1, 1), 115, 4)
        # c.Convicts.add_convicts(date(2000, 5, 7), date(2030, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2005, 6, 8), date(2020, 1, 1), 116, 5)
        # c.Convicts.add_convicts(date(2019, 7, 5), date(2070, 1, 1), 117, 4)

        """
        Delete Convicts in Database and json file
        You can delete more than Convicts or delete one Convicts 
        """
        # c.Convicts.delete_convicts_by_id(39)

        """Print All convicts in console with Database only"""
        # c.Convicts.__str__()

        """Return persons by offense id and print offense name"""
        # c.Convicts.select_persons_by_offense_id(4)

        """Return Persons between tow date first and second date"""
        # c.Convicts.select_persons_between_date(date(2004, 11, 3), date(2005, 6, 8))

        """Print all Convicts data in console by json file only"""
        # c.Convicts.print_all_data_by_json()

        """Reset all Convicts data in json file, then get data from database"""
        # c.Convicts.reset_json_by_database()
        """ Convicts End """




        """ Visits Start """
        """Add Visits in Database and json file"""
        # v.Visits.add_Visiting(date(1199, 1, 1), 115, "karam", time(3, 40))
        # v.Visits.add_Visiting(date(2001, 11, 8), 116, "amera", time(5, 50))
        # v.Visits.add_Visiting(date(2011, 11, 8), 115, "fatema", time(6, 00))
        # v.Visits.add_Visiting(date(2021, 10, 1), 117, "osama", time(20, 20))

        """
        Delete Visits in Database and json file
        You can delete more than Visits or delete one Visits
        """
        # v.Visits.delete_visitor_by_id(33)

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

        """ Visits End """



        """ Dungeon Moves Start """
        """Add Dungeon Moves in Database and json file"""
        # dm.Dungeon_Moves.add_dungeon_moves(12, 155, date(1950, 5, 8))
        # dm.Dungeon_Moves.add_dungeon_moves(10, 116, date(2002, 10, 10))
        # dm.Dungeon_Moves.add_dungeon_moves(10, 116, date(2011, 10, 10))
        # dm.Dungeon_Moves.add_dungeon_moves(10, 115, date(2006, 10, 10))

        """
        Delete Dungeon Moves in Database and json file
        You can delete more than Dungeon or delete one Dungeon
        """
        # dm.Dungeon_Moves.delete_dungeon_moves_by_id(8, 9)

        """Print All Dungeon Moves in console with Database only"""
        # dm.Dungeon_Moves.__str__()

        """Result persons inside dungeons and print's"""
        # dm.Dungeon_Moves.select_person_inside_dungeons(115)

        """Reset all Dungeon Moves data in json file, then get data from database"""
        # dm.Dungeon_Moves.reset_json_by_database()

        """Print all Dungeon Moves data in console by json file only"""
        # dm.Dungeon_Moves.print_all_data_by_json()

        """ Dungeon Moves End """




        """ Offense Start """

        """Add Offense in Database and json file"""
        # o.Offense.add_offense("first")
        # o.Offense.add_offense("second")

        """
        Delete Offense in Database and json file
        You can delete more than Offense or delete one Offense
        Warning: if Offense id referencing other tables, you can't delete Offense 
        """
        # o.Offense.delete_offense_by_id(6)

        """Print All Offense in console with Database only"""
        # o.Offense.__str__()

        """Reset all Offense data in json file, then get data from database"""
        # o.Offense.reset_json_by_database()

        """Print all Offense data in console by json file only"""
        # o.Offense.print_all_data_by_json()

        """ Offense End """




        """ Dungeon Start """
        """Add Dungeon in Database and json file"""
        # d.Dungeon.add_dungeon("   weee   ", 123)
        # d.Dungeon.add_dungeon("    second    ", 5)
        # d.Dungeon.add_dungeon("  third    ", 10000)

        """
        Delete Dungeon in Database and json file
        You can delete more than Dungeon or delete one Dungeon
        Warning: if Dungeon id referencing other tables, you can't delete Dungeon 
        """
        # d.Dungeon.delete_dungeon_by_id()

        """Print All Dungeon in console with Database only"""
        # d.Dungeon.__str__()

        """Reset all Dungeon data in json file, then get data from database"""
        # d.Dungeon.reset_json_by_database()

        """Print all Dungeon data in console by json file only"""
        # d.Dungeon.print_all_data_by_json()
        """ Dungeon End """


    except c_DB.sq.ProgrammingError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
