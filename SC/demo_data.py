import sqlite3
import os

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


def show_table(curs):
    rows = curs.execute(f'''
    SELECT COUNT(*) FROM demo
    ''')
    # Show how many rows
    print(f'{rows.fetchall()[0][0]} rows')
    # Show that the rows work
    print(curs.execute('SELECT * FROM demo;').fetchall())
    # Count if both columns got five
    print('Column five counts:', curs.execute('''
    SELECT COUNT(*) FROM demo WHERE x = 5 AND y = 5
    ''').fetchall()[0][0])
    # Show how many distinct values for y column
    print('Y-distincts:', curs.execute('''
    SELECT COUNT(DISTINCT(y)) FROM demo
    ''').fetchall()[0][0])


create_table = '''
CREATE TABLE demo (
    s VARCHAR(2) NOT NULL,
    x INT,
    y INT
)
'''

# Create table
# curs.execute(create_table)

insert_table = f'''
INSERT INTO demo (
    s, x, y
)
VALUES
    ( 'g', 3, 9 ),
    ( 'v', 5, 7 ),
    ( 'f', 8, 7 )
'''
curs.execute(insert_table)

show_table(curs)

# IF you wish to commit another few row inserts
# curs.close()
# conn.commit()
