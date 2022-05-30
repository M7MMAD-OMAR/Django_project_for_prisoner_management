import Person, Dungeon, Dungeon_Moves, Visitings, Connect_DB as c_DB, Offense

# Person
if __name__ == '__main__':
    try:
        # p = Person.Person('nn', ' 11', ' qq', "male", '15-06-1099   ', ' aa')
        # p.add_person(' qq', '333 ', 'last_name', "female", '15-2-3003', 'Azaz')
        # d = Dungeon.Dungeon("ppp ", 555)
        # print("Add")
        # d.add_dungeon("ppp1", 22)
        # dm = Dungeon_Moves.Dungeon_Moves(5, 101, '15-2-2003, 10:12')
        # v = Visitings.Visitings('15-06-1099, 08:03', 101, 'wesal', '00:30')
        # v.add_Visiting('15-06-1099, 08:03', 101, 'wesal', '00:30')
        o = Offense.Offense("zena")
        o.add_offense("  zena   ")
    except c_DB.sq.ProgrammingError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
print("fucking 👌🖖👌🏻")