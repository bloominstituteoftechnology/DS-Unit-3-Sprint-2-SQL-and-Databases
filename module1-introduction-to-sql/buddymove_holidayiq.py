import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('module1-introduction-to-sql/buddymove_holidayiq.csv')
engine = create_engine('sqlite://', echo=False)
df.to_sql('review', con=engine)
query = 'SELECT count(*) FROM review'
size = engine.execute(query).fetchall()
print(f'This file has {size[0][0]} rows.')
query2 = '''SELECT Nature, Shopping
            FROM review
            WHERE Nature>99 AND Shopping>99;'''
reviews = engine.execute(query2).fetchall()
print('The number of users that wrote 100 reviews for Shopping and Nature:',
      len(reviews))
