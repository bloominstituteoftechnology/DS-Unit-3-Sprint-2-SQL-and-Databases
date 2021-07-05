import sqlite3
import pandas as pd
import sys

orig = sys.stdout
f = open('buddymove_answers.txt', 'a+')
sys.stdout = f

CSV_PATH = 'buddymove_holidayiq.csv'

df = pd.read_csv(CSV_PATH)
df = df.rename({'User Id': 'user_id'}, axis=1)

DB_PATH = 'buddymove_holidayiq.sqlite3'

db = sqlite3.connect(DB_PATH)
df.to_sql('buddymove_holidayiq', db,
           index_label='id')
curs = db.cursor()



q1 = curs.execute('select count(id) from buddymove_holidayiq').fetchone()[0]
print('How many rows?' , "\n", q1, "\n", "~"*40 )


q2 = curs.execute('''select count(user_id) from buddymove_holidayiq
                            where Shopping>99 and Nature>99''').fetchone()[0]
print(q2, 'rated both at least 100' , "\n", "~"*40)


cats = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']

for cat in cats:
    mean = curs.execute('select avg('+cat+')from buddymove_holidayiq').fetchone()[0]
    print( cat , '\n' , mean, '\n', '~'*10 )

sys.stdout = orig
f.close()