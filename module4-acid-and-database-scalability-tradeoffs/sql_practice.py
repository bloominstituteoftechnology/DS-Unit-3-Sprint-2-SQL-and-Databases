import psycopg2

# Removed credentials
dbname = 'DBNAME'
user = 'USER'
password = 'PASS'
host = 'raja.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()
# How many passengers survived, and how many died?

query = """
SELECT COUNT(passenger_id)
FROM TITANIC
WHERE SURVIVED = 1;
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print(results, "survived.")

query = """
SELECT COUNT(passenger_id)
FROM titanic
WHERE SURVIVED = 0;
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print(results, "did not survive.")

# How many passengers were in each class?
for k in [1, 2, 3]:
    query = """
    SELECT COUNT(passenger_id)
    FROM TITANIC
    WHERE PCLASS = """ + str(k) + ";"
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results = pg_curs.fetchall()[0][0]
    print(results, "in class", k)

# How many passengers survived/died within each class?

for k in [1, 2, 3]:
    query = """
    SELECT COUNT(passenger_id)
    FROM TITANIC
    WHERE PCLASS = """ + str(k) + " AND survived = 1;"
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results = pg_curs.fetchall()[0][0]
    print(results, "survived in class", k)

    query = """
    SELECT COUNT(passenger_id)
    FROM TITANIC
    WHERE PCLASS = """ + str(k) + " AND survived = 0;"
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results = pg_curs.fetchall()[0][0]
    print(results, "died in class", k)

# What was the average age of survivors vs nonsurvivors?

query = """
SELECT AVG(age)
FROM titanic
WHERE survived = 1
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print("Average age of survivors: ", results)

query = """
SELECT AVG(age)
FROM titanic
WHERE survived = 0
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print("Average age of non-survivors: ", results)

# What was the average age of each passenger class?

for k in [1, 2, 3]:
    query = """
    SELECT AVG(age)
    FROM TITANIC
    WHERE PCLASS = """ + str(k) + ";"
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results = pg_curs.fetchall()[0][0]
    print("Average age of class " + str(k), results)


# What was the average fare by passenger class?

for k in [1, 2, 3]:
    query = """
    SELECT AVG(fare)
    FROM TITANIC
    WHERE PCLASS = """ + str(k) + ";"
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results = pg_curs.fetchall()[0][0]
    print("Average fare of class ", k, results)

# By survival?

query = """
SELECT AVG(fare)
FROM titanic
WHERE survived = 1
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print("Average fare of survivors: ", results)

query = """
SELECT AVG(fare)
FROM titanic
WHERE survived = 0
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print("Average fare of non-survivors: ", results)

# How many siblings/spouses aboard on average, by passenger class?

for k in [1, 2, 3]:
    query = """
    SELECT AVG(siblings_spouses)
    FROM TITANIC
    WHERE PCLASS = """ + str(k) + ";"
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results = pg_curs.fetchall()[0][0]
    print("Avg. # of siblings/spouses for class ", k, results)

# By survival?

query = """
SELECT AVG(siblings_spouses)
FROM titanic
WHERE survived = 1
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print("Avg. # of siblings/spouses for survivors: ", results)

query = """
SELECT AVG(siblings_spouses)
FROM titanic
WHERE survived = 0
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print("Avg. # of siblings/spouses for non-survivors: ", results)

#  How many parents/children aboard on average, by passenger class?
for k in [1, 2, 3]:
    query = """
    SELECT AVG(parents_children)
    FROM TITANIC
    WHERE PCLASS = """ + str(k) + ";"
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results = pg_curs.fetchall()[0][0]
    print("Avg. # of parents/children for class ", k, results)

# By survival?

query = """
SELECT AVG(parents_children)
FROM titanic
WHERE survived = 1
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print("Avg. # of parents/children for survivors: ", results)

query = """
SELECT AVG(parents_children)
FROM titanic
WHERE survived = 0
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print("Avg. # of parents/children for non-survivors: ", results)

# Do any passengers have the same name?
# Counts number of names and distinct names and subtracts:

query = """
SELECT (SELECT COUNT(distinct name)
FROM titanic)-(SELECT COUNT(name)
FROM titanic);
"""
pg_curs = pg_conn.cursor()
pg_curs.execute(query)
results = pg_curs.fetchall()[0][0]
print(results, "people have the same name.")

# (Bonus! Hard, may require pulling and processing with Python) How many
# married couples were aboard the Titanic? Assume that two people
# (one Mr. and one Mrs.) with the same last name and with at least 1
# sibling/spouse aboard are married couple.

# query = """

# """
# pg_curs = pg_conn.cursor()
# pg_curs.execute(query)
# results = pg_curs.fetchall()[0][0]
# print(results)
