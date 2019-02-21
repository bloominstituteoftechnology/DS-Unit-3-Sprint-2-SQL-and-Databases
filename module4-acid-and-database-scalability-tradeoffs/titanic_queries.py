import psycopg2 as pg
import pandas as pd

pg.connect

dbname = 'fyhefwlq'
user = 'fyhefwlq'
password = 'BuchWImOB1Fa68LH52tirHsWp3yc8mvF'
host = 'baasu.db.elephantsql.com'

conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
pg_cur = conn.cursor()


# How many passengers survived, and how many died?
def total_status():
    print(pd.read_sql_query("""SELECT CASE WHEN survived = 1
            THEN 'survived' ELSE 'died' END as status,
            COUNT(distinct person_id)
            FROM titanic
            GROUP BY 1;""", conn))


# How many passengers were in each class?
def classes():
    print(pd.read_sql_query("""SELECT pclass, COUNT(distinct person_id)
            FROM titanic
            GROUP BY pclass;""", conn))


# How many passengers survived/died within each class?
def status_classes():
    print(pd.read_sql_query("""SELECT pclass, CASE WHEN survived = 1
            THEN 'survived' ELSE 'died' END as status,
            COUNT(distinct person_id)
            FROM titanic
            GROUP BY 1,2;""", conn))


# What was the average age of survivors vs nonsurvivors?
def age_status():
    print(pd.read_sql_query("""SELECT CASE WHEN survived = 1 THEN 'survived' ELSE 'died' END as status,
            round(AVG(age)) as avg_age
            FROM titanic
            GROUP BY 1;""", conn))


# What was the average age of each passenger class?
def age_class():
    print(pd.read_sql_query("""SELECT pclass, round(AVG(age)) as avg_age
            FROM titanic
            GROUP BY pclass;""", conn))


# What was the average fare by passenger class? By survival?
def avg_fare_class():
    print(pd.read_sql_query("""SELECT pclass, AVG(fare) as avg_fare
            FROM titanic
            GROUP BY pclass;""", conn))


def avg_fare_status():
    print(pd.read_sql_query("""SELECT CASE WHEN survived = 1
            THEN 'survived' ELSE 'died' END as status,
            AVG(fare) as avg_fare
            FROM titanic
            GROUP BY 1;;""", conn))


# How many siblings/spouses aboard on average, by passenger class? By survival?
def sibspo_class():
    print(pd.read_sql_query("""SELECT pclass,
            AVG(siblings_spouses_aboard) as avg_sibling_spouse
            FROM titanic
            GROUP BY pclass;""", conn))


def sibspo_status():
    print(pd.read_sql_query("""SELECT CASE WHEN survived = 1
            THEN 'survived' ELSE 'died' END as status,
            AVG(siblings_spouses_aboard) as avg_sibling_spouse
            FROM titanic
            GROUP BY 1;""", conn))


# How many parents/children aboard on average, by passenger class? By survival?
def par_child_status():
    print(pd.read_sql_query("""SELECT CASE WHEN survived = 1 
            THEN 'survived' ELSE 'died' END as status,
            AVG(parents_children_aboard) as avg_parent_child
            FROM titanic
            GROUP BY 1;""", conn))


def par_child_status():
    print(pd.read_sql_query("""SELECT pclass,
            AVG(parents_children_aboard) as avg_parent_child
            FROM titanic
            GROUP BY pclass;""", conn))


# Do any passengers have the same name?
def par_child_class():
    print(pd.read_sql_query("""SELECT name, count(distinct person_id) as count
            FROM titanic
            GROUP BY 1
            HAVING count(distinct person_id) > 1;""", conn))


# (Bonus! Hard, may require pulling and processing with Python) How many
# married couples were aboard the Titanic? Assume that two people
# (one Mr. and one Mrs.) with the same last name and with at least
# 1 sibling/spouse aboard are a married couple.
def married_couples():
    print(pd.read_sql_query("""SELECT COUNT(DISTINCT l_name) as married_couples
            FROM (
            SELECT RIGHT(name, POSITION(' ' in REVERSE(name))) as l_name,
            COUNT(distinct person_id) as count
            FROM titanic
            WHERE siblings_spouses_aboard >= 1
            AND name NOT LIKE 'Miss%'
            GROUP BY 1
            HAVING COUNT(distinct person_id) > 1) x;""", conn))
