import psycopg2
import sqlite3
import pandas as pd
import numpy as np

# from the CSV file get the headers
with open('titanic.csv') as file:
    line = file.readline().strip().split(',')
headers = [x.strip() for x in list(line)]

"""use pandas to infer datatypes
"""
df = pd.read_csv('titanic.csv')
cols = df.dtypes
dtypes_to_pg = {np.dtype('int64'): 'smallint',
                np.dtype('object'): 'TEXT',  # names are stupid long!
                np.dtype('float64'): 'float8'}
cols = cols.map(dtypes_to_pg)
 # now we have series of column names and pgsql dtypes


"""setup pg db """

# We need to make a create statement for PostgreSQL that captures these types


def sql_create_table(tableName, ntind):
    """ generate CREATE statement given some data
        using the pandas index from above
    """
    sql = (f"CREATE TABLE IF NOT EXISTS {tableName} ( "
           f"{tableName}_id SERIAL PRIMARY KEY"
           )
    for i in range(0, ntind.shape[0]):
        sql += f", \"{ntind.index[i]}\" {ntind[i]}"
    sql += ");"
    return sql


SQL_CREATE_TABLE = sql_create_table('titanic', cols)  # CREATE TABLE SQL


def sqlite_get_table(table):
    return f'SELECT * FROM {table};'


def list_to_string(l):
    """take a python and return as string 
    with all values in double quotes for 
    column headers
    """
    start = ''
    for x in l:
        start += f"\"{str(x)}\","
    start = start.rstrip(',')
    return start


def list_to_string(l):
    """take a python and return as string 
    with all values in doubble quotes for
    SQL """
    start = ''
    for x in l:
        start += f"\"{str(x)}\","
    start = start.rstrip(',')
    return start


def list_to_string1(l):
    """take a python and return as string 
    formated for VALUES
    """
    start = ''
    for x in l:
        start += f"""'{x.replace("'", "")}',""" if isinstance(x,str) else f"{str(x)},"
    start = start.rstrip(',')
    return start


def sql_insert_lines(tableName, data):  
    """taking a dataframe for the values, provide fr"""
    HEADERS = list_to_string(data.columns.tolist()) 
    sql = (f"INSERT INTO {tableName} "
               f"({HEADERS}) " # column list
               f" VALUES "
              )
    for i in range(0,data.shape[0]):                #iterate over lines in df
        line  = data.iloc[i][0:].tolist()
        VALUES = list_to_string1(line)
        sql +=  f"({VALUES}),"               #add 1 values block for each line 
    sql = sql.rstrip(',') 
    return sql
SQL_INSERT_ALL_ROWS = sql_insert_lines('titanic',df)  # last line


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
"""
- What was the average fare by passenger class? By survival?
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
"""
AVG_FARE_BY_CLASS = """SELECT "Pclass as "Class",
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