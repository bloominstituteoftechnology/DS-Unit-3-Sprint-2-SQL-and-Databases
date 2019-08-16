import pandas as pd
import sqlite3

df = pd.read_csv('https://github.com/zevan07/DS-Unit-3-Sprint-2-SQL-and-Databases/raw/master/module1-introduction-to-sql/buddymove_holidayiq.csv')

conn = sqlite3.connect('/Users/oliver/Desktop/Lambda_Projects/DS-Unit-3-Sprint-2-SQL-and-Databases-master/module1-introduction-to-sql/buddymove_holidayiq.sqlite3')

# df.to_sql('reviews', conn)
# conn.commit()
# conn.close()

curs = conn.cursor()

review_count = 'SELECT COUNT(*) FROM reviews;'
print(curs.execute(review_count).fetchone())


nature_shopping_count = 'SELECT COUNT(*) FROM reviews WHERE Nature > 100 AND Shopping > 100'
print(curs.execute(nature_shopping_count).fetchall())
curs.close()