
import pandas as pd 
import sqlite3

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
conn 

cursor = conn.cursor()
# df = pd.read_csv('/Users/noahpovis/Desktop/Lambda Clones/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')
# df.to_sql('buddymove_holidayiq' , con=conn)

# - Count how many rows you have - it should be 249!
query = '''
    SELECT 
        COUNT(*) 
    FROM buddymove_holidayiq
    '''
result = cursor.execute(query).fetchall()
print(f'Number of rows are {result[0][0]}')
# - How many users who reviewed at least 100 `Nature` in the category also
#   reviewed at least 100 in the `Shopping` category?
query = '''
    SELECT 
        COUNT(*) 
    FROM buddymove_holidayiq
    WHERE buddymove_holidayiq.Nature >= 100 AND buddymove_holidayiq.Shopping >= 100
    '''
result = cursor.execute(query).fetchall()
print(f'{result[0][0]} users reviewed both Nature and Shopping categories over 100 times')
# - (*Stretch*) What are the average number of reviews for each category?
query = '''
SELECT
round(AVG(Nature),2) as Nature_Avg, round(AVG(Sports),2) as Sport_Avg, round(AVG(Religious),2) as Religion_Avg,
round(AVG(Theatre),2) as Theatre_Avg, round(AVG(Shopping)
        , 2) as Shopping_avg, round(AVG(Picnic),2) as Picnic_AVG
FROM (SELECT * FROM buddymove_holidayiq)
'''
results = cursor.execute(query).fetchall()

print(results)
