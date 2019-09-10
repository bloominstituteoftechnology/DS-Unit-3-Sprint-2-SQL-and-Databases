# Teacher's:
# https://colab.research.google.com/drive/1ytC02TuG4VnHKTLJ2F7L1TvE2cwWYXL2
# Best one vvv
# https://colab.research.google.com/drive/1IdP7r8Q4MNtykXPvqrJv84C-jKuOx3zE

# Pythonic Python Pythonifies the Pythas.
import psycopg2
import sqlite3
import os

# Want to make connection then cursor, use cursor to execute query then
# get results
# Postgres requires password
temp_pass = os.environ.get('password')
# Don't even try
temp_user = os.environ.get('username')
host = 'salt.db.elephantsql.com'
dbnm = temp_user

pg_conn = psycopg2.connect(dbname=dbnm, user=temp_user,
                           password=temp_pass, host=host)

# Got cursor
pg_curs = pg_conn.cursor()

# Execute
pg_curs.execute(f'''
SELECT * FROM testy;
''')

# Get all the entries (if that's what fetchall REALLY does...)
# print(pg_curs.fetchall()[1])

sl_conn = sqlite3.connect('../module1-introduction-to-sql/rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

characters = sl_curs.execute('''
SELECT * FROM charactercreator_character;
''').fetchall()
# Checkout length and that single char
print(f'\nEntries:{len(characters)}\n{characters[0]}\n')

# Postgres wants different stuff than SQL
create_character_table = f'''
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
'''

pg_curs.execute(create_character_table)
show_tables = f'''
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema'
'''

pg_curs.execute(show_tables)
print(pg_curs.fetchall())

example_insert = f'''
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES
''' + str(characters[0][1:])
print(example_insert)

for character in characters:
    insert_character = f'''
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES
    ''' + str(characters[1:]) + ';'
    print(insert_character)

pg_curs.close()
