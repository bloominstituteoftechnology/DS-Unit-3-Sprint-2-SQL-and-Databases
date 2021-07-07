import sqlite3

# construct a path to wherever your database exists
DB_FILEPATH = "buddymove_holidayiq.sqlite3"
# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()

# queries

query = "SELECT * from review"
chars = cursor.execute(query).fetchall()
q1 = len(chars)

print(' # How many rows in the table?')
print(f'  {q1} rows in the table.')

query1 = '''
         SELECT
            (Nature > 100) as nature_count,
	        (Shopping > 100) as shopping_count
         FROM review
         WHERE nature_count = 1
         AND shopping_count = 1
         '''

chars = cursor.execute(query1).fetchall()
q2 = len(chars)

print(' # How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?')
print(f'  {q2} who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category.')
