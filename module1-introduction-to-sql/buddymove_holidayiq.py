import pandas as pd
import sqlite3

df = pd.read_csv("buddymove_holidayiq.csv")

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
c = conn.cursor()

df.to_sql("buddymove_holidayiq", conn)

def connect_to_db(db_name="buddymove_holidayiq.sqlite3"):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

ROW_COUNT = """
SELECT COUNT(*) FROM buddymove_holidayiq
"""

USER_REVIEWS = """

SELECT COUNT(*) 
FROM buddymove_holidayiq
WHERE buddymove_holidayiq.Nature > 100 
AND buddymove_holidayiq.Shopping > 100
"""

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    row_count = execute_query(curs, ROW_COUNT)
    print("Row Count:", row_count)
    user_reviews = execute_query(curs, USER_REVIEWS)
    print("User Reviews:", user_reviews)