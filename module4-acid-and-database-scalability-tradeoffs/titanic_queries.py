import psycopg2
from db import DBNAME, USER, PASSWORD, HOST

# connect to ElephantSQL database
pg_conn = psycopg2.connect(dbname=DBNAME,
                           user=USER,
                           password=PASSWORD,
                           host=HOST)
pg_curs = pg_conn.cursor()

# How many passengers survived, and how many died?
q1_surv = "SELECT COUNT(*) FROM titanic WHERE survived = 1;"
pg_curs.execute(q1_surv)
print("Number who survived:", pg_curs.fetchall()[0][0])

q1_die = "SELECT COUNT(*) FROM titanic WHERE survived = 0;"
pg_curs.execute(q1_die)
print("Number who died:", pg_curs.fetchall()[0][0])

# How many passengers were in each class?
q2_c1 = "SELECT COUNT(*) FROM titanic WHERE class = 1;"
pg_curs.execute(q2_c1)
print("Number in first class:", pg_curs.fetchall()[0][0])

q2_c2 = "SELECT COUNT(*) FROM titanic WHERE class = 2;"
pg_curs.execute(q2_c2)
print("Number in second class:", pg_curs.fetchall()[0][0])

q2_c3 = "SELECT COUNT(*) FROM titanic WHERE class = 3;"
pg_curs.execute(q2_c3)
print("Number in third class:", pg_curs.fetchall()[0][0])

# How many passengers survived/died within each class?
q3_c1 = "SELECT COUNT(*) FROM titanic WHERE class = 1 AND survived = 1;"
pg_curs.execute(q3_c1)
print("Number who survived in first class:", pg_curs.fetchall()[0][0])

q3_c2 = "SELECT COUNT(*) FROM titanic WHERE class = 2 AND survived = 1;"
pg_curs.execute(q3_c2)
print("Number who survived in second class:", pg_curs.fetchall()[0][0])

q3_c3 = "SELECT COUNT(*) FROM titanic WHERE class = 3 AND survived = 1;"
pg_curs.execute(q3_c3)
print("Number who survived in third class:", pg_curs.fetchall()[0][0])

# What was the average age of survivors vs nonsurvivors?
q4_surv = "SELECT AVG(age) FROM titanic WHERE survived = 1;"
pg_curs.execute(q4_surv)
print("Average age of survivors:", pg_curs.fetchall()[0][0])

q4_die = "SELECT AVG(age) FROM titanic WHERE survived = 0;"
pg_curs.execute(q4_die)
print("Average age of diers:", pg_curs.fetchall()[0][0])

# What was the average age of each passenger class?
for i in range(1, 4):
    query = f"SELECT AVG(age) FROM titanic WHERE class = {i};"
    pg_curs.execute(query)
    print(f"Average age of class {i}:", pg_curs.fetchall()[0][0])

# What was the average fare by passenger class? By survival?
for i in range(1, 4):
    query = f"SELECT AVG(fare) FROM titanic WHERE class = {i};"
    pg_curs.execute(query)
    print(f"Average fare of class {i}:", pg_curs.fetchall()[0][0])

for i in [0, 1]:
    query = f"SELECT AVG(fare) FROM titanic WHERE survived = {i};"
    pg_curs.execute(query)
    stat = "survivors"
    if i == 0:
        stat = "diers"
    print(f"Average fare among {stat}:", pg_curs.fetchall()[0][0])

# How many siblings/spouses aboard on average by passenger class? By survival?
for i in range(1, 4):
    query = f"SELECT AVG(sibspouse) FROM titanic WHERE class = {i};"
    pg_curs.execute(query)
    print(f"Average sibs/spice of class {i}:", pg_curs.fetchall()[0][0])

for i in [0, 1]:
    query = f"SELECT AVG(sibspouse) FROM titanic WHERE survived = {i};"
    pg_curs.execute(query)
    stat = "survivors"
    if i == 0:
        stat = "diers"
    print(f"Average sibs/spice among {stat}:", pg_curs.fetchall()[0][0])

# How many parents/children aboard on average by passenger class? By survival?
for i in range(1, 4):
    query = f"SELECT AVG(parentchild) FROM titanic WHERE class = {i};"
    pg_curs.execute(query)
    print(f"Average parent/child of class {i}:", pg_curs.fetchall()[0][0])

for i in [0, 1]:
    query = f"SELECT AVG(parentchild) FROM titanic WHERE survived = {i};"
    pg_curs.execute(query)
    stat = "survivors"
    if i == 0:
        stat = "diers"
    print(f"Average parent/child among {stat}:", pg_curs.fetchall()[0][0])

# Do any passengers have the same name?
q9_tot = "SELECT COUNT(*) FROM titanic;"
pg_curs.execute(q9_tot)
total = pg_curs.fetchall()[0][0]
q9_dist = "SELECT COUNT(DISTINCT name) FROM titanic;"
pg_curs.execute(q9_dist)
distinct = pg_curs.fetchall()[0][0]
if total == distinct:
    print("All passengers had different names.")

# How many married couples were aboard the Titanic?
# get married women as list of tuples
q10 = "SELECT name FROM titanic WHERE name LIKE 'Mrs.%' AND sibspouse > 0"
pg_curs.execute(q10)
mrs = pg_curs.fetchall()
# women's names are formatted as 'mrs. [husband's given] (maiden name) surname
# ASIDE from Lizzie Faunthorpe, who doesn't have her husband's given names
# but there's no other Faunthorpes on board so let's not worry about her

# get adult men as list of tuples
q11 = "SELECT name FROM titanic WHERE name LIKE 'Mr.%' AND sibspouse > 0;"
pg_curs.execute(q11)
mr = pg_curs.fetchall()

# it's not actually necessary to make the list of men, so that's commented
# but it's good to look at for validation
# no woman shares her surname with multiple men, but some share them with
# unrelated men, so first name check is necessary
# men = []
couples = 0
for woman in mrs:
    # husbands = []
    surname = woman[0].split()[len(woman[0].split())-1]
    fname = woman[0].split()[1]
    for man in mr:
        if surname == man[0].split()[len(man[0].split())-1] and fname == man[0].split()[1]:
            # husbands.append(man[0])
            couples += 1
    # men.append(husbands)

print("Number of couples:", couples)
