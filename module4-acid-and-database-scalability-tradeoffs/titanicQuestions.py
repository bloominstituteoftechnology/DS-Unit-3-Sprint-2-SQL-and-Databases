import psycopg2
dbname = 'REDACTED'
user = 'REDACTED'
password = 'REDACTED'
host = 'REDACTED'
pg_conn = psycopg2.connect(database=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

print("Titanic questions")
print("\nHow many passengers survived, and how many died? (Percentage survival)")
pg_curs.execute('SELECT AVG(survived) FROM titanic_set2;')
print(pg_curs.fetchall())

print("\nHow many passengers were in each class?")
pg_curs.execute(' \
SELECT pclass, COUNT(pclass) \
FROM titanic_set2 \
GROUP By pclass; \
')
print(pg_curs.fetchall())

print("\nHow many passengers survived/died within each class?")
print("Survived")
pg_curs.execute(' \
SELECT pclass, COUNT(survived) \
FROM titanic_set2 \
WHERE survived = 1 \
GROUP BY pclass \
ORDER BY pclass \
;')
print(pg_curs.fetchall())
print("Did not survive")
pg_curs.execute(' \
SELECT pclass, COUNT(survived) \
FROM titanic_set2 \
WHERE survived = 0 \
GROUP BY pclass \
ORDER BY pclass \
;')
print(pg_curs.fetchall())

print("\nWhat was the average age of survivors vs nonsurvivors?")
pg_curs.execute(' \
SELECT survived, AVG(age) \
FROM titanic_set2 \
GROUP BY survived \
;')
print(pg_curs.fetchall())

print("\nWhat was the average age of each passenger class?")
pg_curs.execute(' \
SELECT pclass, AVG(age) \
FROM titanic_set2 \
GROUP BY pclass \
ORDER BY pclass \
;')
print(pg_curs.fetchall())

print("\nWhat was the average fare by passenger class? By survival?")
print("By class")
pg_curs.execute(' \
SELECT pclass, AVG(fare) \
FROM titanic_set2 \
GROUP BY pclass \
ORDER BY pclass \
;')
print(pg_curs.fetchall())
print("By survival")
pg_curs.execute(' \
SELECT survived, AVG(fare) \
FROM titanic_set2 \
GROUP BY survived \
ORDER BY survived \
;')
print(pg_curs.fetchall())

print("\nHow many siblings/spouses aboard on average, by passenger class? By survival?")
print("By class")
pg_curs.execute(' \
SELECT pclass, AVG(siblingsspousesaboard) \
FROM titanic_set2 \
GROUP BY pclass \
ORDER BY pclass \
;')
print(pg_curs.fetchall())
print("By survival")
pg_curs.execute(' \
SELECT survived, AVG(siblingsspousesaboard) \
FROM titanic_set2 \
GROUP BY survived \
ORDER BY survived \
;')
print(pg_curs.fetchall())

print("\nHow many parents/children aboard on average, by passenger class? By survival?")
print("By class")
pg_curs.execute(' \
SELECT pclass, AVG(parentschildrenaboard) \
FROM titanic_set2 \
GROUP BY pclass \
ORDER BY pclass \
;')
print(pg_curs.fetchall())
print("By survival")
pg_curs.execute(' \
SELECT survived, AVG(parentschildrenaboard) \
FROM titanic_set2 \
GROUP BY survived \
ORDER BY survived \
;')
print(pg_curs.fetchall())

print("\nDo any passengers have the same name?")
print("Total names")
pg_curs.execute(' \
SELECT COUNT(name) \
FROM titanic_set2 \
;')
print(pg_curs.fetchall())
print("Total distinct names")
pg_curs.execute(' \
SELECT COUNT(DISTINCT name) \
FROM titanic_set2 \
;')
pg_curs.fetchall()
print(pg_curs.fetchall())
print("All names unique")

pg_curs.close()

"""
Output

Titanic questions

How many passengers survived, and how many died? (Percentage survival)
[(Decimal('0.38556933483652762120'),)]

How many passengers were in each class?
[(1, 216), (3, 487), (2, 184)]

How many passengers survived/died within each class?
Survived
[(1, 136), (2, 87), (3, 119)]
Did not survive
[(1, 80), (2, 97), (3, 368)]

What was the average age of survivors vs nonsurvivors?
[(0, 30.1385321100917), (1, 28.4083918128272)]

What was the average age of each passenger class?
[(1, 38.7889814815587), (2, 29.8686413042571), (3, 25.188747433238)]

What was the average fare by passenger class? By survival?
By class
[(1, 84.154687528257), (2, 20.6621831810993), (3, 13.7077075010452)]
By survival
[(0, 22.2085840951412), (1, 48.3954076976107)]

How many siblings/spouses aboard on average, by passenger class? By survival?
By class
[(1, Decimal('0.41666666666666666667')), (2, Decimal('0.40217391304347826087')), (3, Decimal('0.62012320328542094456'))]
By survival
[(0, Decimal('0.55779816513761467890')), (1, Decimal('0.47368421052631578947'))]

How many parents/children aboard on average, by passenger class? By survival?
By class
[(1, Decimal('0.35648148148148148148')), (2, Decimal('0.38043478260869565217')), (3, Decimal('0.39630390143737166324'))]
By survival
[(0, Decimal('0.33211009174311926606')), (1, Decimal('0.46491228070175438596'))]

Do any passengers have the same name?
Total names
[(887,)]
Total distinct names
[]
All names unique

"""