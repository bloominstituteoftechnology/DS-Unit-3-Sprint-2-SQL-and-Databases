# Pythonic Python Pythonifies the Pythas.
import psycopg2
import sqlite3
import os


def table_reveal():
    # Query table using this postgresql internal thingie
    show_tables = f'''
    SELECT * FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schema'
    '''
    pg_curs.execute(show_tables)
    print(pg_curs.fetchall())
    thingie = curs.execute('PRAGMA table_info(titanic);').fetchall()
    for i in thingie:
        print(i)


# Connect to this special csv; Get cursor for this table
conn = sqlite3.connect('../module2-sql-for-analysis/titanic.sqlite3')
curs = conn.cursor()

pswd = os.environ.get('password')
# Don't even try
user = os.environ.get('username')
host = 'salt.db.elephantsql.com'
dbnm = user

# Connect to postgres; Get cursor
pg_conn = psycopg2.connect(dbname=dbnm, user=user,
                           password=pswd, host=host)
pg_curs = pg_conn.cursor()

# Get passengers
passengers = curs.execute('SELECT * FROM titanic;').fetchall()
if len(passengers) != 887:
    raise ValueError("Not the right table")

table_reveal()

survival_query = curs.execute(f'''
SELECT SUM(Survived) FROM titanic;
''').fetchall()[0][0]
print(f'''
Amount of survivors:\t{survival_query}
Non-survivors:\t\t{len(passengers)-survival_query}
''')

passengers_per_class = curs.execute(f'''
SELECT Pclass, COUNT(Pclass) FROM titanic
GROUP BY Pclass;
''').fetchall()
print(f'Amount of passengers per Class: {passengers_per_class}')

death_within_class = curs.execute(f'''
SELECT Pclass, SUM(Survived) FROM titanic
GROUP BY Pclass;
''').fetchall()
print(f'''
First Class:\t{death_within_class[0]}
Second Class:\t{death_within_class[1]}
Third Class:\t{death_within_class[2]}
''')

# Just gonna assume 1 is alive and 0 is not
average_age_sNs = curs.execute(f'''
SELECT ROUND(AVG(Age),2), Survived FROM titanic
GROUP BY Survived;
''').fetchall()
print(f'''
Avg Death Age:\t{average_age_sNs[0]}
Avg Alive Age:\t{average_age_sNs[1]}
''')

average_age_pCl = curs.execute(f'''
SELECT ROUND(AVG(Age),2), Pclass FROM titanic
GROUP BY Pclass;
''').fetchall()
print(f'''
Class Ages\t-----
First Class:\t{average_age_pCl[0]}
Second Class:\t{average_age_pCl[1]}
Third Class:\t{average_age_pCl[2]}
''')

listo = ['Pclass', 'Survived']
lasto = ['Fare', '`Siblings/Spouses Aboard`',
         '`Parents/Children Aboard`']
for a in listo:
    for b in lasto:
        average = curs.execute(f'''
        SELECT ROUND(AVG({b}),2), {a} FROM titanic
        GROUP BY {a};
        ''').fetchall()
        print(f'''By {a}\t---
        Average {b}\n\t{average}''')

""" Not sure but there either really are no similiar names or when I made the
Postgres database I messed up the names a bit.
name_check = curs.execute(f'''
SELECT name FROM titanic
WHERE name NOT IN (
    SELECT DISTINCT(name) FROM titanic
)
''').fetchall()
name_check = curs.execute(f'''
SELECT DISTINCT(name) FROM titanic;
''').fetchall()
print(len(name_check))
"""
