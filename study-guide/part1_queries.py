import sqlite3


conn = sqlite3.connect('study_part1.sqlite3')
curs = conn.cursor()

query1 = """
SELECT AVG(age)
FROM example;
"""

query2 = """
SELECT student
FROM example
WHERE sex='Female';
"""

query3 = """
SELECT COUNT(studied)
FROM example
WHERE studied='True';
"""

query4 = """
SELECT *
FROM example
ORDER BY student DESC;
"""

queries = [query1, query2, query3, query4]


def exe_query(query):
    records = curs.execute(query).fetchall()
    return f'{records} \n'


if __name__ == "__main__":
    for query in queries:
        print(exe_query(query))
    curs.close()
    conn.close()
