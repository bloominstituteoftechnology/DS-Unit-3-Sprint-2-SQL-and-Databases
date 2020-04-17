import os
import sqlite3


DB_FILEPATH = os.path.join(os.path.dirname(__file__),"rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

# Question 01 - How many total Characters are there?
question01 = 'How many total Characters are there?'
query01 = '''
SELECT 
	COUNT(character_id) AS character_count
FROM charactercreator_character
'''

# Question 02 - How many of each specific subclass?
question02 = 'How many of each specific subclass?'
query02 = '''
SELECT 
	COUNT(character_id) AS character_count
FROM charactercreator_character
'''

#question02 = 'How many of each specific subclass?'
#query02 = '''
#SELECT 
#	COUNT(character_id) AS character_count
#FROM charactercreator_character
#'''

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

#result2 = cursor.execute(query).fetchall()
#print("RESULT 2", result2)

'''
question_list = [question01,
               question02, 
               question03,
               question04,
               question05,
               question06,
               question07,
               question08]

query_list = [query01,
              query02,
              query03,
              query04,
              query05,
              query06,
              query07,
              query08]

for n in query_list:
'''

result_test = cursor.execute(query01).fetchall()
print(question01 + ':', str(result_test[0])
                        .replace(',', '')
                        .replace('(', '')
                        .replace(')', ''))

#print(str(result_test[0]).replace(',', '').replace('(', '').replace(')', ''))
    
#breakpoint()