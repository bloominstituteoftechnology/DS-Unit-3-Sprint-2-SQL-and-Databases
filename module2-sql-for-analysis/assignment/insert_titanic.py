import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
from psycopg2.extras import execute_values


load_dotenv()

# connecting to the elephant sql titanic db
TITANIC_DB_NAME = os.getenv('TITANIC_DB_NAME', default='oops')
TITANIC_DB_USER = os.getenv('TITANIC_DB_USER', default='oops')
TITANIC_DB_PASSWORD = os.getenv('TITANIC_DB_PASSWORD', default='oops')
TITANIC_DB_HOST = os.getenv('TITANIC_DB_HOST', default='oops')
postgresql_connection = psycopg2.connect(dbname=TITANIC_DB_NAME, host=TITANIC_DB_HOST, password=TITANIC_DB_PASSWORD, user=TITANIC_DB_USER)
postgresql_cursor = postgresql_connection.cursor()

print(postgresql_connection)
print(postgresql_cursor)
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'titanic.csv')

query = '''
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    survived integer,
    pclass integer,
    name varchar(200) NOT NULL,
    sex varchar(6),
    age float,
    "siblings/spouses_aboard" integer,
    "parents/children_aboard" integer,
    fare float
)
'''

postgresql_cursor.execute(query)

df = pd.read_csv(CSV_FILEPATH)
df.columns = [item.lower().replace(' ', '_') for item in df.columns.tolist()]
df['survived'] = df['survived'].apply(lambda x: float(x))


my_list = [tuple(row) for row in df.itertuples(index=False)] 
# commenting this out so it doesnt keep adding more and more data
'''
insertion_query = f'INSERT INTO titanic (survived, pclass, name, sex, age, "siblings/spouses_aboard", "parents/children_aboard", fare) VALUES %s'
execute_values(postgresql_cursor, insertion_query, my_list)
'''

result = postgresql_cursor.execute('SELECT * FROM titanic')
print(result)
postgresql_connection.commit()
postgresql_cursor.close()
postgresql_connection.close()