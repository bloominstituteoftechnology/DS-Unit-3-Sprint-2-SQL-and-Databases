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

#Counts the amount of rows
count_row = """
SELECT COUNT(s)
FROM demo;
"""
#Returns 3

#counts how many instances that both x and y contain 5
atleast_five = """
SELECT COUNT(*)
FROM demo
WHERE x = 5 AND y = 5;
"""
#Returns 0

#counts the number of unique values in y
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