
# Make a Connection
pg_conn = postgres_helper.create_postgres_connection(verbose=True)

# List top 10 titanic rows
query = 'SELECT * FROM titanic LIMIT 10;'
results = postgres_helper.select_query(pg_conn, query)
print(results)
print('-'*80)
print('\n')

# How many passengers were in each class?
query = '''SELECT pclass, COUNT(pclass)
FROM titanic
GROUP BY pclass;'''
results = postgres_helper.select_query(pg_conn, query)
print(results)
print('-'*80)
print('\n')

# How many passengers survived/died within each class?
query = '''SELECT pclass, survived, COUNT(survived)
FROM titanic
GROUP BY pclass, survived
ORDER BY pclass, survived ASC;;'''
results = postgres_helper.select_query(pg_conn, query)
print(results)
print('-'*80)
print('\n')

# What was the average age of each passenger class?
query = '''SELECT pclass, AVG(age)
FROM titanic
GROUP BY pclass;'''
results = postgres_helper.select_query(pg_conn, query)
print(results)
print('-'*80)
print('\n')

# What was the average fare by passenger class? By survival?
query = '''SELECT pclass, survived, AVG(fare)
FROM titanic
GROUP BY pclass, survived
ORDER BY pclass, survived ASC;'''
results = postgres_helper.select_query(pg_conn, query)
print(results)
print('-'*80)
print('\n')

# How many siblings/spouses aboard on average, by passenger class? By survival?
query = '''SELECT pclass, survived, AVG(siblings_spouses)
FROM titanic
GROUP BY pclass, survived
ORDER BY pclass, survived ASC;'''
results = postgres_helper.select_query(pg_conn, query)
print(results)
print('-'*80)
print('\n')

# How many parents/children aboard on average, by passenger class? By survival?
query = '''SELECT pclass, survived, AVG(parents_children)
FROM titanic
GROUP BY pclass, survived
ORDER BY pclass, survived ASC;
'''
results = postgres_helper.select_query(pg_conn, query)
print(results)
print('-'*80)
print('\n')

# Do any passengers have the same name?
query = '''SELECT name FROM titanic WHERE name NOT IN (SELECT DISTINCT name FROM titanic);
'''
results = postgres_helper.select_query(pg_conn, query)
print(results)
print('-'*80)
print('\n')
