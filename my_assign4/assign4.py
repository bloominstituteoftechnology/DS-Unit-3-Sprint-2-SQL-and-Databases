# This is where we will do the postgresql
# queries on the titanic

import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")


connection = psycopg2.connect(dbname=DB_NAME , password=DB_PASSWORD, 
                                        user=DB_USER , host=DB_HOST)



p_cur = connection.cursor()

# Question 1 -- How many passengers survived, and how many died?

query1 = """
    SELECT --*
        survived
        ,count(distinct id_num)

    FROM titanic
    GROUP BY survived
"""

p_cur.execute(query1)
result = p_cur.fetchall()
print("The number of passengers surviving (1) and not (0) is: \n", result)

# Question 2 -- How many passengers were in each class?

quer2 = """
    SELECT --*
        titanic.pclass
        ,count(distinct titanic.id_num) as num_passengers
	
    FROM titanic
    GROUP BY titanic.pclass
"""
p_cur.execute(quer2)
result = p_cur.fetchall()
print("Question 2")
print("The number of passenger in each class is: \n", result)

# Question 3 -- How many passengers survived/died within each class?

query3 =  """
    SELECT --*
        titanic.pclass
        ,titanic.survived
        ,count(distinct titanic.id_num) as num_passengers
	
	
    FROM titanic
    GROUP BY titanic.pclass, titanic.survived
"""

p_cur.execute(query3)
result = p_cur.fetchall()
print("\nAnswer for question 3:\n", result)


# Question 4 -- What was the average age of survivors vs nonsurvivors?

query4 = """
    SELECT --*

        titanic.survived
        ,avg(titanic.age)
	
    FROM titanic
    GROUP BY  titanic.survived
"""
p_cur.execute(query4)
result = p_cur.fetchall()
print("\nThe answer for question 4 is: \n", result)

# Question 5 -- What was the average fare by passenger class? By survival?

query5 = """
    SELECT --*

        pclass
        ,survived
        ,AVG(fare)
        
        
    FROM titanic
    GROUP BY  pclass, titanic.survived
    ORDER BY pclass, survived
"""
p_cur.execute(query5)
result = p_cur.fetchall()
print("\nThe answer to question 5 is: \n", result)

# Question 6 -- How many siblings/spouses aboard on average, by passenger class? By survival?
query6 = """
    SELECT
        
        pclass,
        survived,
        avg(siblings_spouses_aboard) as avg_sibling_spouses
    FROM
        titanic
    GROUP BY
        pclass,
        titanic.survived
    ORDER BY
        pclass,
        survived
"""
p_cur.execute(  query6)
result = p_cur.fetchall()
print("\nAnswer to question 6: \n", result)

# Question 7 -- How many parents/children aboard on average, by passenger class? By survival?

query7 = """
    SELECT
        pclass,
        survived,
        avg(titanic.parents_children_aboard) as parent_and_children
    FROM
        titanic
    GROUP BY
        pclass,
        titanic.survived
    ORDER BY
        pclass,
        survived
"""

p_cur.execute(query7)
result = p_cur.fetchall()
print("\nThe answer to question 7 is: \n", result)

# Question 8 -- Do any passengers have the same name?

query8 = """
    SELECT  

	--IF SUBSTRING(titanic.name, from '[M][r][s][.]') = NULL THEN
	 count( distinct SUBSTRING(titanic.name from '\s[A-Z][a-z]*\s') )
	--SUBSTRING(titanic.name from [^m|M][^.)
	--END IF;
	

FROM titanic

"""
p_cur.execute(query8)
result = p_cur.fetchall()
print("This is my answer for the 8th question\n", result)
