import sqlite3
import pandas as pd

url = 'https://raw.githubusercontent.com/tesseract314/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'

# Make dataframe
df = pd.read_csv(url)

# Make empty sql file
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# Make cursor
curs = conn.cursor()

# Add above dataframe/table to sql file
df.to_sql('review', conn)

# Count rows
total_rows = """  
SELECT COUNT(*) FROM review;
"""

# Rows where movie >= 100 and shopping >= 100
mov_shop = """
SELECT * FROM review
WHERE review.Nature >= 100 AND review.Shopping >=100;
"""

# Average of each category
cat_avgs = """
SELECT 
AVG(r.Sports),
AVG(r.Religious),
AVG(r.Nature),
AVG(r.Theatre),
AVG(r.Shopping),
AVG(r.Picnic)
FROM review AS r;
"""
