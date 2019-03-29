import sqlite3


# Function that connects to a db and executes an sql statement in the sql param
def execute_sql(sql, db_name):
    conn = sqlite3.connect(db_name)
    curs = conn.cursor()
    return [curs.execute(sql).fetchall(), conn.commit()][0]

db = "demo_data.sqlite3"

sql = "CREATE TABLE demo(s varhar(2), x smallint, y smallint);"

execute_sql(sql, db)

sql = ("""INSERT INTO demo (s, x, y)
          VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);""")

execute_sql(sql, db)

# Number of rows
sql = "SELECT COUNT(*) FROM demo;"
print('Total number of rows:', execute_sql(sql, db))

# Number of rows where both x and y are at least 5
sql = "SELECT COUNT(*) FROM demo WHERE x >= 5 and y >= 5;"
print('Number of rows where bith x and y are at least 5:',
      execute_sql(sql, db))

# Unique values of y
sql = "SELECT COUNT(DISTINCT y) from demo"
print('Unique values of y:', execute_sql(sql, db))
