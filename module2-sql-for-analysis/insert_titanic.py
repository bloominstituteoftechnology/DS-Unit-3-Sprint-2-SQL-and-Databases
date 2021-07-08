# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
# %%
import pandas as pd


# %%
df = pd.read_csv('module2-sql-for-analysis/titanic.csv')
df.Name = df.Name.replace("'", '', regex=True)


# %%
df.head()


# %%
df.shape


# %%
import psycopg2


# %%
pg_conn = psycopg2.connect(database=dbname, user=user, password=password, host=host)


# %%
pg_conn


# %%
import sqlite3


# %%
sl_conn = sqlite3.connect('module2-sql-for-analysis/titanic.sqlite3')


# %%
df.to_sql('titanic_set2',con=sl_conn,if_exists='replace')


# %%
sl_curs = sl_conn.cursor()


# %%
sl_curs.execute('SELECT COUNT(*) FROM titanic_set2;').fetchall()


# %%
sl_curs.execute('PRAGMA table_info(titanic_set2);').fetchall()


# %%
create_titanic_table = """
  CREATE TABLE titanic_set2 (
    index SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex sex,
    Age REAL,
    SiblingsSpousesAboard INT,
    ParentsChildrenAboard INT,
    Fare REAL
  );
"""


# %%
pg_curs = pg_conn.cursor()


# %%
pg_curs.execute('SELECT * FROM test_table;')


# %%
pg_curs.fetchall()


# %%



# %%
#pg_curs.execute("CREATE TYPE sex AS ENUM ('male', 'female');")


# %%
pg_curs.execute(create_titanic_table)


# %%
show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""


# %%
pg_curs.execute(show_tables)


# %%
pg_curs.fetchall()


# %%
allData = sl_curs.execute('SELECT * from titanic_set2;').fetchall()


# %%
len(allData)


# %%
allData[0]


# %%
allData[-1]


# %%
example_insert = """
INSERT INTO titanic_set2
(Survived, Pclass, Name, Sex, Age, SiblingsSpousesAboard, ParentsChildrenAboard, Fare)
VALUES """ + str(allData[1][1:]) + ';'


# %%
print(example_insert)


# %%
for theData in allData:
    insert_data="""
    INSERT INTO titanic_set2
    (Survived, Pclass, Name, Sex, Age, SiblingsSpousesAboard, ParentsChildrenAboard, Fare)
    VALUES """ + str(theData[1:]) + ';'
    print(insert_data)
    pg_curs.execute(insert_data)


# %%
pg_curs.execute('SELECT * FROM titanic_set2;')
pg_curs.fetchall()


# %%
pg_curs.close()
pg_conn.commit()


# %%


