import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

curs = conn.cursor()

create_demo_table = """
CREATE TABLE demo (
  s char, 
  x INT ,
  y INT
)
"""



curs.execute(create_demo_table)

insert_demo_record1 = """
        INSERT INTO demo
        (s,x,y)
        VALUES ('g',3,9)"""

insert_demo_record2 = """
        INSERT INTO demo
        (s,x,y)
        VALUES ('v',5,7)"""

insert_demo_record3 = """
        INSERT INTO demo
        (s,x,y)
        VALUES ('f',8,7)"""

curs.execute(insert_demo_record1)
curs.execute(insert_demo_record2)
curs.execute(insert_demo_record3)

conn.commit()

query1 = 'select count(*) from demo'
print(curs.execute(query1).fetchall())


query2 = 'select count(*) from demo where x>=5 and y>=5'
print(curs.execute(query2).fetchall())

query3 = 'SELECT count(DISTINCT y) FROM demo'

print(curs.execute(query3).fetchall())
