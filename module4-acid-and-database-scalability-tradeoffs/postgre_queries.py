"""
Postgre queries
"""

import psycopg2
from password_example import postgre_password

dbname = 'gubyurua'
user = 'gubyurua'
host = 'salt.db.elephantsql.com'

conn = psycopg2.connect(dbname=dbname, user=user, password=postgre_password, host=host)
curs = conn.cursor()

print('Question 1: How many passengers survived, and how many died?')
query1 = 'SELECT COUNT(*) FROM titanic GROUP BY survived HAVING survived = false;'
query2 = 'SELECT COUNT(*) FROM titanic GROUP BY survived HAVING survived = true;'
curs.execute(query1)
answer_died = curs.fetchone()[0]
curs.execute(query2)
answer_survived = curs.fetchone()[0]
print(f'Answer: {answer_survived} passengers survived, and {answer_died} died.')
print(' ')

print('Question 2: How many passengers were in each class?')
query = 'SELECT pclass, COUNT(*) FROM titanic GROUP BY pclass;'
curs.execute(query)
answer = curs.fetchall()
print('Answer:')
for tup in answer:
    print(f'{tup[1]} passengers were in class {tup[0]}.')
print(' ')

print('Question 3: How many passengers survived/died within each class?')
query = 'SELECT pclass, survived, COUNT(*) FROM titanic GROUP BY pclass, survived ORDER BY pclass;'
curs.execute(query)
answer = curs.fetchall()
print('Answer:')
for tup in answer:
    if tup[1] is True:
        print(f'{tup[2]} passengers in class {tup[0]} survived.')
    else:
        print(f'{tup[2]} passengers in class {tup[0]} died.')
print(' ')

print('Question 4: What was the average age of survivors vs nonsurvivors?')
query1 = 'SELECT AVG(age) FROM titanic GROUP BY survived HAVING survived = true;'
query2 = 'SELECT AVG(age) FROM titanic GROUP BY survived HAVING survived = false;'
curs.execute(query1)
answer_survived = curs.fetchone()[0]
curs.execute(query2)
answer_died = curs.fetchone()[0]
print(f'Answer: The average age of survivors was {answer_survived}; that of nonsurvivors was {answer_died}.')
print(' ')

print('Question 5: What was the average age of each passenger class?')
query = 'SELECT pclass, AVG(age) FROM titanic GROUP BY pclass;'
curs.execute(query)
answer = curs.fetchall()
print('Answer:')
for tup in answer:
    print(f'The average age of class {tup[0]} was {tup[1]}.')
print(' ')

print('Question 6: What was the average fare by passenger class? By survival?')
query1 = 'SELECT pclass, AVG(fare) FROM titanic GROUP BY pclass;'
query2 = 'SELECT AVG(fare) FROM titanic GROUP BY survived HAVING survived = true;'
query3 = 'SELECT AVG(fare) FROM titanic GROUP BY survived HAVING survived = false;'
curs.execute(query1)
ans_class = curs.fetchall()
print('Answer:')
for tup in answer:
    print(f'The average fare of class {tup[0]} was {tup[1]}.')
curs.execute(query2)
ans_lived = curs.fetchone()[0]
print(f'The average fare of survivors was {ans_lived}.')
curs.execute(query3)
ans_died = curs.fetchone()[0]
print(f'The average fare of nonsurvivors was {ans_died}.')
print(' ')

print('Question 7: How many siblings/spouses aboard on average, by passenger class? By survival?')
query1 = 'SELECT pclass, AVG(siblings_spouses_aboard) FROM titanic GROUP BY pclass;'
query2 = 'SELECT AVG(siblings_spouses_aboard) FROM titanic GROUP BY survived HAVING survived = true;'
query3 = 'SELECT AVG(siblings_spouses_aboard) FROM titanic GROUP BY survived HAVING survived = false;'
curs.execute(query1)
ans_class = curs.fetchall()
print('Answer:')
for tup in ans_class:
    print(f'The average siblings/spouses aboard of class {tup[0]} was {tup[1]}.')
curs.execute(query2)
ans_lived = curs.fetchone()[0]
print(f'The average siblings/spouses aboard of survivors was {ans_lived}.')
curs.execute(query3)
ans_died = curs.fetchone()[0]
print(f'The average siblings/spouses aboard of nonsurvivors was {ans_died}.')
print(' ')

print('Question 8: How many parents/children aboard on average, by passenger class? By survival?')
query1 = 'SELECT pclass, AVG(parents_children_aboard) FROM titanic GROUP BY pclass;'
query2 = 'SELECT AVG(parents_children_aboard) FROM titanic GROUP BY survived HAVING survived = true;'
query3 = 'SELECT AVG(parents_children_aboard) FROM titanic GROUP BY survived HAVING survived = false;'
curs.execute(query1)
ans_class = curs.fetchall()
print('Answer:')
for tup in ans_class:
    print(f'The average parents/children aboard of class {tup[0]} was {tup[1]}.')
curs.execute(query2)
ans_lived = curs.fetchone()[0]
print(f'The average parents/children aboard of survivors was {ans_lived}.')
curs.execute(query3)
ans_died = curs.fetchone()[0]
print(f'The average parents/children aboard of nonsurvivors was {ans_died}.')
print(' ')

print('Question 9: Do any passengers have the same name?')
query1 = 'SELECT COUNT(*) FROM titanic;'
query2 = 'SELECT COUNT(*) FROM (SELECT DISTINCT name FROM titanic) AS unique_names;'
curs.execute(query1)
total_names = curs.fetchone()[0]
curs.execute(query2)
unique_names = curs.fetchone()[0]
if total_names == unique_names:
    print('Answer: No passengers have the same name.')
else:
    print('Answer: Some passengers have the same name.')
print(' ')

print('Question 10: How many married couples were aboard the Titanic?')
print("Answer: I tried for some time but couldn't figure it out...")