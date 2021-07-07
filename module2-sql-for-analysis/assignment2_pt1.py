import sqlite3
import pandas as pd

conn = sqlite3.connect('titanic.sqlite3')
cur = conn.cursor()

# Loading in data and cleaning it for good SQL schema
df = pd.read_csv('https://raw.githubusercontent.com/lechemrc/DS-Unit-3-Sprint\
-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv', index_col=0)

columns_dict = {'Survived':'survived', 'Pclass':'passenger_class',
                'Name':'name', 'Sex':'sex', 'Age':'age',
                'Siblings/Spouses Aboard':'siblings_spouses',
                'Parents/Children Aboard':'parents_children', 'Fare':'fare'}
df = df.rename(columns=columns_dict)
df.head()

df.to_sql('titanic', con=conn, if_exists='replace')

cur.execute('''
    PRAGMA table_info(titanic)
''')
print(cur.fetchall())

