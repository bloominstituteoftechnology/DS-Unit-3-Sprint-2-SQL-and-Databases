import psycopg2

dir(psycopg2
    )

dbname = 'ppezxvjc'
user = 'ppezxvjc'
password = 't0tlBYAiZvucD-MTqJAG2SPT87DZbVnS'  # Don't commit
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()
# help(pg_curs.execute)

# were connected, lets see what is the db
pg_curs.execute('SELECT * FR'
                'OM test_table;')
print(pg_curs.fetchall())

# Add another insert statement
insert_statement = """  
INSERT INTO test_table (name, data) VALUES
(
  'pokemon',
  '{"key": "value","key2" : 2}'::JSONB
) ;

"""

pg_curs.execute(insert_statement)
pg_conn.commit()

pg_curs.execute('SELECT * FROM test_table;')
print(pg_curs.fetchall())

# closing cursor
pg_curs.close()
# pg_conn.close() # If we were really done

