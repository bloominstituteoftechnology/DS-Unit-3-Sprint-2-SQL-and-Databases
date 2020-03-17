import os
import sqlite3

query1 = """
SELECT
	count()
FROM review
"""

query2 = """
SELECT
count()
FROM review
WHERE Nature >= 100 AND Shopping >= 100
"""

query3 = """
SELECT
	avg(Sports) as avg_sports,
	avg(Religious) as avg_sports,
	avg(Nature) as avg_sports,
	avg(Theatre) as avg_sports,
	avg(Shopping) as avg_sports,
	avg(Picnic) as avg_sports
FROM review

"""

connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

print('--------------')

result1 = cursor.execute(query1).fetchall()
print('Count how many rows you have - it should be 249!')
print(result1[0][0])
print('--------------')

result2 = cursor.execute(query2).fetchall()
print('How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?')
print(result2[0][0])
print('--------------')

result3 = cursor.execute(query3).fetchall()
print('What are the average number of reviews for each category?')
print('Sports',result3[0][0])
print('Religious',result3[0][1])
print('Nature',result3[0][2])
print('Theatre',result3[0][3])
print('Shopping',result3[0][4])
print('Picnic',result3[0][5])
