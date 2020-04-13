
# import appropriate modules
import pandas as pd
import sqlite3

# Read in the data from the local file path or website
df = pd.read_csv('C:/Users/dougcohen/Repos/Unit-3/DS-Unit-3-Sprint-2-SQL-and-\
Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')
print(df.shape) # print the shape to ensure we have right rows and columns
print(df.head()) # print the head to ensure right format

# Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
conn = sqlite3.connect("buddymove_holidayiq.sqlite3")

# Use df.to_sql() to insert the data into a new table 'review' in the SQLite3 
#. database
df.to_sql('review', conn)