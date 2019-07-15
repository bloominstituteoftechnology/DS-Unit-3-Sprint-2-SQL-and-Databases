#!/usr/bin/env python
import pandas as pd
def main():
    import sqlite3
    conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
    try:
        pd.read_csv('buddymove_holidayiq.csv').to_sql('review', conn)
    except ValueError:
        print('Database Already Created, Proceeding with reports...')
    c = conn.cursor()
    row_count = c.execute('SELECT count(*) FROM review').fetchone()[0]
    print('Count How many rows: ', row_count)
    res = c.execute('SELECT count(*) FROM review WHERE Nature>=100 AND Shopping>=100')\
        .fetchone()[0]
    print('How many users who reviewed at least 100 Nature in the category'
            ' also reviewed at least 100 in the Shopping category? ',
            res)
    avgs = c.execute('''
        SELECT AVG(Sports),
        AVG(Religious), AVG(Nature),
        AVG(Shopping), AVG(Picnic) FROM review
        ''').fetchone()
    print('What are the average number of reviews for each category?')
    print('Sports: ', avgs[0])
    print('Religious: ', avgs[1])
    print('Nature: ', avgs[2])
    print('Shopping: ', avgs[3])
    print('Picnic: ', avgs[4])
if __name__ == "__main__":
    main()