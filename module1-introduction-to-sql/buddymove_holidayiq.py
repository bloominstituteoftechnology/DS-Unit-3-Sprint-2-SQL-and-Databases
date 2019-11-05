import pandas as pd
import sqlite3
import warnings


warnings.simplefilter('ignore')
# I get a UserWarning that the space in "User Id" will not be changed when
# I convert to sqlite3. I don't care about this so I set it to ignore warnings.

df = pd.read_csv('buddymove_holidayiq.csv')
print(f'The shape of the dataset is {df.shape}')
nulls = 0
for i in range(len(df.columns)):
    col_nulls = df.isnull().sum()[i]
    nulls += col_nulls
    if col_nulls > 0:
        print(f'Column {df.columns[i]} has {nulls} missing values.')
if nulls == 0:
    print('This dataset has no missing values!')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', con=conn)
curs = conn.cursor()

print('Testing to see if the conversion to sqlite3 worked:')
query1 = 'SELECT COUNT(*) FROM review;'
output1 = curs.execute(query1).fetchone()
amount1 = output1[0]
print(f'After converting to sqlite3, the dataset contains {amount1} rows.')

query2 = 'SELECT COUNT(*) FROM review \
        WHERE Nature >= 100 AND Shopping >= 100;'
output2 = curs.execute(query2).fetchone()
amount2 = output2[0]
print(f'{amount2} users who reviewed at least 100 in the Nature category also reviewed at least 100 in the Shopping category.')

categories = df.columns.tolist()
categories.remove('User Id')

for category in categories:
    query3 = f'SELECT AVG({category}) FROM review;'
    output3 = curs.execute(query3).fetchone()
    amount3 = output3[0]
    print(f'The average number of reviews for category {category} is {amount3}.')
