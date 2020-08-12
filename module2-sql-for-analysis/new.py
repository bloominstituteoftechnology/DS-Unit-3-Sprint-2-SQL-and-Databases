import pandas as pd
import psycopg2
import sqlite3
"""change csv to sqlite"""
df = pd.read_csv("titanic.csv")
df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
              'Parents/Children Aboard', 'Fare']
# print(df)
#
#
# Connecting to the Elephant database
conn = psycopg2.connect(
                        database="put yours here",
                        user="same as above",
                        password="gimme dat passwordd", # Sensitive! Don't share/commit
                        host = 'isilo.db.elephantsql.com'
                        )
# print(conn)
#
#
# Connect to database
DB_FILEPATH = "titanic.sqlite3"
connection = sqlite3.connect(DB_FILEPATH)
# Make a Cursor
cursor = connection.cursor()
#
#
Passengers = cursor.execute("""
DROP TABLE IF EXISTS review;
CREATE TYPE GENDER AS ENUM ('male', 'female');
CREATE TABLE "passengers" (
    Survived INT NOT NULL,
    Pclass INT NOT NULL,
    Name  VARCHAR(75) NOT NULL,
    Sex GENDER NOT NULL,
    Age REAL NOT NULL,
    Siblings_Spouses_Aboard INT NOT NULL, 
    Parents_Children_Aboard INT NOT NULL,
    Fare REAL NOT NULL
);
""")
#
#
for row in df:
    cursor.execute(
                """
                    INSERT INTO 
                        passengers (
                            survived, 
                            name, 
                            pclass, 
                            sex, 
                            age, 
                            siblings_spouse_count, 
                            parents_children_count, 
                            fare
                        ) 
                    VALUES 
                        (
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s   
                        );
                """,
                (
                    row['Survived'],
                    row['Name'],
                    row['Pclass'],
                    row['Sex'],
                    row['Age'],
                    row['Siblings/Spouses Aboard'],
                    row['Parents/Children Aboard'],
                    row['Fare']
                )
    )
    print(df)
#
#
#
#
# (((( Remove Blockcode for the lines below ONLY when the above runs properly))))
# (((( Hopefully, I get a response before 8am from my TL to help with the minor))))
# (((( pd.read_csv('titanic.csv) error... see error below))))
# ((((     FileNotFoundError: [Errno 2] No such file or directory: 'titanic.csv'    ))))
#
#
#
#
# df_to_sql = df.to_sql('review_titanic', conn)
# cursor = conn.cursor()
# ### Count how many rows you have? Hint: 249
# query = """
#         SELECT COUNT(*)
#         FROM review_titanic
#         """
# query2 = """
#         SELECT COUNT(Survived)
#         FROM review_titanic
#         WHERE Survived = 1
#         AND Fare > AVG(Fare)
#         AND Sex = 'female'
#         """
# cursor.execute(query)
# result = cursor.fetchall()
# print("RESULT of Query:", result)  #> returns cursor objects w/o results (need to fetch)
# cursor.execute(query2)
# result2 = cursor.fetchall()
# print("RESULT of Query 2:", result2)
# conn.commit()
# curs.close()
# conn.close()