import sqlite3


con = sqlite3.connect('demo_data.sqlite3')
curs = con.cursor()

q1 = '''
CREATE TABLE demo_data
(s, x, y);
'''

curs.execute(q1)

q2 = '''
INSERT INTO demo_data
VALUES ("g", 3, 9), ("v", 5, 7), ("f", 8, 7);
'''

curs.execute(q2)

curs.close()
con.commit()
con.close()
