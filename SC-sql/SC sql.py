""" DOCSTRING
THIS IS A .py TAHT CREAT A DEMO DATABASE
"""

import sqlite3

# Open a connection and crate database
conn = sqlite3.connect('C:\\Users\\mhdal\\github\\SC sql\\demo_data.db')
cur = conn.cursor()

# Create Table
cur.execute('''CREATE TABLE demo (s TEXT, x INT, y INT)''')
conn.commit()

s_l = ['g','v','f']
x_l = ['3','5','8']
y_l = ['9','7','7']
for i in range(len(s_l)):
    s_c = s_l[i]
    x_i = x_l[i]
    y_i = y_l[i]
    cur.execute('''INSERT INTO demo (s, x, y) VALUES(?,?,?)''', (s_c, x_i, y_i))
conn.commit()

print('Number of rows in DB', cur.execute('''SELECT COUNT(*) FROM demo''').fetchall()[0][0])
print('Number of rows where x and y are at least 5', cur.execute('''SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5''').fetchall()[0][0])
print('Number of unique values in y', cur.execute('''SELECT COUNT(DISTINCT y) FROM demo''').fetchall()[0][0])

