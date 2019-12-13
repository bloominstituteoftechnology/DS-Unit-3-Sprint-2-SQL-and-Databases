import psycopg2

dbname = 'zaddfkaj'
user = 'zaddfkaj'
password = 'PvcjNh59KEhsprLQnRCfJ0uAn2La90R9'
host = 'rajje.db.elephantsql.com'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

# how many survived?
curs.execute('SELECT COUNT(*) FROM peeps WHERE survived = 1;')
print(curs.fetchall())

# how many did the opposite of surviving?
curs.execute('SELECT COUNT(*) FROM peeps WHERE survived = 0;')
print(curs.fetchall())

# how many passengers in each class?
curs.execute('SELECT pclass, COUNT(*) FROM peeps GROUP BY pclass;')
print(curs.fetchall())

# god have mercy on my soul

# how many people in class 1 survived?
curs.execute('SELECT COUNT(*) FROM peeps WHERE pclass = 1 AND survived = 1')
print(curs.fetchall())

# how many people in class 1 didn't?
curs.execute('SELECT COUNT(*) FROM peeps WHERE pclass = 1 AND survived = 0')
print(curs.fetchall())

# how many people in class 2 survived?
curs.execute('SELECT COUNT(*) FROM peeps WHERE pclass = 2 AND survived = 1')
print(curs.fetchall())

# how many people in class 2 didn't?
curs.execute('SELECT COUNT(*) FROM peeps WHERE pclass = 2 AND survived = 0')
print(curs.fetchall())

# how many people in class 3 survived?
curs.execute('SELECT COUNT(*) FROM peeps WHERE pclass = 3 AND survived = 1')
print(curs.fetchall())

# how many people in class 3 didn't?
curs.execute('SELECT COUNT(*) FROM peeps WHERE pclass = 3 AND survived = 0')
print(curs.fetchall())

# okay, no more soul mercy

# average ages of survivors/others
curs.execute('SELECT survived, AVG(age) FROM peeps GROUP BY survived')
print(curs.fetchall())

# average ages of classes
curs.execute('SELECT pclass, AVG(age) FROM peeps GROUP BY pclass')
print(curs.fetchall())

# average fares of classes
curs.execute('SELECT pclass, AVG(fare) FROM peeps GROUP BY pclass')
print(curs.fetchall())

# average fares of survived/other
curs.execute('SELECT survived, AVG(fare) FROM peeps GROUP BY survived')
print(curs.fetchall())

# average spouses/siblings by survived/other
curs.execute('SELECT survived, AVG(sibspouse) FROM peeps GROUP BY survived')
print(curs.fetchall())

# average spouses/siblings by class
curs.execute('SELECT pclass, AVG(sibspouse) FROM peeps GROUP BY pclass')
print(curs.fetchall())

# average parents/children by survived/other
curs.execute('SELECT survived, AVG(parchil) FROM peeps GROUP BY survived')
print(curs.fetchall())

# average parents/children by class
curs.execute('SELECT pclass, AVG(parchil) FROM peeps GROUP BY pclass')
print(curs.fetchall())

# how many times does each name come up?
curs.execute('SELECT name, COUNT(*) FROM peeps GROUP BY name HAVING COUNT(*) > 1')
print(curs.fetchall()) # answer: 1

# how many married couples...
curs.execute('SELECT name FROM peeps WHERE sibspouse > 0')
peeps = [{
  'name': row[0],
  'last': row[0].split(' ')[-1],
  'pref': row[0].split(' ')[0]
} for row in curs.fetchall()]
peeps = list(filter(lambda x: x['pref'] == 'Mr.' or x['pref'] == 'Mrs.', peeps))
name_buck = {}
for p in peeps:
  if p['last'] not in name_buck:
    name_buck[p['last']] = []
  name_buck[p['last']].append(p)
name_buck2 = {}
for k in name_buck:
  if len(name_buck[k]) > 1:
    name_buck2[k] = name_buck[k]
marred = 0
for ln in name_buck2:
  mcount = 0
  wcount = 0
  for rec in name_buck2[ln]:
    if rec['pref'] == 'Mr.' :
      mcount += 1
    else:
      wcount += 1
  marred += min(mcount, wcount)
print(marred)

# all done that's enough
curs.close()
conn.commit()