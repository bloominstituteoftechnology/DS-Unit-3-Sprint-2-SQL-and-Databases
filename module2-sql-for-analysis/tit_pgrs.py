import psycopg2 as pg
import pandas as pd
from functools import reduce
'''
For ElephantSQL API. 


- Make a table in your PostgreSQL db for titanic data (think about the schema!)
- Figure out inserting all the rows from the provided `titanic.csv`
     (try to do it all in a single `INSERT` statement, so it's more efficient)
- Explore pandas `to_sql`/`from_sql` and other cool functionality

'''
trunk = {
    'server': 'stampy.db.elephantsql.com',
    'username': 'xxvuedzq',
    'db': 'xxvuedzq',
    'pw': 'dPC9ig42zSmqFp6RhLeIGpgeVu1-gQed',
    'url': 'postgres://xxvuedzq:dPC9ig42zSmqFp6RhLeIGpgeVu1-gQed@stampy.db.elephantsql.com:5432/xxvuedzq',
    'apik': '9bbb1cb9-057a-4ae6-aa3c-8cb3e2288a4e'}

pg_conn = pg.connect(dbname=trunk['username'], user=trunk['db'],
                     password=trunk['pw'], host=trunk['server'])


def f(x):
    if isinstance(x, str):
        return (x.replace(' ', '_')
                .replace('/', '_')
                .replace(')', '')
                .replace('(', '')
                .replace("'", '')
                .replace(".", ""))
    else:
        return x

name = 'titanic'
df = pd.read_csv(name+'.csv').rename(columns=f).applymap(f)
N = df.shape[0]
dts = df.dtypes.replace({'int64': 'INT', 'object': 'TEXT', 'float64': 'FLOAT'})

tab_feats_name = '{0} ({1})'.format(name, reduce(
    lambda s, t: s + ', ' + t, [' '.join(t) for t in zip(dts.index,
                                                         [x.__str__() for x in dts.values])]))

create = f'CREATE TABLE {tab_feats_name};'
curs = pg_conn.cursor()

insert_prefix = f'INSERT INTO ' + name

inserts_multir = ' VALUES {0};'.format(reduce(
    lambda s, t: s + ", " + t, ["('" + "', '".join(map(str, df.loc[k].values)) + "')" for k in df.index]))


def inserts(q, NNN=N): 
    curs.execute('SELECT COUNT(*) FROM ' + name)
    if curs.fetchall()[0][0]<NNN: 
        try:
            curs.execute(q)
        except pg.ProgrammingError as e:
            print(e)
        else: 
            print("inserted now")
        finally: 
            print("exiting")
            pass
    else:
        print("items already inserted. ")
        pass

#curs.execute("DROP TABLE "+name)
try:
    curs.execute(create)
except pg.ProgrammingError as e:
    print(e)
else: 
    inserts(insert_prefix + inserts_multir)
finally: 
    pg_conn.commit()
    pg_conn.close()


