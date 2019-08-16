import psycopg2
import pandas as pd 

"""
Script queries titanic data from elephantSQL
"""

# Database info
dbname = 'jehgnrff'
user = 'jehgnrff'
password = '21Al2FjnMu8SMSi6q505r4qfFZ7JLGTO'
host = 'otto.db.elephantsql.com'

# Initalize connection and cursor to db 
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()


# Queries
query = 'SELECT COUNT(survived) FROM titanic WHERE survived = 1;'
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers survived')


query = 'SELECT COUNT(survived) FROM titanic WHERE survived = 0;'
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers died')


query = 'SELECT COUNT(pclass) FROM titanic WHERE pclass = 1;'
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 1')


query = 'SELECT COUNT(pclass) FROM titanic WHERE pclass = 2;'
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 2')


query = 'SELECT COUNT(pclass) FROM titanic WHERE pclass = 3;'
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 3')


query = '''
    SELECT COUNT(pclass) FROM titanic
    WHERE pclass = 1 AND survived = 1;
    '''
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 1 survied')


query = '''
    SELECT COUNT(pclass) FROM titanic
    WHERE pclass = 2 AND survived = 1;
    '''
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 2 survied')


query = '''
    SELECT COUNT(pclass) FROM titanic
    WHERE pclass = 3 AND survived = 1;
    '''
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 3 survied')


query = '''
    SELECT COUNT(pclass) FROM titanic
    WHERE pclass = 1 AND survived = 0;
    '''
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 1 died')


query = '''
    SELECT COUNT(pclass) FROM titanic
    WHERE pclass = 2 AND survived = 0;
    '''
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 2 died')


query = '''
    SELECT COUNT(pclass) FROM titanic
    WHERE pclass = 3 AND survived = 0;
    '''
pg_curs.execute(query)
print(pg_curs.fetchall()[0][0], 'passengers in class 3 survied')


query = '''
    SELECT AVG(age) FROM titanic
    WHERE survived = 1;
    '''
pg_curs.execute(query)
print('Average age of survivors:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(age) FROM titanic
    WHERE survived = 0;
    '''
pg_curs.execute(query)
print('Average age of casualties:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(age) FROM titanic
    WHERE pclass = 1;
    '''
pg_curs.execute(query)
print('Average age of class 1:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(age) FROM titanic
    WHERE pclass = 2;
    '''
pg_curs.execute(query)
print('Average age of class 2:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(age) FROM titanic
    WHERE pclass = 3;
    '''
pg_curs.execute(query)
print('Average age of class 3:', round(pg_curs.fetchall()[0][0], 2))

query = '''
    SELECT AVG(fare) FROM titanic
    WHERE pclass = 1;
    '''
pg_curs.execute(query)
print('Average fare of class 1:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(fare) FROM titanic
    WHERE pclass = 2;
    '''
pg_curs.execute(query)
print('Average fare of class 2:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(fare) FROM titanic
    WHERE pclass = 3;
    '''
pg_curs.execute(query)
print('Average fare of class 3:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(fare) FROM titanic
    WHERE survived = 0;
    '''
pg_curs.execute(query)
print('Average fare of deceased:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(siblings_spouses_aboard) FROM titanic
    WHERE pclass = 1;
    '''
pg_curs.execute(query)
print('Average siblings/spouses aboard for class 1:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(siblings_spouses_aboard) FROM titanic
    WHERE pclass = 2;
    '''
pg_curs.execute(query)
print('Average siblings/spouses aboard for class 2:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(siblings_spouses_aboard) FROM titanic
    WHERE pclass = 3;
    '''
pg_curs.execute(query)
print('Average siblings/spouses aboard for class 3:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(siblings_spouses_aboard) FROM titanic
    WHERE survived = 1;
    '''
pg_curs.execute(query)
print('Average siblings/spouses aboard for survivors:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(siblings_spouses_aboard) FROM titanic
    WHERE survived = 0;
    '''
pg_curs.execute(query)
print('Average siblings/spouses aboard for deceased:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(parents_children_aboard) FROM titanic
    WHERE pclass = 1;
    '''
pg_curs.execute(query)
print('Average parents/children aboard for class 1:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(parents_children_aboard) FROM titanic
    WHERE pclass = 2;
    '''
pg_curs.execute(query)
print('Average parents/children aboard for class 2:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(parents_children_aboard) FROM titanic
    WHERE pclass = 3;
    '''
pg_curs.execute(query)
print('Average parents/children aboard for class 3:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(parents_children_aboard) FROM titanic
    WHERE survived = 1;
    '''
pg_curs.execute(query)
print('Average parents/children aboard for survivors:', round(pg_curs.fetchall()[0][0], 2))


query = '''
    SELECT AVG(parents_children_aboard) FROM titanic
    WHERE survived = 0;
    '''
pg_curs.execute(query)
print('Average parents/children aboard deceased:', round(pg_curs.fetchall()[0][0], 2))

query = '''
    SELECT COUNT(total.nm) FROM
(SELECT a.first_name, count(*) as nm
FROM (SELECT split_part(name, ' ', 2) AS first_name
FROM titanic) as a
GROUP BY a.first_name
HAVING COUNT(*) > 1) as total
'''
pg_curs.execute(query)
print('Number of passengers who share a  first name with at least one other:', pg_curs.fetchall()[0][0])

pg_curs.close()
