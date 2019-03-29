import sqlite3

'''create a three row test database'''

'''connect to blank file and add table schema'''
conn = sqlite3.connect('demo_data.sqlite3')
cursor = conn.cursor()
create_table = """CREATE TABLE demo_data (S VARCHAR(1),
                                          X INT,
                                          Y INT);"""
cursor.execute(create_table)


'''add three rows to the table'''
row1 = """INSERT INTO demo_data
          VALUES ('g', 3, 9);"""

row2 = """INSERT INTO demo_data
          VALUES ('v', 5, 7);"""

row3 = """INSERT INTO demo_data
          VALUES ('f', 8, 7);"""

cursor.execute(row1)
cursor.execute(row2)
cursor.execute(row3)
commit()

'''how many rows are there?'''
rowcount = """SELECT COUNT(*) FROM demo_data;"""
print(cursor.execute(rowcount).fetchall())


'''how many rows are there where the number
   in 'X' and "Y' is at least 5?'''
fivecount = """SELECT COUNT(*) FROM demo_data
               WHERE demo_data.X > 5
               AND demo_data.Y >5;"""
print(cursor.execute(fivecount).fetchall())


'''how many unique are there of y?'''
uniquecount = """SELECT COUNT(DISTINCT Y) FROM demo_data;"""
print(cursor.execute(uniquecount).fetchall())
