import psycopg2 as pg
import pandas as pd
from functools import reduce
'''
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


df = pd.read_csv('titanic.csv').rename(columns=f).applymap(f)

dts = df.dtypes.replace({'int64': 'INT', 'object': 'TEXT', 'float64': 'FLOAT'})

tab_feats_name = '{0} ({1})'.format('titanic', reduce(
    lambda s, t: s + ', ' + t, [' '.join(t) for t in zip(dts.index,
                                                         [x.__str__() for x in dts.values])]))

create = f'CREATE TABLE {tab_feats_name};'
curs = pg_conn.cursor()

# + '(' + reduce(lambda s, t: s + ', ' + t, dts.index) + ')'
insert_prefix = f'INSERT INTO ' + '"titanic"'

inserts_multir = ' VALUES {0};'.format(reduce(
    lambda s, t: s + ", " + t, ["('" + "', '".join(map(str, df.loc[k].values)) + "')" for k in df.index]))
'''
try:
    curs.execute(create)
except pg.ProgrammingError as e:
    print(e)
'''
'''
try:
    curs.execute(insert_prefix + inserts_multir)
except pg.ProgrammingError as e:
    print(e)
#'''

pg_conn.commit()
pg_conn.close()
