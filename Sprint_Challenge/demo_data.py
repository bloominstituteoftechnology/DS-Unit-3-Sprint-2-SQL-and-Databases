import sqlite3

# form connection to 'demo_data' sqlite3 db
conn = sqlite3.connect('demo_data.sqlite3')

# create cursor
curs = conn.cursor()

# set schema for the 'demo' table
create_demo_table = ("""
    CREATE TABLE demo (
        s CHAR(1),
        x INT,
        y INT
    )
""")

# create the table in demo_data db
curs.execute(create_demo_table)

# insert data into the 'demo' table
insert_data = """
INSERT INTO demo (s, x, y)
VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
"""

curs.execute(insert_data)

# save changes
conn.commit()

## test queries to make sure that everything worked

#how many rows? - 3
test_1 = ("SELECT COUNT(*) FROM demo")
print("How many rows?: ", curs.execute(test_1).fetchone())

#How many rows are there where both x and y are at least 5?
test_2 = ("SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5")
print("How many rows where 'x' and 'y' at least 5: ", curs.execute(test_2).fetchone())

#How many unique values of y are there (hint - COUNT() can accept
#a keyword DISTINCT)?
test_3 = ("SELECT DISTINCT COUNT(y) FROM demo")
print("How many distinct 'y'?: ", curs.execute(test_3).fetchone())

