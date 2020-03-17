import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
#print('CONNECTION: ', connection)
cursor = connection.cursor()
#print('CURSOR: ', cursor)

#
### QUESTIONS 
# 

# Question 1: 
print('QUESTION 1: How many total characters?')
query = """SELECT
	count(DISTINCT character_id) as character_count
FROM
	charactercreator_character;"""

# result = cursor.execute(query)
# print('RESULT: ', result)
result2 = cursor.execute(query).fetchall()
print('Total characters: ', result2)

# Question 2: How many of each subclass?
print('QUESTION 2: How many of each subclass?')
query = """SELECT
	count(DISTINCT character_ptr_id) as cleric_count
FROM
	charactercreator_cleric;"""

result2 = cursor.execute(query).fetchall()
print('Total clerics: ', result2)

query = """SELECT
	count(DISTINCT character_ptr_id) as fighter_count
FROM
	charactercreator_fighter;"""

result2 = cursor.execute(query).fetchall()
print('Total fighters: ', result2)

query = """SELECT
	count(DISTINCT character_ptr_id) as mage_count
FROM
	charactercreator_mage;"""

result2 = cursor.execute(query).fetchall()
print('Total mages: ', result2)

query = """SELECT
	count(DISTINCT character_ptr_id) as thief_count
FROM
	charactercreator_thief;"""

result2 = cursor.execute(query).fetchall()
print('Total thieves: ', result2)

query = """SELECT
	count(DISTINCT mage_ptr_id) as necromancer_count
FROM
	charactercreator_necromancer;"""

result2 = cursor.execute(query).fetchall()
print('Total necromancers: ', result2)

# Question 3: How many total items?






# All my queries are dumped down here
# 
# 
# 
# 
# 
# 
# 
# 
#####
# # # Q1: How many total characters are there?
# SELECT
# 	count(DISTINCT character_id) as character_count
# FROM
# 	charactercreator_character;

# # Q2 How many of each subclass?
# SELECT
# 	count(DISTINCT character_ptr_id) as cleric_count
# FROM
# 	charactercreator_cleric;

# SELECT
# 	count(DISTINCT character_ptr_id) as fighter_count
# FROM
# 	charactercreator_fighter;

# SELECT
# 	count(DISTINCT character_ptr_id) as mage_count
# FROM
# 	charactercreator_mage;

# SELECT
# 	count(DISTINCT character_ptr_id) as thief_count
# FROM
# 	charactercreator_thief;

# SELECT
# 	count(DISTINCT mage_ptr_id) as necromancer_count
# FROM
# 	charactercreator_necromancer;

# #

#

#

#

######