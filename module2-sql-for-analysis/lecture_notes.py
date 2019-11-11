
# help(psycopg2.connect) -- create a new database connection
import psycopg2

dbname = '********'       #same as user
user = '********'         #same as dbbase
password = '********'     #don't commit this to github!
host = '********'         #from SERVER type this in as string

pg_conn = psycopg2.connect(database=dbname, user=user, password=password, host=host)
# pg because it's made through postgress, not sqllite.


# A cursor is a temporary work area created in the system memory when a SQL statement is executed.
# A cursor contains information on a select statement and the rows of data accessed by it.
# This temporary work area is used to store the data retrieved from the database, and manipulate this data.

pg_curs = pg_conn.cursor()
# a nice thing about cursors is that we can execute sql queries off of them.


# The SQL EXECUTE command executes an SQL command and binds the result to 4D objects (arrays, variables or fields).
# A valid connection must be specified in the current process in order to execute this command.
pg_curs.execute('SELECT * FROM test_table')

#unlike in sqlite, we have to do that fetchall command seperately.
#fetchall() The method fetches all (or all remaining) rows of a query result set and returns a list of tuples.
#If no more rows are available, it returns an empty list.
pg_curs.fetchall()

# Need to get the database from github.
import sqlite3
# wget 'https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true'
# mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall()
sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character').fetchall()
# 5 less distinct names

# list of characters
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()

#We can see different entities in the list with list slicing. Can see len, etc.
print(characters[-1])
print(len(characters))

# Gives us all the info we need about the table.
sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

# Serial primary key instead of integer type in postgress.
create_character_table = """
    CREATE TABLE charactercreator_character(
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
#
# #Execute on top of postgress database.
# pg_curs.execute(create_character_table)

# Creating another query to make sure this worked.
show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
pg_curs.fetchall()

# I guess we're supposed to be able to enter stuff into ElephantSQL and it should be updating.
# Not sure how it works from my local machine to the site; do I have to upload to github or something?

#We're doing [1:] because postgress automatically gives it the serial number so we don't want to one from
#sqlite.
print(str(characters[0][1:]))

example_insert = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(characters[0][1:]) + ';'


# Repeats the character over and over for all of the characters.
for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ';'
    pg_curs.execute(insert_character)

# print(insert_character)
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_curs.fetchall()


pg_curs.close()
pg_conn.commit()
