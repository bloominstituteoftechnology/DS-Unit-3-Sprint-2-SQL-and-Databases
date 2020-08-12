import pandas as pd
import sqlite3

pd.set_option('display.max_columns', 500)

# Create data frame
df = pd.read_csv('titanic.csv')
df = df.rename(columns={'Siblings/Spouses Aboard': 'Siblings_Spouses', 'Parents/Children Aboard': 'Parents_Children'})
print(df.head())
print(df.info())
print(df.describe())
# Create Table
conn = sqlite3.connect('Titanic.db')
c = conn.cursor()
c.execute(
    'CREATE TABLE TITANIC (Survived number, Pclass number, Name text,' \
    ' Sex text, Age float, Siblings_Spouses number,Parents_Children number, Fare float)')

df.to_sql('TITANIC', conn, if_exists='replace', index=False)

c.execute("SELECT * FROM TITANIC;")

for row in c.fetchall():
    print(row)
