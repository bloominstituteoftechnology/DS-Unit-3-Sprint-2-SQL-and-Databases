import psycopg2

dbname = 'yjbbntkp'
user = 'yjbbntkp'
password = 'euAG1JE7Wa6Fb_K9FVhQaU1Y3uLPgj9B'
host = 'salt.db.elephantsql.com' 

# PostgresQL setup
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# Query Survived
pg_curs.execute("SELECT COUNT(Survived) FROM iceberg WHERE Survived > 0 ;")
query_surv =  pg_curs.fetchall()[0][0]
print(f'Total Survived on the Titanic: {query_surv}')

# Query amount in each class
# 1st class
pg_curs.execute("SELECT COUNT(*) FROM iceberg WHERE pclass = 1;")
class_1 = pg_curs.fetchall()[0][0]
print(f'Total People in First Class: {class_1}')

# 2nd Class
pg_curs.execute("SELECT COUNT(*) FROM iceberg WHERE pclass = 2;")
class_2 = pg_curs.fetchall()[0][0]
print(f'Total People in Second Class: {class_2}')

# 3rd Class
pg_curs.execute("SELECT COUNT(*) FROM iceberg WHERE pclass = 3;")
class_3 = pg_curs.fetchall()[0][0]
print(f'Total People in Third Class: {class_3}')

# How many died in each class 
# 1st Class
pg_curs.execute("SELECT COUNT(*) FROM iceberg WHERE pclass = 1 AND survived = 1;")
class_1 = pg_curs.fetchall()[0][0]
print(f'Total People Survived in First Class: {class_1}')

# 2nd Class
pg_curs.execute("SELECT COUNT(*) FROM iceberg WHERE pclass = 2 AND survived = 2;")
class_1 = pg_curs.fetchall()[0][0]
print(f'Total People Survived in Second Class: {class_2}')

# 3rd Class
pg_curs.execute("SELECT COUNT(*) FROM iceberg WHERE pclass = 3 AND survived = 3;")
class_1 = pg_curs.fetchall()[0][0]
print(f'Total People Survived in Third Class: {class_3}')

# Average Age of Survivors
pg_curs.execute("SELECT AVG(age) FROM iceberg WHERE survived = 1;")
avg_age = pg_curs.fetchall()[0][0]
print(f'Average age of Survivors {avg_age}')

# Average Age of Non Survivors
pg_curs.execute("SELECT AVG(age) FROM iceberg WHERE survived = 0;")
avg_ded = pg_curs.fetchall()[0][0]
print(f'Average age of deceased {avg_ded}')

# Average Age in 1st Class
pg_curs.execute("SELECT AVG(age) FROM iceberg WHERE pclass = 1;")
avg_1 = pg_curs.fetchall()[0][0]
print(f'Average age of 1st Class {avg_1}')

# Average Age 2nd class
pg_curs.execute("SELECT AVG(age) FROM iceberg WHERE pclass = 2;")
avg_2 = pg_curs.fetchall()[0][0]
print(f'Average age of 2nd Class {avg_2}')

# Average Age 3rd Class
pg_curs.execute("SELECT AVG(age) FROM iceberg WHERE pclass = 3;")
avg_3 = pg_curs.fetchall()[0][0]
print(f'Average age of 3rd Class {avg_3}')

# Average fare paid by surviving 1st class
pg_curs.execute("SELECT AVG(fare) FROM iceberg WHERE survived = 1 GROUP BY pclass;")
fare = pg_curs.fetchall()
print(f'The average fare paid by each survived class - \n 1st:{fare[0][0]}\n 2nd:{fare[2][0]}\n 3rd:{fare[1][0]}')

# Average Sibling Spouses aboard by survived & class
pg_curs.execute("SELECT AVG(siblings_spouses_aboard) FROM iceberg WHERE survived = 1 GROUP BY pclass;")
avg_sib = pg_curs.fetchall()
print(f'The average siblings/spouses by each survived class - \n 1st:{avg_sib[0][0]}\n 2nd:{avg_sib[2][0]}\n 3rd:{avg_sib[1][0]}')

pg_curs.execute("SELECT AVG(parents_children_aboard) FROM iceberg WHERE survived = 1 GROUP BY pclass;")
avg_fam = pg_curs.fetchall()
print(f'The average siblings/spouses by each survived class - \n 1st:{avg_fam[0][0]}\n 2nd:{avg_fam[2][0]}\n 3rd:{avg_fam[1][0]}')

# Passengers with the exact same name 
pg_curs.execute("SELECT name, COUNT(*) FROM iceberg GROUP BY name HAVING COUNT(*) > 1;")
totes = pg_curs.fetchall()
print(f'Passengers that boarded with the EXACT same First/Last/Suffixes/Prefixes: {totes} aka None')

pg_conn.commit()
pg_conn.close()
