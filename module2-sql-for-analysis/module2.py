
import psycopg2


## from the CSV file get the headers
with open('titanic.csv') as file: 
    line = file.readline().strip().split(',')
headers  = [x.strip() for x in list(line)]
print(headers)

"""setup pg db """

params = {"dbname": "rtnktynj",
        'user': 'rtnktynj',
        'password': 'UDZgOFVupQwhuoyRcHtjVt9q1GK-XDtO',  ##need something better
        'host': 'ruby.db.elephantsql.com',
        'port': 5432}
SQL = "".join(open('titanic.db', 'r').readlines()[1:])
with psycopg2.connect(**params) as conn:     
    with conn.cursor() as curs:            # this code will auto commit if no exception
        curs.execute(SQL)

conn.close()


###########################333333
# Our goal - copy the charactercreator_character table


characters = sl_curs.execute(sql_column_values('charactercreator_character')).fetchall()

