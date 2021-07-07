#Installing psycopg2 if necessary
#!pip install psycopg2-binary

#importing libraries
import psycopg2
import sqlite3

#reviewing options and the help documentation
#dir(psycopg2)
#help(psycopg2.connect)

#DB Connection info from Elephent SQL
dbname = 'oqsgenkt'
user = 'oqsgenkt'
password = 'mwI4YXJFcNUVaDyQ7TjGP7KhXEIkZ-U9' #update with password here
host = 'salt.db.elephantsql.com'

#creating the connection object from our login credentials above
pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)

#creating the cursor object to interact with the database
pg_curs = pg_conn.cursor()

#example query from the test_table we made earlier in elephentsql GUI.
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()

#grabbing the rpg_db file from github
#!wget https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true

#relabelling it properly
#!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

# For this SQLite3 file, we'll make a new connection and cursor object
#loading the sqlite3 file via sqlite3 connection object
sl_conn = sqlite3.connect('rpg_db.sqlite3')

#creating the sqlite3 connection object
sl_curs = sl_conn.cursor()

#example query for sqlite3 query
sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall()

#getting the table schema from the sqlite3 database
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

#using the schema information above, creating the schema in elephentsql
#for the file transfer
# You simply follow each column and its output, (integer, float, whole number, etc)
# Triple quotes are needed for multi-line text (queries)
create_character_table = """
  CREATE TABLE charactercreator_character(
  character_id SERIAL PRIMARY KEY,
  name varchar(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
  );
"""

#executing the table creation
pg_curs.execute(create_character_table)

#the show table query for elephentsql
show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""

#executing the showtable query in elephentsql
pg_curs.execute(show_tables)

pg_curs.fetchall()

#writing all of the character creator table to the variable characters for transfer
characters = sl_curs.execute('SELECT * from charactercreator_character;').fetchall()

#example of the first entry
characters[0]

#converting the first entry into a string, BUT cutting out the first column
#which was the ID
str(characters[0][1:])

#creating an insert command for one character as an example:
example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity,wisdom)
VALUES """ + str(characters[0][1:]) + ";"

#printing the example
print(example_insert)

#looping to do this for all characters and actually execute to elephentsql
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity,wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)

#showing the table we just made in elephent sql
pg_curs.execute('SELECT * FROM charactercreator_character;')

#example to show everything has been updated to elephentsql!
pg_curs.fetchall()

#closing and commiting to save changes
pg_curs.close()
pg_conn.commit()

#now reopening the connection to check for errors
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * from charactercreator_character;')
pg_characters= pg_curs.fetchall()

#first row in sqlite
characters[0]

#first row in sqelephant
pg_characters[0]

# comparing the first two rows to see if they are the same

#writing to verify that entries all coppied over accurately!
# Using the zip function to put those two together
for character, pg_character in zip(characters,pg_characters):
  assert character == pg_character
