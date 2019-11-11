/* How many passengers Survived/ Died on the Titanic? */

import psycopg2

dbname = '********'       #same as user
user = '********'         #same as dbbase
password = '**********'     #don't commit this to github!
host = '***********'         #from SERVER type this in as string

pg_conn = psycopg2.connect(database=dbname, user=user, password=password, host=host)
