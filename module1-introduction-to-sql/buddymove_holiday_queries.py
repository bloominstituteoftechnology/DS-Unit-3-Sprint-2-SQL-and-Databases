import sqlite3


def connect_to_db(db_name='Reviews.db'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_ROWS = """
    SELECT COUNT(*)
    FROM REVIEWS;

"""
GET_REVIEWS_LEAST_100 = """
SELECT COUNT(*)
FROM REVIEWS
WHERE Nature >= 100 and Shopping >=100
;


"""



if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()

    reviews_least_100 = execute_query(curs, GET_REVIEWS_LEAST_100)
    print(reviews_least_100)
