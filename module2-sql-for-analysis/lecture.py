import psycopg2
import sqlite3

db = 'bgpuyxgj'
user = 'bgpuyxgj'
password = 'V-Jx_5OuILdziMIe5MvVDu61OdhoWMCR'  # Don't commit!
host = 'raja.db.elephantsql.com'

conn = psycopg2.connect(dbname=db, user=user,
                        password=password, host=host)

curs = conn.cursor()

curs.execute('''SELECT * FROM test_table''')
print(curs.fetchall())

sq_conn = sqlite3.connect('rpg_db.sqlite3')
sq_curs = sq_conn.cursor()
characters = sq_curs.execute('''select * from charactercreator_character''')
characters = characters.fetchall()
print(characters[0])

create_character_table = '''
Create table character_creator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
    )
    '''
curs.execute(create_character_table)

curs.execute('''select * from character_creator_character''')
print(curs.fetchall())

# Loop over and insert results.
for result in characters:
    insert_result = '''
    INSERT INTO character_creator_character (
    name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    values''' + str(result[1:])
    curs.execute(insert_result)

conn.commit()

curs.execute('''select * from character_creator_character''')
query = curs.fetchall()
print(query)

print(query[0])
