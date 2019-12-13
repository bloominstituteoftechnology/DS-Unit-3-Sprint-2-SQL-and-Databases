import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

df.to_sql('df', conn, if_exists = 'replace')

"""Count number of rows"""
print(pd.read_sql_query('SELECT COUNT(*) FROM df;', conn))

"""
How many users who reviewed at least 100 Nature in the category also reviewed
at least 100 in the Shopping category?
"""
print(pd.read_sql_query('SELECT COUNT(*) FROM df WHERE Nature >= 100 AND Shopping >=100;', conn))
