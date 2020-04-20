import psycopg2, sqlite3, sys
import os

from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

sqdb='rpg_db.sqlite3'
sqlike='charactercreator_%'
pgdb=DB_NAME
pguser=DB_USER
pgpswd=DB_PASSWORD
pghost=DB_HOST
pgport='5432'
pgschema='rpg_data'

consq=sqlite3.connect(sqdb)
cursq=consq.cursor()

tabnames=[]

cursq.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%s'" % sqlike)
tabgrab = cursq.fetchall()
for item in tabgrab:
    tabnames.append(item[0])

for table in tabnames:
    cursq.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name = ?;", (table,))
    create = cursq.fetchone()[0]
    print(create)
    create = create.replace(" AUTOINCREMENT", "")
    print(create)
    cursq.execute("SELECT * FROM %s;" %table)
    rows=cursq.fetchall()
    colcount=len(rows[0])
    pholder='%s,'*colcount
    newholder=pholder[:-1]

    try:

        conpg = psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
                               host=pghost, port=pgport)
        curpg = conpg.cursor()
        print("debug 1")
        curpg.execute("SET search_path TO %s;" %pgschema)
        print("debug 2")
        curpg.execute("DROP TABLE IF EXISTS %s;" %table)
        print("debug 3")
        curpg.execute(create)
        print("debug 4")
        curpg.executemany("INSERT INTO %s VALUES (%s);" % (table, newholder),rows)
        print("debug 5")
        conpg.commit()
        print('Created', table)

    except psycopg2.DatabaseError as e:
        print ('Error %s' % e)
        sys.exit(1)

    finally:

        if conpg:
            conpg.close()

consq.close()
