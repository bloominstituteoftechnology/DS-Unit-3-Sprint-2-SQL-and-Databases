"""
Practicing SQL on the titanic DB hosted locally
"""

import sqlite3

conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# - How many passengers were in each class?
# - How many passengers survived/died within each class?
# - What was the average age of survivors vs nonsurvivors?
# - What was the average age of each passenger class?
# - What was the average fare by passenger class? By survival?
# - How many siblings/spouses aboard on average, by passenger class? By survival?
# - How many parents/children aboard on average, by passenger class? By survival?
# - Do any passengers have the same name?
# - (Bonus! Hard, may require pulling and processing with Python) How many married
#   couples were aboard the Titanic? Assume that two people (one `Mr.` and one
#   `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
#   a married couple.

# - How many passengers survived, and how many died?
pass_survived = """
SELECT COUNT(survived)
FROM titanic
WHERE survived = 1;
"""
results1 = execute_query(curs, pass_survived)
print(results1)

# how many died
pass_dead = """
SELECT COUNT(survived)
FROM titanic
WHERE survived = 0;"""

results2 = execute_query(curs, pass_dead)
print(results2)

# - How many passengers survived/died within each class?
pass_dead_class = """
SELECT COUNT(survived)
FROM titanic
WHERE survived = 1
GROUP BY pclass
ORDER BY pclass DESC; """

results3 = execute_query(curs, pass_dead_class)
print(results3)

pass_survive_class = """
SELECT COUNT(survived)
FROM titanic
WHERE survived = 0
GROUP BY pclass
ORDER BY pclass DESC; """

results4 = execute_query(curs, pass_survive_class)
print(results4)

# - What was the average age of survivors vs nonsurvivors?
avg_survivor = """
SELECT AVG(age)
FROM
(SELECT age, survived
FROM titanic
WHERE survived = 1);"""

results5 = execute_query(curs, avg_survivor)
print(results5)

avg_dead = """
SELECT AVG(age)
FROM
(SELECT age, survived
FROM titanic
WHERE survived = 0);"""

print(execute_query(curs, avg_dead))


