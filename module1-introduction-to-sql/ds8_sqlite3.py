import sqlite3

conn = sqlite3.connect('toy_data.db')

conn

import os
os.listdir()

query = 'CREATE TABLE toy (name varchar(30), size int);'

curs = conn.cursor()
dir(curs)

curs.execute(query)

curs.close()
conn.commit()

curs2 = conn.cursor()

curs2.execute('SELECT * FROM toy;').fetchall()

insert_query = 'INSERT INTO toy (name, size) VALUES ("awesome", 27);'

curs2.execute(insert_query)
curs2.close()
conn.commit()

curs3 = conn.cursor()
curs3.execute('SELECT * from toy;').fetchall()
