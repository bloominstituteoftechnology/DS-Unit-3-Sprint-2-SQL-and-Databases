"""
Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite). With PostgreSQL, answer the following:

- How many passengers survived, and how many died?
- How many passengers were in each class?
- How many passengers survived/died within each class?
- What was the average age of survivors vs nonsurvivors?
- What was the average age of each passenger class?
- What was the average fare by passenger class? By survival?
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.
"""

import psycopg2
import sqlite3

pg_conn = psycopg2.connect("dbname=postgres user=postgres password={secret}")
pg_curs = pg_conn.cursor()


query_survived = """
    SELECT survived_true,
    survived_false
    FROM (SELECT COUNT(survived)
    FROM titanic
    WHERE survived = 1) AS survived_true, 
    (SELECT COUNT(survived)
    FROM titanic
    WHERE survived = 0) AS survived_false;
    """
pg_curs.execute(query_survived)
survived = pg_curs.fetchall()
print("The number of passengers that survived: {}, didn't survive: {}"
    .format(survived[0][0][1:4], survived[0][1][1:4]))


query_total_class = """
    SELECT COUNT(pclass)
    FROM titanic
    GROUP BY pclass;
    """
pg_curs.execute(query_total_class)
total_class = pg_curs.fetchmany(3)
print("The number of passengers per class is: 1.- {}, 2.- {}, 3.- {}"
    .format(total_class[0][0], total_class[1][0], total_class[2][0]))


query_class_survived = """
    SELECT pclass,
    COUNT(survived) FILTER(WHERE survived = 1) as survive_true,
    COUNT(survived) FILTER(WHERE survived = 0) as survive_false
    FROM titanic
    GROUP BY pclass
    ORDER BY pclass;
    """
pg_curs.execute(query_class_survived)
class_survived = pg_curs.fetchmany(3)
print("The number of passengers separated by class/survived/died is {}; {}; {}"
    .format(str(class_survived[0])[1:-1], str(class_survived[1])[1:-1],
        str(class_survived[2])[1:-1]))


query_avg_age_survived = """
    SELECT ROUND(AVG(age) FILTER(WHERE survived = 1)) as avg_age_survive_true,
    ROUND(AVG(age) FILTER(WHERE survived = 0)) as avg_age_survive_false
    FROM titanic;
    """
pg_curs.execute(query_avg_age_survived)
avg_age_survived = pg_curs.fetchall()
print("The average age of the passengers that survived: {}, didn't survive: {}"
    .format(avg_age_survived[0][0], avg_age_survived[0][1]))


query_avg_age_pclass = """
    SELECT ROUND(AVG(age) FILTER(WHERE pclass = 1)) as avg_age_pclass1,
    ROUND(AVG(age) FILTER(WHERE pclass = 2)) as avg_age_pclass2,
    ROUND(AVG(age) FILTER(WHERE pclass = 3)) as avg_age_pclass3
    FROM titanic;
    """
pg_curs.execute(query_avg_age_pclass)
avg_age_pclass = pg_curs.fetchall()
print("The average age per class is: 1.- {}, 2.- {}, 3.- {}"
    .format(avg_age_pclass[0][0], avg_age_pclass[0][1], avg_age_pclass[0][2]))


query_avg_fare_pclass = """
    SELECT pclass,
    ROUND(AVG(fare) FILTER(WHERE survived = 1)) as avg_fare_survived_true,
    ROUND(AVG(fare) FILTER(WHERE survived = 0)) as avg_fare_survived_false
    FROM titanic
    GROUP BY pclass
    ORDER BY pclass;
    """
pg_curs.execute(query_avg_fare_pclass)
avg_fare_pclass = pg_curs.fetchall()
print("The average fare separated by class/survived/died is {}; {}; {}"
    .format(str(avg_fare_pclass[0])[1:-1], str(avg_fare_pclass[1])[1:-1],
        str(avg_fare_pclass[2])[1:-1]))


query_sib_spouse_pclass_survived = """
    SELECT pclass,
    ROUND(COUNT(siblings_spouses_aboard) FILTER(WHERE survived = 1)) as sib_spouse_survived_true,
    ROUND(COUNT(siblings_spouses_aboard) FILTER(WHERE survived = 0)) as sib_spouse_survived_false
    FROM titanic
    GROUP BY pclass
    ORDER BY pclass;
    """
pg_curs.execute(query_sib_spouse_pclass_survived)
sib_spouse_pclass_survived = pg_curs.fetchall()
print("The number of sibblings and spouse separated by class/survived/died is {}; {}; {}"
    .format(str(sib_spouse_pclass_survived[0])[1:-1], 
        str(sib_spouse_pclass_survived[1])[1:-1],
        str(sib_spouse_pclass_survived[2])[1:-1]))


query_parents_children_pclass_survived = """
    SELECT pclass,
    ROUND(COUNT(parents_children_aboard) FILTER(WHERE survived = 1)) as parents_children_survived_true,
    ROUND(COUNT(parents_children_aboard) FILTER(WHERE survived = 0)) as parents_children_survived_false
    FROM titanic
    GROUP BY pclass
    ORDER BY pclass;
    """
pg_curs.execute(query_parents_children_pclass_survived)
parents_children_pclass_survived = pg_curs.fetchall()
print("The number of parents and children separated by class/survived/died is {}; {}; {}"
    .format(str(parents_children_pclass_survived[0])[1:-1], 
        str(parents_children_pclass_survived[1])[1:-1],
        str(parents_children_pclass_survived[2])[1:-1]))