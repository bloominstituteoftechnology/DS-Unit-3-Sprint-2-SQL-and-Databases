#Copy tables and data from a SQLite database and recreate them
#in a PostgreSQL database
 
import os, psycopg2, sqlite3, sys
from dotenv import load_dotenv

load_dotenv()

pgdb = os.getenv("pgdb")
pguser = os.getenv("pguser")
pgpswd = os.getenv("pgpswd")
pghost = os.getenv("pghost")
sqdb='rpg_db.sqlite3'
pgschema='public'
 
consq=sqlite3.connect(sqdb)
cursq=consq.cursor()
 
tabnames=[]
 
cursq.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'character%' OR name LIKE 'armory%' ORDER BY name;")
tabgrab = cursq.fetchall()
for item in tabgrab:
    tabnames.append(item[0])
 
for table in tabnames:
    cursq.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name = ?;", (table,))
    create = cursq.fetchone()[0]
    create = create.replace('AUTOINCREMENT', '')
    create = create.replace('bool', 'integer')
    cursq.execute("SELECT * FROM %s;" %table)
    rows=cursq.fetchall()
    colcount=len(rows[0])
    pholder='%s,'*colcount
    newholder=pholder[:-1]
 
    try:
 
        conpg = psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
                               host=pghost)
        curpg = conpg.cursor()
        curpg.execute("SET search_path TO %s;" %pgschema)
        curpg.execute("DROP TABLE IF EXISTS %s;" %table)
        curpg.execute(create)
        curpg.executemany("INSERT INTO %s VALUES (%s);" % (table, newholder),rows)
        conpg.commit()
        print('Created', table)
 
    except psycopg2.DatabaseError as e:
        print ('Error %s' % e) 
        sys.exit(1)
 
    finally:
 
        if conpg:
            conpg.close()
 
consq.close()