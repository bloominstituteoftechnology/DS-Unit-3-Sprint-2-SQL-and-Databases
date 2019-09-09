import sqlite3
import os

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# Question 1 - How many rows are there
print('Answer 1')
print('-----------')
a1 = curs.execute('SELECT COUNT(Id) FROM review').fetchall()[0][0]
print(f'There are {a1} rows in the table')
print('\n')

# Question 2
print('Answer 2')
print('-----------')
a2 = curs.execute('''SELECT COUNT(Id) FROM review
                     WHERE Nature > 100 AND Shopping > 100''').fetchall()[0][0]
print(f'{a2} users reviewed at least 100 in both categories')
