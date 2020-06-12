import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/britneh/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')

print(df.head(10))
print(df.shape)
import psycopg2

