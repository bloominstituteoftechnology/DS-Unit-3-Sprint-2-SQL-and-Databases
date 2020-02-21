import os
import psycopg2
from dotenv import load_dotenv

# Connect to the database
load_dotenv()

TITANIC_NAME = os.getenv("TITANIC_NAME")
TITANIC_USER = os.getenv("TITANIC_USER")
TITANIC_PASS = os.getenv("TITANIC_PASS")
HOST = os.getenv("HOST")

connection = psycopg2.connect(
    dbname=TITANIC_NAME,
    user=TITANIC_USER,
    password=TITANIC_PASS,
    host=HOST
    )
cursor = connection.cursor()

# Explore data
print("-------------------")
print('1. How many passengers survived, and how many died?')
query = 'SELECT survived, COUNT(*) FROM titanic GROUP BY survived;'
cursor.execute(query)
result = cursor.fetchall()
died = result[0][1]
survived = result[1][1]
print(f'{survived} passengers survived, and {died} died.')
print("-------------------")

print('2. How many passengers were in each class?')
query = 'SELECT pclass, COUNT(*) FROM titanic GROUP BY pclass;'
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(f'Class {row[0]}: {row[1]} passengers')
print("-------------------")

print('3. How many passengers survived/died within each class?')
query = """SELECT pclass, survived, COUNT(*)
    FROM titanic
    GROUP BY pclass, survived
    ORDER BY pclass, survived;"""
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    if row[1]==0:
        print(f'{row[2]} passengers died in class {row[0]}')
    else:
        print(f'{row[2]} passengers survived in class {row[0]}')
print("-------------------")

print('4. What was the average age of survivors vs nonsurvivors?')
query = 'SELECT survived, AVG(age) FROM titanic GROUP BY survived;'
cursor.execute(query)
result = cursor.fetchall()
died = result[0][1]
survived = result[1][1]
print(f'The average age of survivors: {survived:.0f}')
print(f'The average age of nonsurvivors: {died:.0f}')
print("-------------------")

print('5. What was the average age of each passenger class?')
query = 'SELECT pclass, AVG(age) FROM titanic GROUP BY pclass;'
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(f'Class {row[0]}: {row[1]:.0f}')
print("-------------------")

print('6. What was the average fare by passenger class?')
query = 'SELECT pclass, AVG(fare) FROM titanic GROUP BY pclass;'
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(f'Class {row[0]}: {row[1]:.0f}')
print("-------------------")

print('7. What was the average fare by passenger survival?')
query = 'SELECT survived, AVG(fare) FROM titanic GROUP BY survived;'
cursor.execute(query)
result = cursor.fetchall()
died = result[0][1]
survived = result[1][1]
print(f'The average fare for survivors was: {survived:.0f}')
print(f'The average fare for nonsurvivors was: {died:.0f}')
print("-------------------")

print('8. How many siblings/spouses aboard on average, by passenger class?')
query = 'SELECT pclass, AVG(siblings_spouses_aboard) FROM titanic GROUP BY pclass;'
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(f'Class {row[0]}: {row[1]:.0f} siblings/spouses aboard')
print("-------------------")

print('9. How many siblings/spouses aboard on average, by survival?')
query = 'SELECT survived, AVG(siblings_spouses_aboard) FROM titanic GROUP BY survived;'
cursor.execute(query)
result = cursor.fetchall()
died = result[0][1]
survived = result[1][1]
print(f'Survivors: {survived:.0f} siblings/spouses aboard')
print(f'Nonsurvivors: {died:.0f} siblings/spouses aboard')
print("-------------------")

print('10. How many parents/children aboard on average, by passenger class?')
query = 'SELECT pclass, AVG(parents_children_aboard) FROM titanic GROUP BY pclass;'
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(f'Class {row[0]}: {row[1]:.0f} parents/children aboard')
print("-------------------")

print('11. How many parents/children aboard on average, by survival?')
query = 'SELECT survived, AVG(parents_children_aboard) FROM titanic GROUP BY survived;'
cursor.execute(query)
result = cursor.fetchall()
died = result[0][1]
survived = result[1][1]
print(f'Survivors: {survived:.0f} parents/children aboard')
print(f'Nonsurvivors: {died:.0f} parents/children aboard')
print("-------------------")

print('12. Do any passengers have the same name?')
query1 = 'SELECT COUNT(name) FROM titanic;'
query2 = 'SELECT COUNT(DISTINCT name) FROM titanic;'
cursor.execute(query1)
total_names = cursor.fetchall()[0][0]
cursor.execute(query2)
distinct_names = cursor.fetchall()[0][0]
duplicate_names = total_names - distinct_names
if duplicate_names == 0:
    print('All passengers have distinct names')
else:
    print(f'{duplicate_names} names are duplicates')
print("-------------------")

# BONUS QUESTION TO DO