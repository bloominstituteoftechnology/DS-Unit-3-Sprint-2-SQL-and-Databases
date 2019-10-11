import sqlite3

#Connect to sqlite file 
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

#Delete the table if one exists already
delete_table = 'DROP TABLE IF EXISTS demo'
curs.execute(delete_table)

#Create the table and insert values
createtbl = "CREATE TABLE demo (s varchar(255),x int, y int);"
inserttbl = """
INSERT INTO demo(
    s,
    x,
    y)
VALUES
    ('g','v','f'), 
    (3,5,8), 
    (9,7,7);
"""
curs.execute(createtbl)
curs.execute(inserttbl)

count_row = """
SELECT COUNT(s)
FROM demo;
"""
#Returns 3


atleast_five = """
SELECT COUNT(*)
FROM demo
WHERE X = 5 AND Y = 5;
"""
#Returns 0


unique = """
SELECT COUNT(DISTINCT y)
FROM demo;
"""
#Returns 2

print(curs.execute(count_row).fetchall()) #Returns 3
print(curs.execute(atleast_five).fetchall()) #Returns 0
print(curs.execute(unique).fetchall()) #Returns 2

#Close and commit!
curs.close()
conn.commit()