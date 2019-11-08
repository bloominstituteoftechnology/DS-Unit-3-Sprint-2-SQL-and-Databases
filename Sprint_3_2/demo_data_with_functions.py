import sqlite3
CONN = sqlite3.connect('demo_data_2.sqlite3')
DATA = [
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)
        ]

""" Delete table if exists created anticipating file being
run multiple times.
"""
curs = CONN.cursor()
delete_table = "DROP TABLE IF EXISTS demo_2"
curs.execute(delete_table)
curs.close()
CONN.commit()


def make_db():
    """Make and populate the demo_2 database."""
    curs = CONN.cursor()
    curs.execute("""
                    CREATE TABLE demo_2(
                        's' char(1),
                        'x' INT,
                        'y' INT
                                    );
                    """
                )   

    for datum in DATA:
        curs.execute("""
        INSERT INTO demo_2(s, x, y) 
        VALUES""" + str(datum))
    curs.close()
    CONN.commit()


def run_queries():
    """Run and printe output from queries for sprint challenge questions."""
    curs = CONN.cursor()
    print(curs.execute('SELECT COUNT(*) FROM demo_2;').fetchall())
    print(curs.execute('SELECT COUNT(*) FROM demo_2 WHERE x >= 5 AND y >= 5;').fetchall())
    print(curs.execute('SELECT COUNT (DISTINCT y) FROM demo_2;').fetchall())



if __name__== "__main__":
    make_db()
    run_queries()    