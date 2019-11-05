import pandas as pd
import psycopg2
from db import DBNAME, USER, PASSWORD, HOST

# load data from file
df = pd.read_csv('titanic.csv')

# connect to ElephantSQL database
pg_conn = psycopg2.connect(dbname=DBNAME,
                           user=USER,
                           password=PASSWORD,
                           host=HOST)
pg_curs = pg_conn.cursor()

# create enumerated type SEX
create_sex = """CREATE TYPE SEX AS ENUM ('male', 'female');"""
pg_curs.execute(create_sex)

create_titanic_table = """
    CREATE TABLE titanic (
        item_id SERIAL PRIMARY KEY,
        survived INT,
        class INT,
        name varchar(100),
        sex SEX,
        age INT,
        sibspouse INT,
        parentchild INT,
        fare DECIMAL(7, 4)
    );
"""
pg_curs.execute(create_titanic_table)

passengers = list(df.itertuples(index=False, name=None))

# iteratively add every passenger from the dataframe to the elephant
for passenger in passengers:
    if "'" in passenger[2]:  # handles the IRISH
        passenger = (passenger[0], passenger[1], passenger[2].replace("'", ''),
                     passenger[3], passenger[4], passenger[5], passenger[6],
                     passenger[7])
    current = str(passenger)
    insert_pass = f"""
        INSERT INTO titanic (survived, class, name, sex, age,
                             sibspouse, parentchild, fare)
        VALUES {current};
    """
    pg_curs.execute(insert_pass)

pg_curs.close()
pg_conn.commit()
