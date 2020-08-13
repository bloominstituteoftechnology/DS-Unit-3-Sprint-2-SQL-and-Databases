# How many passengers survived, and how many died?
# How many passengers were in each class?
# How many passengers survived/died within each class?
# What was the average age of survivors vs nonsurvivors
# What was the average age of each passenger class?
# What was the average fare by passenger class? By survival?
# How many siblings/spouses aboard on average, by passenger class?By survival?
# How many parents/children aboard on average, by passenger class? By survival?
# Do any passengers have the same name? (Bonus! Hard, may require pulling and processing with Python) How
# many married couples were aboard the Titanic? Assume that two people (one Mr. and one Mrs.) with the same last name
# and with at least 1 sibling/spouse aboard are a married couple.

import sqlite3


def connect_to_db(db_name='Titanic.db'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# Queries
GET_TOTAL_SURVIVORS = """
    SELECT SUM(Survivor) AS TOTAL_SURVIVORS
    FROM (SELECT Name, COUNT(*) AS Survivor
    FROM TITANIC
    WHERE Survived = 1
    GROUP BY Name);
    """

GET_TOTAL_DEATHS = """
SELECT SUM(DIED) AS DEATHS
FROM (SELECT Name, COUNT(*) AS DIED
FROM TITANIC
WHERE Survived = 0
GROUP BY Name);
"""

GET_SURVIVED_DIED_PER_CLASS = """
SELECT Pclass, COUNT(Survived) as SURVIVED_OR_DIED_PER_CLASS
FROM TITANIC
GROUP BY Pclass;
"""
GET_AVG_AGE_SURVIVOR = """
SELECT AVG(Survivor_Age) FROM(SELECT Name, COUNT(*) AS Survivor, Age  AS Survivor_Age
FROM TITANIC WHERE Survived = 1 GROUP BY Name);
"""

GET_AVG_AGE_DEATH = """
SELECT AVG(Death_Age) FROM( SELECT Name, COUNT(*) AS DEATH, Age as Death_Age
FROM TITANIC WHERE Survived = 0 GROUP BY Name);
"""
GET_AVG_AGE_CLASS ="""
SELECT Pclass, Avg(Age) AS Avg_Age_Class
FROM TITANIC
GROUP BY Pclass;
"""

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    total_survivors = execute_query(curs, GET_TOTAL_SURVIVORS)
    print('Total survivors', total_survivors)

    total_deaths = execute_query(curs, GET_TOTAL_DEATHS)
    print('Total deaths', total_deaths)

    survived_died_per_class = execute_query(curs, GET_SURVIVED_DIED_PER_CLASS)
    print('Get survived or Died Per Class', survived_died_per_class)

    avg_age_survivor = execute_query(curs, GET_AVG_AGE_SURVIVOR)
    print('Average Age SURVIVOR', avg_age_survivor)

    avg_age_death = execute_query(curs, GET_AVG_AGE_DEATH)
    print('Average Age of Deaths', avg_age_death)

    avg_age_class = execute_query(curs, GET_AVG_AGE_CLASS)
    print('Average Age of Passenger Class', avg_age_class)


