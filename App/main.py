import Person, Dungeon, Dungeon_Moves

# Person
if __name__ == '__main__':
    try:
        pass
        # p = Person.Person('nn', ' 11', ' qq', "male", '15-06-1099   ', ' aa')
        # p.add_person(' qq', '333 ', 'last_name', "female", '15-2-3003', 'Azaz')
        # d = Dungeon.Dungeon("ppp ", 555)
        # print("Add")
        # d.add_dungeon("ppp1", 22)

        dm = Dungeon_Moves.Dungeon_Moves(5, 101, '15-2-2003, 10:12')
    except Exception as ex:
        print(ex)
