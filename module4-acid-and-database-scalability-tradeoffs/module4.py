#!/usr/bin/env python 
import psycopg2

"""setup pg db connection"""

params = {"dbname": "rtnktynj",
        'user': 'rtnktynj',
        'password': 'UDZgOFVupQwhuoyRcHtjVt9q1GK-XDtO',  ##need something better
        'host': 'ruby.db.elephantsql.com',
        'port': 5432}
"""
- How many passengers survived, and how many died?
- How many passengers were in each class?
- How many passengers survived/died within each class?
- What was the average age of survivors vs nonsurvivors?
- What was the average age of each passenger class?
"""
queries = {} # queries to answer question 
queries["COUNT_SURVIVED"] = f"""SELECT COUNT(*) as "Number of Survivors"
                    FROM titanic
                    WHERE "Survived" = 1
                    """
                                            
queries["COUNT_DIED"] =  f"""SELECT COUNT(*) as "Number of dead"
                    FROM titanic
                    WHERE "Survived" = 0
                    """

queries["COUNT_PASSENGERS_BY_CLASS"] =  f""" 
                            SELECT "Pclass" as "class",
                                COUNT(*) as "# passengers" 
                            FROM titanic
                            GROUP BY "Pclass"
                            """
                        
queries["COUNT_SURVIVED_BY_CLASS"] = f"""
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
queries["AVG_AGE_BY_CLASS"] = f"""SELECT "Pclass", AVG("Age") as "Average Age"
                        FROM titanic
                        GROUP BY "Pclass"
                        ORDER BY "Pclass";
                        """
queries["AVG_AGE_BY_SURVIVAL"] = f"""SELECT "Survived",AVG("Age")
                        FROM titanic
                        GROUP BY "Survived"
                        """
"""
- What was the average fare by passenger class? By survival?
"""
queries["AVG_FARE_BY_CLASS"] = """SELECT "Pclass" as "Class",
                               AVG("Fare") as "Average Fare"
                        FROM titanic
                        GROUP BY "Pclass"
                        ORDER BY "Pclass";
                        """
queries["AVG_FARE_BY_SURVIVED"] = """SELECT "Survived", 
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
queries["SIBLINGS_SPOUSES_AVG_BY_CLASS"] = """
                        SELECT "Pclass",
                                AVG("Siblings/Spouses Aboard") as "Siblings or Spouses"
                        FROM titanic
                        GROUP BY "Pclass"
                        ORDER BY "Pclass"
                        """
queries["SIBLINGS_SPOUSES_AVG_BY_SURVIVAL"] = """
                        SELECT "Survived",
                                AVG("Siblings/Spouses Aboard") as "Siblings or Spouses"
                        FROM titanic
                        GROUP BY "Survived"
                        """
queries["AVG_PARENTS_CHILDREN_BY_CLASS"] = """
                        SELECT "Pclass",
                            ROUND(AVG("Parents/Children Aboard"),2) as "Parents and Children"
                        FROM titanic
                        GROUP BY "Pclass"
                        ORDER BY "Pclass"
                        """
queries["ARE_ANY_NAMES_THE_SAME"] ="""
                SELECT CASE (select count("Name") FROM titanic) != (select count(distinct("Name")) from titanic) 
                            WHEN 't' THEN 'yes' 
                            ELSE 'no' 
                            END as "Duplicate names Exist?";
                        """
with psycopg2.connect(**params) as conn:     
    with conn.cursor() as curs:            # this code will auto commit if no exception
       # curs.execute(COUNT_PASSENGERS_BY_CLASS).fetchall()
        for name in queries:
            curs.execute(queries[name])
            result = curs.fetchall()     # list of tuples
            print(f"{name} : ")
            for x in result:             #iterate thru list print on new line
                print(f"{x}")
conn.close()
