import psycopg2
connect = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cursor = connect.cursor()
query = '''
    CREATE TABLE titanic(
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name TEXT,
    sex VARCHAR(6),
    age INT,
    siblings_spouses_aboard INT,
    parents_children_aboard INT,
    fare INT
);
'''
cursor.execute(query)

query = '''
COPY titanic(survived, pclass, name, sex, age, siblings_spouses_abroad, parents_children_abroad, fare)
FROM 'DS-Unit-3-Sprint-2-SQL-and-Databases\module2-sql-for-analysis\titanic.csv' DELIMITER ',' CSV HEADER;
'''
cursor.execute(query)