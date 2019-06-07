import sqlite3

connect = sqlite3.connect('demo_data.sqlite3')


create_statement="""
... CREATE TABLE demo(
... s varchar(30),
... x integer,
... y integer)"""

create_statement
curs=connect.cursor()
curs.execute(create_statement)
connect.commit()
insert ="INSERT INTO demo VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);"
insert
curs.execute(insert)
query = 'SELECT * FROM demo;'
results = curs.execute(query)
results.fetchall()
connect.commit()
query  =' SELECT COUNT(*) FROM demo;'
results =curs.execute(query)
results.fetchall()
query ='SELECT COUNT(*) FROM demo WHERE x >= 5  AND y >=5;'
results = curs.execute(query)
results.fetchall()
query = 'SELECT COUNT(DISTINCT y) FROM demo;'
results= curs.execute(query)
results.fetchall()
connect.commit()
