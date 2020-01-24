import psycopg2

dbname = 'tjqpupzb'
user = 'tjqpupzb'
password = 'ExCV1Zaq1teecCPRXMCo9lA-wetfjcCO' #Don't commit or share for security purposes
host = 'rajje.db.elephantsql.com' #Port should be included or default

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

create_table_statement = ''' 
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
'''
insert_statement = '''
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
'''

pg_curs.execute(create_table_statement)
pg_curs.execute(insert_statement)
pg_conn.commit()

query = 'SELECT * FROM test_table;'
pg_curs.execute(query)
pg_curs.fetchall()