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

from sqlalchemy import create_engine
url = 'postgres://famiawbc:iA7gkgbluCi-KqWnRub3CHAbKQcB1Geb@rajje.db.elephantsql.com:5432/famiawbc'
engine=create_engine(url, echo=False)


# df = pd.read_csv('titanic.csv')
# df.to_sql("titanic", con=engine, if_exists="replace", index=False)

gres_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)

gres_curs = gres_conn.cursor()

query1 = '''
select
    "Survived",
    count("Sex") as "sexcount"
from
    titanic
where
    "Survived" = 1
group by
    "Survived"
'''

q1 = gres_curs.execute(query1)
results = gres_curs.fetchall()

print(results)
# records = df.to_records(index=False)

# result = list(records)
# # print(result)
# # breakpoint()

# df_list = [list(row) for row in df.itertuples(index=False)] 

# gres_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)

# gres_curs = gres_conn.cursor()

# create_table = '''
# create table if not exists titanic_table2(
#     Survived INTEGER PRIMARY KEY,
#     Pclass  INTEGER,
#     Name    varchar(100),
#     Sex   varchar(10),
#     Age  INTEGER,
#     Siblings_Spouses_Aboard INTEGER,
#     Parents_Children_Aboard INTEGER,
#     Fare FLOAT
# )
# '''
# # actually create the table
# gres_curs.execute(create_table)
# # commit the created table
# gres_conn.commit()

# # get_first_table = '''
# # select *
# # from titanic_table
# # '''
# # q1 = gres_curs.execute(get_first_table).fetchall()

# # insertion query string
# insertion_query = f"INSERT INTO titanic_table2 (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare) VALUES %s"
# # use insertion query above and q1 (first query), to insert table into postgresql
# execute_values(gres_curs, insertion_query, df_list)
# gres_conn.commit()
# gres_curs.close()
# gres_conn.close()
