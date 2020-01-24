import psycopg2
import sqlite3

dbname = 'itlfjtuh'
user = 'itlfjtuh'
# password =
host = 'rajje.db.elephantsql.com'

# Create connection and cursor
pg_conn = psycopg2.connect(
    dbname=dbname, user=user,
    password=password, host=host
    )
pg_curs = pg_conn.cursor()

# Create table
create_table_statement = """
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""

pg_conn.commit()
pg_curs.execute(create_table_statement)

# Insert data into table
insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""

pg_curs.execute(insert_statement)
pg_conn.commit()

# Query new data
query = "SELECT * FROM test_table;"
pg_curs.execute(query)
look_at_data = pg_curs.fetchall()
print(look_at_data)

# Create RPG data connection and cursor
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Extract data
get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()

# Transform data
create_character_table = """
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
"""

pg_curs.execute(create_character_table)
pg_conn.commit()

# Insert data into table
for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(characters[0][1:]) + ";"
    pg_curs.execute(insert_character)
pg_conn.commit()

# Print table
pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5')
character_table = pg_curs.fetchall()
print(character_table)
