import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# load csv to dataframe
CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')
df = pd.read_csv(CSV_FILE_PATH)
# print(df.head())
# print(df.columns)
# print(df.dtypes)
# print(df.values)
# i'm not sure if I do some data cleansing before taking care of sql thing

# Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("dbname"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    host=os.getenv("host")
)
# A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()

# Drop the table if exist
cur.execute('DROP TABLE IF EXISTS Titanic;')

# CREATE TABLE query
query_create = """CREATE TABLE Titanic (
    Survived            INT,
    Pclass              INT,
    Name                varchar(120),
    Sex                 varchar(10),
    Age                 INT,
    SiblingsSpouses     INT,
    ParentsChildren     INT,
    Fare                INT);
"""
cur.execute(query_create)


# for Robert's code
for row in df.values:
    # print(tuple(row))
    cur.execute("""
        INSERT INTO Titanic
        (Survived, Pclass, Name, Sex, Age, SiblingsSpouses, ParentsChildren, Fare)
        VALUES %s;
    """, row)
conn.commit()
# print('@@@@\n')
# print(tuple(df.values))
# print('@@@@\n')
# cur.executemany("""INSERT INTO Titanic VALUES %s;""",
#                 (tuple(df.values)))
print(cur.execute('SELECT * FROM Titanic'))
# # df.to_sql('Titanic', conn, if_exists='replace', index=False)
