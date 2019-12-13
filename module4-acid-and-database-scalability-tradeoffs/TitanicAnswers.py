import pandas as pd

def query(x, db="titanic.sqlite3"):
    '''
    - This function connects to a database, 
    - establishes a cursor on top of the connection,
    - executes the SQL command = x
    - fetches the results from the SQL command and store it 
    in the variable ANSWER
    - Then commits and close the cursor and connection
    - then returns the result of the query.
    '''
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute(x)
    answer = curs.fetchall()
    curs.close()
    conn.commit()
    return answer

'''
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
'''

import psycopg2

def postgre(x):
    '''
    - Connects to elephant sql database
    - create a cursor on top of the connection
    - then commit the cursur to save it
    - then close the connection

    '''
    dbname = 'lqsujdux' 
    user = 'lqsujdux' 
    password =  'w7ih63BvRfpV_Mf9suEjW-6NmOGaTcP-'
    host =  'rajje.db.elephantsql.com'
    
    pg_conn = psycopg2.connect(dbname=dbname, user = user, password=password, host=host)
    pg_curs = pg_conn.cursor()
    pg_curs.execute(x)
    result = pg_curs.fetchall()
    pg_curs.close()
    pg_conn.commit()
    
    return result

all_tables = """ SELECT * FROM titanic
                LIMIT 10;
                
"""

postgre(all_tables)

# getting the column names
description = '''
SELECT column_name,data_type 
FROM information_schema.columns 
WHERE table_name = 'titanic';
'''
postgre(description)

# How many passengers survived, and how many died?

survived = """SELECT COUNT(*) FROM titanic
              Group by survived;"""


postgre(survived)
      
# How many passengers were in each class?

passengers = """SELECT COUNT(*) FROM titanic
                GROUP BY pclass;"""

postgre(passengers)

# How many passengers survived/died within each class?

survived_class = """SELECT pclass, survived,
                    COUNT('survived')
                    FROM titanic
                    GROUP BY survived, pclass;"""

# creating a dataframe to turn the returned result into a dataframe that is readable. 
sur_list = postgre(survived_class)

df = pd.DataFrame(sur_list, columns=['Pclass', 'Survived', 'Count'])

# What was the average age of survivors vs nonsurvivors?

survived_age = """SELECT survived, AVG(age)
                  FROM titanic
                  GROUP BY survived;
                  """

postgre(survived_age)

# What was the average age of each passenger class?

pclass_age = """SELECT pclass, AVG(age)
                  FROM titanic
                  GROUP BY pclass;
                  """

postgre(pclass_age)

# What was the average fare by passenger class? By survival?

avg_fare = """SELECT pclass, survived, AVG(fare)
              FROM titanic
              GROUP BY pclass, survived;
              """

postgre(avg_fare)

#How many siblings/spouses aboard on average, by passenger class? By survival?

sib_spo = """SELECT pclass, survived, ROUND(AVG(siblings_spouses_aboard), 0)
              FROM titanic
              GROUP BY pclass, survived;
              """

postgre(sib_spo)

#How many parents/children aboard on average, by passenger class? By survival?

par_child = """SELECT pclass, survived, ROUND(AVG(parents_children_aboard), 0)
              FROM titanic
              GROUP BY pclass, survived;
              """

postgre(par_child)

# Do any passengers have the same name?

same_name = """SELECT name, COUNT(*)
               FROM titanic
               GROUP BY name
               HAVING COUNT(*) > 1
              """

postgre(same_name)
# No, passengers don't have the same name. 