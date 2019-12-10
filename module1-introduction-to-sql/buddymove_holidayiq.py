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
