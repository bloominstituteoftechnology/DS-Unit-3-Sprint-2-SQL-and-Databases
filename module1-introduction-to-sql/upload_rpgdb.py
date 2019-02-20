import psycopg2, sqlite3, sys

pg_user = 'munmevbr'
pg_password = 'ZTpRBiHy6sTarv3OPATL8vOVsQmOCeAH'
pg_db = 'munmevbr'
pg_host = 'stampy.db.elephantsql.com'
pg_port = '5432'
pg_schema = ''

sqlite_db = 'rpg_db.sqlite3'

connection = sqlite3.connect(sqlite_db)
sqlite_cursor = connection.cursor()

table_names = []

# grabs the names of all the sqlite db tables
sqlite_cursor.execute(""" SELECT name FROM sqlite_master WHERE type='table' """)
table_grab = sqlite_cursor.fetchall()

for name in table_grab:
    table_names.append(name[0])

for table in table_names:
    sqlite_cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name = ?", (table,))
    create_view = sqlite_cursor.fetchone()[0]
    sqlite_cursor.execute('SELECT * FROM %s' % table)
    table_rows = sqlite_cursor.fetchall()
    column_count = len(table_rows[0])
    placeholder = '%s,'*column_count
    new = placeholder[:-1]

    try:
        postgres_connection = psycopg2.connect(database=pg_db, user=pg_user, password=pg_password, host=pg_host,
                                               port=pg_port)
        postgres_cursor = postgres_connection.cursor()
        postgres_cursor.execute("SET search_path TO {!r};".format(pg_schema))
        postgres_cursor.execute("DROP TABLE IF EXISTS %s;" % table)
        postgres_cursor.execute(create_view)
        postgres_cursor.executemany("INSERT INTO %s VALUES (%s);" % (table, new), table_rows)
        postgres_cursor.commit()
        print('Created', table)

    except psycopg2.DatabaseError as e:
        print('Error %s') % e
        sys.exit(1)

    finally:
        if postgres_cursor:
            postgres_cursor.close()

sqlite_cursor.close()
