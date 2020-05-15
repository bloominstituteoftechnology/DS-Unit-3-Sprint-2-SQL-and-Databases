# Titanic Query Practice
# Module 4, Sprint 3
# Michael Toce

question_list = ["How many passengers survived, and how many died?","How many passengers were in each class?","How many passengers survived/died within each class?","What was the average age of survivors vs nonsurvivors?","What was the average age of each passenger class?","What was the average fare by passenger class? By survival?","How many siblings/spouses aboard on average, by passenger class? By survival?","How many parents/children aboard on average, by passenger class? By survival?","Do any passengers have the same name?"]

import os
import sqlite3
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv


# load in environmnet variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PW = os.getenv("DB_PW", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

gres_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)

gres_curs = gres_conn.cursor()
##----------------------------------------------------------------------------------------------------------------------
# 1. How many passengers survived, and how many died?
##----------------------------------------------------------------------------------------------------------------------

col1 = ["Survived", "count"]
q1 = '''
select
    "Survived",
    count("Survived")
from
    titanic
group by
	"Survived"
    '''

##----------------------------------------------------------------------------------------------------------------------
# 2. How many passengers were in each class?
##----------------------------------------------------------------------------------------------------------------------

col2 = ["Pclass", "count"]
q2 = '''
select
	"Pclass",
    count("Pclass")
from
    titanic
group by
	"Pclass"
'''

##----------------------------------------------------------------------------------------------------------------------
# 3. How many passengers survived/died within each class?
##----------------------------------------------------------------------------------------------------------------------
col3 = ["Pclass", "Survived", "count"]
q3 = '''
select
	"Pclass",
    "Survived",
    count("Survived")
from
    titanic
group by
	"Pclass", "Survived"
'''
##----------------------------------------------------------------------------------------------------------------------
# 4. What was the average age of survivors vs nonsurvivors?
##----------------------------------------------------------------------------------------------------------------------
col4 = ["Survived", "avg_age"]
q4 = '''
select
	"Survived",
    AVG("Age") as "avg_age"
from
    titanic
group by
	"Survived"
order by 
    "Survived"
'''

##----------------------------------------------------------------------------------------------------------------------
# 5. What was the average age of each passenger class?
##----------------------------------------------------------------------------------------------------------------------
col5 = ["Pclass", "Survived", "avg_age"]
q5 = '''
select
	"Pclass",
	"Survived",
    AVG("Age") as "avg_age"
from
    titanic
group by
	"Pclass", "Survived"
order by
    "Pclass", "Survived"
'''

##----------------------------------------------------------------------------------------------------------------------
# 6. What was the average fare by passenger class? What was average fare by survival?
##----------------------------------------------------------------------------------------------------------------------
col6 = ["Pclass", "Survived", "avg_fare"]
q6 = '''
select
	"Pclass",
	"Survived",
    AVG("Fare") as "avg_fare"
from
    titanic
group by
	"Pclass", "Survived"
'''

##----------------------------------------------------------------------------------------------------------------------
# 7. How many siblings/spouses aboard on average, by passenger class? By survival?
##----------------------------------------------------------------------------------------------------------------------
col7 = ["Pclass", "Survived", "avg_siblings_spouses"]
q7 = '''
select
	"Pclass",
	"Survived",
    AVG("Siblings/Spouses Aboard") as "avg_siblings_spouses"
from
    titanic
group by
	"Pclass", "Survived"
order BY
	"Pclass", "Survived"
'''

##----------------------------------------------------------------------------------------------------------------------
# 8. How many parents/children aboard on average, by passenger class? By survival?
##----------------------------------------------------------------------------------------------------------------------
col8 = ["Pclass", "Survived", "avg_parents_children"]
q8 = '''
select
	"Pclass",
	"Survived",
    AVG("Parents/Children Aboard") as "avg_parents_children"
from
    titanic
group by
	"Pclass", "Survived"
order BY
	"Pclass", "Survived"
'''
##----------------------------------------------------------------------------------------------------------------------
# 9. Do any passengers have the same name?
##----------------------------------------------------------------------------------------------------------------------
col9 = ["Name", "unique_name_desc"]
q9 = '''
select
	"Name",
	count(distinct "Name") as "unique_name_desc"
from
    titanic
group BY
	"Name"
order BY
	"unique_name_desc" desc
limit
    5
'''
question_list = ["How many passengers survived, and how many died?","How many passengers were in each class?","How many passengers survived/died within each class?","What was the average age of survivors vs nonsurvivors?","What was the average age of each passenger class?","What was the average fare by passenger class? By survival?","How many siblings/spouses aboard on average, by passenger class? By survival?","How many parents/children aboard on average, by passenger class? By survival?","Do any passengers have the same name?"]
col_header_list = [col1, col2, col3, col4, col5, col6, col7, col8, col9]

query_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
c=1
from tabulate import tabulate
# for c in range(len(query_list)):
#     result = gres_curs.execute(query_list[c])
#     results = gres_curs.fetchall()
#     print(question_list[c])
#     # turn into df before printing
#     results_df = pd.DataFrame(results, columns = col_header_list[c])
#     print(tabulate(results_df, headers='keys', tablefmt='psql', showindex=False))
#     print('\n')

def sql_queries_nice_output(questions, column_headers, queries):
    '''
    Takes in a list of questions, column headers, and SQL queries and prints nice, formatted output

    Input:
    question_list (list) of (str)  --  questions to answer with queries
    column_headers_list (list) of (lists) with (str)  --  column headers from tables in SQL
    queries (list) of (str)  --  query strings with SQL code used for data analysis

    Output:
    Multiple DataFrames with neat, tabulated output
    '''
    c = 1
    for c in range(len(query_list)):
        result = gres_curs.execute(query_list[c])
        results = gres_curs.fetchall()
        print(question_list[c])
        # turn into df before printing
        results_df = pd.DataFrame(results, columns = col_header_list[c])
        print(tabulate(results_df, headers='keys', tablefmt='psql', showindex=False))
        print('\n')
sql_queries_nice_output(question_list, col_header_list, query_list)
