import psycopg2
import sqlite3
import pandas as pd
import numpy as np


"""setup pg db and do insert"""

params = {"dbname": "rtnktynj",
        'user': 'rtnktynj',
        'password': 'UDZgOFVupQwhuoyRcHtjVt9q1GK-XDtO',  ##need something better
        'host': 'ruby.db.elephantsql.com',
        'port': 5432}

#SQL = "".join(open('titanic.db', 'r').readlines()[1:])

with psycopg2.connect(**params) as conn:     
    with conn.cursor() as curs:            # this code will auto commit if no exception
        curs.execute("DROP TABLE IF EXISTS titanic;")
        curs.execute(SQL_CREATE_TABLE)
        curs.execute(SQL_INSERT_ALL_ROWS)                   # create table

conn.close()
"""
- How many passengers survived, and how many died?
- How many passengers were in each class?
- How many passengers survived/died within each class?
- What was the average age of survivors vs nonsurvivors?
- What was the average age of each passenger class?
"""

COUNT_SURVIVED = f"""SELECT COUNT(*) as "Number of Survivors"
                    FROM titanic
                    WHERE = "Survived" 1
                    """
                                            
COUNT_DIED =  f"""SELECT COUNT(*) as "Number of dead"
                    FROM titanic
                    WHERE "Survived" = 0
                    """

COUNT_PASSENGERS_BY_CLASS =  f""" 
                            SELECT "Pclass" as "class",
                                COUNT(*) as "# passengers" 
                            FROM titanic
                            GROUP BY "Pclass"
                            """
                        
COUNT_SURVIVED_BY_CLASS = f"""
                            SELECT "Pclass" as "Class",
                                CASE "Survived"
                                    WHEN 1 THEN 'Survived'
                                    ELSE 'Perished'
                                    END AS "Survival",
                                COUNT(*) as "count" 
                            FROM titanic 
                            GROUP BY "Pclass", "Survived" 
                            ORDER BY "Pclass", "Survived";
                             """
AVG_AGE_BY_CLASS = f"""SELECT "Pclass", AVG("Age") as "Average Age"
                        FROM titanic
                        GROUP BY "Pclass"
                        ORDER BY "Pclass";
                        """
AVG_AGE_BY_SURVIVAL = f"""SELECT "Survived",AVG("Age")
                        FROM titanic
                        GROUP BY "Survived"
                        """
"""
- What was the average fare by passenger class? By survival?
"""
AVG_FARE_BY_CLASS = """SELECT "Pclass" as "Class",
                               AVG("Fare") as "Average Fare"
                        FROM titanic
                        GROUP BY "Pclass"
                        ORDER BY "Pclass";
                        """
AVG_FARE_BY_SURVIVED = """SELECT "Survived", 
                                AVG("Fare") as "Average Fare"
                        FROM titanic
                        GROUP BY "Survived"
                        ORDER BY "Survived";
                        """
"""
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
"""
SIBLINGS_SPOUSES_AVG_BY_CLASS = """
                        SELECT "PClass",
                                AVG("Siblings/Spouses Aboard") as "Siblings or Spouses"
                        FROM titanic
                        GROUP BY "Pclass"
                        """
SIBLINGS_SPOUSES_AVG_BY_SURVIVAL = """
                        SELECT "Survived",
                                AVG("Siblings/Spouses Aboard") as "Siblings or Spouses"
                        FROM titanic
                        GROUP BY "Survived"
                        """
PARENTS_CHILDREN_AVG_BY_CLASS = """
                        SELECT "Pclass",
                            ROUND(AVG("Parents/Children Aboard"),2) as "Parents and Children"
                        FROM titanic
                        GROUP BY "Pclass"
                        ORDER BY "Pclass"
                        """


