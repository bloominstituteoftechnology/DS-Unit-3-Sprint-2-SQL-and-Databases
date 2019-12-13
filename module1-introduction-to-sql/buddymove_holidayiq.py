# IMPORT ZE DATA
import pandas as pd
df = pd.read_csv('buddymove_holidayiq.csv')
assert(df.shape[0] == 249)
assert(df.shape[1] == 7)
assert(df.isnull().sum().sum() == 0)

# PREPARE FOR ZE SQL
import sqlite3
khan = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = khan.cursor()

# FIRE ZE DATA! (BUT ONLY ZE ONCE!)
#df.to_sql('review', khan)

# how many rows do we have? (spoiler alert: 249)
runq = lambda q: curs.execute(q).fetchall()
assert(runq('''
  SELECT COUNT(`User Id`)
  FROM `review`
''')[0][0] == 249)

# how many users *who* reviewed 100+ Nature
# *also* reviewed 100+ Shopping?
print(runq('''
  SELECT COUNT(`User Id`)
  FROM `review`
  WHERE `Nature` > 99
    AND `Shopping` > 99;
''')[0][0])

# AU REVOIR, SHOSHANNA
curs.close()
khan.commit()