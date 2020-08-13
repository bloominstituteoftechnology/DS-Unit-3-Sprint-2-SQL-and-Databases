import pandas as pd
import sqlite3


def connect_to_db(db_name="buddymove_holidayiq.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# Count how many rows you have - it should be 249!
TOTAL_ROWS = """
    SELECT COUNT(*)
    FROM review
"""


# How many users who reviewed at least 100 `Nature` in the category also
# reviewed at least 100 in the `Shopping` category?
TOTAL_USERS_NATURE_SHOPPING = """
    SELECT COUNT(*)
    FROM review
    WHERE Nature > 100 AND Shopping > 100
"""


if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()

    # df = pd.read_csv('buddymove_holidayiq.csv')
    # df.to_sql('review', con=conn)

    rows = execute_query(curs, TOTAL_ROWS)
    users = execute_query(curs, TOTAL_USERS_NATURE_SHOPPING)

    print("There are %d total rows." % (rows[0][0]))
    print(
        "There are %d total users who reviewed at least 100 in the 'Nature'"
        " category as well as at least 100 in the 'Shopping' category."
        % (users[0][0])
    )
