# Imports
import psycopg2

# Set connection variables
dbname = 'itlfjtuh'
user = 'itlfjtuh'
password = 
host = 'rajje.db.elephantsql.com'

# Create postgreSQL connection and cursor
conn = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host
    )
curs = conn.cursor()


question = "How many passengers survived, and how many died?"
query = """SELECT survived, COUNT(*)
FROM titanic
GROUP BY survived;
"""
curs.execute(query)
survival = curs.fetchall()
print(question)
print(survival[0][1], 'passengers died')
print(survival[1][1], 'passengers survived')


question = 'How many passengers were in each class?'
query = """SELECT pclass as class, COUNT(*)
FROM titanic
GROUP BY class;
"""
curs.execute(query)
pclass = curs.fetchall()
first_class = pclass[0][1]
second_class = pclass[2][1]
third_class = pclass[1][1]
print(question)
print('First Class:', first_class,
      '\nSecond Class:', second_class,
      '\nThird Class:', third_class)


question = 'How many passengers survived/died within each class?'
query = """SELECT pclass as class, survived, COUNT(*)
FROM titanic
GROUP BY survived, class;
"""
curs.execute(query)
survive = curs.fetchall()
fcs = survive[5][2]
fcd = survive[1][2]
scs = survive[4][2]
scd = survive[2][2]
tcs = survive[3][2]
tcd = survive[0][2]
print(question)
print(
    'First Class Survived:', fcs,
    '\nFirst Class Died:', fcd,
    '\nSecond Class Survived:', scs,
    '\nSecond Class Died:', scd,
    '\nThird Class Survived:', tcs,
    '\nThird Class Died:', tcd
    )


question = 'What was the average age of survivors vs nonsurvivors?'
query = """SELECT AVG(age) || (CASE WHEN survived = 1
THEN ' was the average age of survivors'
ELSE ' was the average age of nonsurvivors' END)
FROM titanic
GROUP BY survived;
"""
curs.execute(query)
survived_age = curs.fetchall()
print(question)
print(survived_age)


question = 'What was the average age of each passenger class?'
query = """SELECT AVG(age) || (CASE WHEN pclass = 1
THEN ' = average age of first class'
WHEN pclass = 2 THEN ' = average age of second class'
ELSE ' = average age of third class' END)
FROM titanic
GROUP BY pclass
ORDER BY pclass;
"""
curs.execute(query)
age = curs.fetchall()
print(question)
print(age)


question = 'What was the average fare by passenger class?'
query = """SELECT AVG(fare) || (CASE WHEN pclass = 1
THEN ' = average fare of first class'
WHEN pclass = 2 THEN ' = average fare of second class'
ELSE ' = average fare of third class' END)
FROM titanic
GROUP BY pclass
ORDER BY pclass;
"""
curs.execute(query)
fare_by_class = curs.fetchall()
print(question)
print(fare_by_class)


question = 'What was the average fare by survival?'
query = """SELECT AVG(fare) || (CASE WHEN survived = 1
THEN ' = average fare of survivors'
ELSE ' = average fare of those who died' END)
FROM titanic
GROUP BY survived;
"""
curs.execute(query)
fare_by_survival = curs.fetchall()
print(question)
print(fare_by_survival)


question = """
How many siblings/spouses aboard on average,
by passenger class?
"""
query = """SELECT AVG(siblings_spouses_aboard) ||
(CASE WHEN pclass = 1 THEN ' = first class'
WHEN pclass = 2 THEN ' = second class'
ELSE ' = third class' END)
FROM titanic
GROUP BY pclass
ORDER BY pclass;
"""
curs.execute(query)
sibspouse_byclass = curs.fetchall()
print(question)
print(sibspouse_byclass)


question = '''
How many siblings/spouses aboard on average, by survival?
'''
query = """SELECT AVG(siblings_spouses_aboard) ||
(CASE WHEN survived = 1 THEN ' = survived'
ELSE ' = died' END)
FROM titanic
GROUP BY survived;
"""
curs.execute(query)
sibspouse_bysurvived = curs.fetchall()
print(question)
print(sibspouse_bysurvived)


question = '''
How many parents/children aboard on average, by passenger class?
'''
query = """SELECT AVG(parents_children_aboard) ||
(CASE WHEN pclass = 1 THEN ' = first class'
WHEN pclass = 2 THEN ' = second class'
ELSE ' = third class' END)
FROM titanic
GROUP BY pclass
ORDER BY pclass;
"""
curs.execute(query)
parchild_byclass = curs.fetchall()
print(question)
print(parchild_byclass)


question = '''
How many parents/children aboard on average, by survival?
'''
query = """SELECT AVG(parents_children_aboard) ||
(CASE WHEN survived = 1 THEN ' = survived'
ELSE ' = died' END)
FROM titanic
GROUP BY survived;
"""
curs.execute(query)
parchild_bysurvived = curs.fetchall()
print(question)
print(parchild_bysurvived)


question = 'Do any passengers have the same name?'
query = """SELECT COUNT(*)
FROM titanic"""
curs.execute(query)
total = curs.fetchall()[0][0]

query = """SELECT COUNT(DISTINCT name)
FROM titanic
"""
curs.execute(query)
unique = curs.fetchall()[0][0]

print('Total passengers:', total)
print('Uniqe passenger names:', unique)
print('No two passengers have the same name.')
