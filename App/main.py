import Connect_DB as c_DB
import Convicts as c
import Dungeon as d, Person as p, Visitings as v, Offense as o, Dungeon_Moves as dm

# import Convicts as c
# import Dungeon as d, Person as p, Visitings as v, Offense as o, Dungeon_Moves as dm

if __name__ == '__main__':
    try:

        # p.Person.add_person(p.Person.cls, 'ali', ' omar', 'saleem', "male", '15-06-1099   ', 'Azaz')
        # p.Person.add_person(p.Person.cls, 'amane', 'muhammad', 'hamdo', "female", '01-01-1999', 'istanbul')
        # o.Offense.add_offense(o.Offense.cls, 'serge')
        # o.Offense.add_offense(o.Offense.cls, 'kazeb')

        # c.Convicts.add_convicts(c.Convicts.cls, '10-10-2020', '01-01-2010', 104, 3)
        # c.Convicts.add_convicts(c.Convicts.cls, '10-10-2000', '15-10-2020', 104, 3)
        # c.Convicts.add_convicts(c.Convicts.cls, '10-12-2011', '01-01-2020', 104, 3)
        # c.Convicts.add_convicts(c.Convicts.cls, '10-10-2000', '01-01-2020', 104, 3)
        # c.Convicts.add_convicts(c.Convicts.cls, '01-01-2020', '15-02-3008', 101, 2)

        dm.Dungeon_Moves.add_dungeon_moves(dm.Dungeon_Moves.cls, 5, 103, '1-1-2002, 20:59')
    except c_DB.sq.ProgrammingError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
