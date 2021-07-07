import sqlite3 as sql


def create_connection(dbfile):
    """
    Create a connection to the db file:
        param: dbfile = Database file to connect
        to and run queries on.
        return: connection object to that database
    """
    conn = sql.connect(dbfile)
    return conn


def create_cursor(connection):
    """
    Create a cursor for executing SQL in the database
    on the provided connection.
    """
    curs = connection.cursor()
    return curs


def commit_and_close(connection):
    connection.commit()
    connection.close()
    return


# Set condition for running script and getting back the results for each query.

if __name__ == '__main__':
    con1 = create_connection('rpg_db.sqlite3')
    cur1 = create_cursor(con1)

    answer1 = cur1.execute("SELECT COUNT(*) FROM charactercreator_character;").fetchall()[0][0]
    print(f" Question: How many characters are there? Ans:{answer1}. ")

    answer2a = cur1.execute("SELECT COUNT(*) FROM charactercreator_cleric;").fetchall()[0][0]
    answer2b = cur1.execute("SELECT COUNT(*) FROM charactercreator_mage;").fetchall()[0][0]
    answer2c = cur1.execute("SELECT COUNT(*) FROM charactercreator_fighter;").fetchall()[0][0]
    answer2d = cur1.execute("SELECT COUNT(*) FROM charactercreator_necromancer;").fetchall()[0][0]
    answer2e = cur1.execute("SELECT COUNT(*) FROM charactercreator_thief;").fetchall()[0][0]
    print(f" Question: How many characters from each class are there? ")
    print(f" Fighter: {answer2c} ")
    print(f" Mage: {answer2b} ")
    print(f" Thief: {answer2e} ")
    print(f" Cleric: {answer2a} ")
    print(f" Necromancer: {answer2d} ")

    answer3 = cur1.execute(" SELECT COUNT(*) FROM armory_item;").fetchall()[0][0]
    print(f" Question: How many total items are there? Ans: {answer3}. ")

    answer4 = cur1.execute(" SELECT COUNT(*) FROM armory_item, armory_weapon WHERE item_id == item_ptr_id; ").fetchall()[0][0]
    print(f" Question: How many items are weapons? Ans: {answer4}. ")

    answer5 = cur1.execute("""
                           SELECT cc.name, COUNT(*) FROM charactercreator_character as cc,
                           armory_item as ai,
                           charactercreator_character_inventory as ci
                           WHERE cc.character_id == ci.character_id
                           AND ci.item_id == ai.item_id
                           GROUP BY cc.character_id
                           LIMIT 20;
                           """).fetchall()
    print(f" Question: How many items does each character have (first 20)? Ans: ")
    for rows in answer5:
        print("Name:",rows[0],"Items:",rows[1])

    answer6 = cur1.execute("""
                          SELECT cc.name,
                          COUNT(*) FROM charactercreator_character as cc,
                          armory_item as ai,
                          charactercreator_character_inventory as ci,
                          armory_weapon as aw
                          WHERE cc.character_id == ci.character_id
                          AND ci.item_id == ai.item_id
                          AND ai.item_id == aw.item_ptr_id
                          GROUP BY cc.character_id
                          LIMIT 20;
                          """).fetchall()
    print(f" Question: How many weapons does each character have (first 20)? Ans: ")
    for rows in answer6:
        print("Name:",rows[0],"Items:",rows[1])

    answer7 = cur1.execute("""
                          SELECT ROUND(AVG(number_of_items), 2) FROM (
                              SELECT COUNT(*) number_of_items FROM charactercreator_character as cc,
                              armory_item as ai,
                              charactercreator_character_inventory as ci
                              WHERE cc.character_id == ci.character_id
                              AND ci.item_id == ai.item_id
                              GROUP BY cc.character_id
                              );
                          """).fetchall()[0][0]
    print(f" Question: On average, How many items do the characters have? Ans: {answer7}. ")

    answer8 = cur1.execute("""
                          SELECT ROUND(AVG(number_of_weapons), 2) FROM (
                              SELECT COUNT(*) number_of_weapons FROM charactercreator_character as cc,
                              armory_item as ai,
                              armory_weapon as aw,
                               charactercreator_character_inventory as ci
                              WHERE cc.character_id == ci.character_id
                              AND ci.item_id == ai.item_id
                              AND ai.item_id == aw.item_ptr_id
                              GROUP BY cc.character_id
                              );
                          """).fetchall()[0][0]
    print(f" Question: On average, How many weapons do the characters have? Ans: {answer8}. ")
    commit_and_close(con1)

