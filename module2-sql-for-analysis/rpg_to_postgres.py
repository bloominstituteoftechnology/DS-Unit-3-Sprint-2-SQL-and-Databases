# https://github.com/jacobpad/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module2-sql-for-analysis/Unit_3_Sprint_2_Module_2_follow_along.ipynb
import psycopg2
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values
import sqlite3
import wget

load_dotenv() # look in the .env file for env vars, and add them to the env

DB_NAME= os.getenv("DB_NAME", default="oops")
DB_USER= os.getenv("DB_USER", default="oops")
DB_PASSWORD= os.getenv("DB_PASSWORD", default="oops")
DB_HOST= os.getenv("DB_HOST", default="oops")



# COPPIED FROM ABOVE IN THE HELP SECTION EXCEPT I ADDED HOST
pg_conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) # pg means POSTGRES
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')


print("1. PG_CONNECTION:\n", pg_conn)
print('\n')

# CURSOR ALLOWS US TO USE A DB
pg_curs = pg_conn.cursor()
print("2. PG_CURS:\n", pg_curs)
print('\n')

# EXECUTE A QUERY WITH LINE 2, FETCH THE RESULTS WITH LINE 3
pg_curs.execute('SELECT * FROM test_table;')
print('3. SELECT * FROM test_table;\n', pg_curs.fetchall())
print('\n')

# MAKE A CONNECTION VIA SQLITE3 (DOESN'T REQUIRE USERNAME/PASSWORD)
DB_FILE_PATH = 'DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3'
sl_conn = sqlite3.connect(DB_FILE_PATH)
print('4. SL_CONN\n', sl_conn)
print('\n')

# AFTER MAKING CONNECTION, MAKE A CURSOR
sl_curs = sl_conn.cursor()
print('5. SL_CURS\n',sl_curs,'\n\n')
print('\n')

# wget.download('https://github.com/jacobpad/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true')
# # LET'S EXECUTE A QUERY TO DOUBLE CHECK
# # QUERY CHECKS THE NUMBER OF CHARACTERS IN DATABASE
# sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character;').fetchall()
# # .fetchall() works on sqlite3

# SAVE THE CHARACTERS & INFO 
characters = sl_curs.execute('SELECT * FROM charactercreator_character;').fetchall()
print('6. SELECT * FROM charactercreator_character;\n',characters)
print('\n')

# SEE FIRST CHARACTER
print('7. See first character\n',characters[0])
print('\n')

# SEE LAST CHARACTER
print('8. See last character\n',characters[-1])
print('\n')

# GET USFUL INFORMATION ABOUT THE TABLE
# PASSING THE TABLE, WE GET 
# COLUMN NAMES, DATATYPE, AND MORE
# FOR EXAMLE - 'character_id' COLUMN IS AN 'integer'
see = sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()
print('9. See usful info about charactercreator_character table:\n',see)
print('\n')

# CREATE THE QUERY FOR THE TABLE TO RUN IN POSTGRESQL
create_character_table = """
DROP TABLE charactercreator_character;
  CREATE TABLE IF NOT EXISTS charactercreator_character (
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
create_character_table
print('10. create_character_table query\n', create_character_table)
print('\n')

# RUN THE QUERY TO CREATE THE TABLE IN POSTGRES
pg_curs.execute(create_character_table)
print('11. If this outputs, table was successfully created')
print('\n')

# DOUBLE CHECK TO MAKE SURE IT WORKED
#   FIRST CREATE A QUERY TO SHOW US
show_tables = """
  SELECT * 
  FROM pg_catalog.pg_tables
  WHERE schemaname != 'pg_catalog'
  AND schemaname != 'information_schema';
"""
print('12. show_table query\nDOUBLE CHECK TO MAKE SURE IT WORKED FIRST CREATE A QUERY TO SHOW US', show_tables)
print('\n')

# EXECUTE THE QUERY ABOVE
pg_curs.execute(show_tables)
print('13. If this outputs, query was successfully run')
print('\n')


# RUN FETCHALL TO SEE IT
print('14. RUN FETCHALL TO SEE IT\n',pg_curs.fetchall())
# Yep, there's the charactercreator_character table
print('\n')
print('--- Yep, it worked, see, charactercreator_character is a thing now\n')
print('\n')

# THIS IS THE CURRENT FORM IT'S IN AND IT'S NOT HOW WE WANT IT TO BE
print('15. THIS IS THE CURRENT FORM IT\'S IN AND IT\'S NOT HOW WE WANT IT TO BE\n',characters[0])
print('\n')

# TURN IT INTO A STRING AND SLICE AWAY THE FIRST COLUMN
print('16. TURN IT INTO A STRING AND SLICE AWAY THE FIRST COLUMN\n',str(characters[0][1:]))
print('\n')

# EXAMPLE INSERT
example_insert = """
  INSERT INTO charactercreator_character
  (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
  VALUES """ + str(characters[0][1:]) + ';'
print('17. example_insert\n', example_insert)
print('\n')

# MAKE A LOOP TO ADD ALL AT ONCE INSTEAD OF ADDING ONE BY ONE
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
  pg_curs.execute(insert_character) # THIS LINE IN THE FOR LOOP ALLOWS THE QUERY 
                                    # TO ADD A ROW 
print('18. MAKE A LOOP TO ADD ALL AT ONCE INSTEAD OF ADDING ONE BY ONE')
print('for character in characters:')
print('  insert_character = """')
print('  INSERT INTO charactercreator_character')
print('  (name, level, exp, hp, strength, intelligence, dexterity, wisdom)')
print('  VALUES """ + str(character[1:]) + \';\'')
print('pg_curs.execute(insert_character)')
print('\n')

# SEE THE TABLE
pg_curs.execute('SELECT * FROM charactercreator_character;')
see = pg_curs.fetchall()
print('19. See it all\n',see)
print('\n')




print('\n')
print('\n')
# COMMIT AND CLOSE
pg_curs.close()
pg_conn.commit()
# print('\n')
