import pandas as pd
import sqlite3


def import_dataset():
    data = pd.read_csv('https://raw.githubusercontent.com/NikuDubenco/DS-Unit-3-Sprint-2-SQL-and-Databases/'
                       'master/module1-introduction-to-sql/buddymove_holidayiq.csv')

    print('First 5 rows of DataFrame data: \n', data.head(),
          'Shape of DataFrame data: \n', data.shape,
          'Check the DataFrame data for Null values: \n', data.isna().sum())

    return data


def create_sql_db(data):
    conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS buddymove_holidayiq''')
    data.to_sql('buddymove_holidayiq', conn, if_exists='replace', index=False)
    pd.read_sql('select * from buddymove_holidayiq', conn)
    conn.commit()
    conn.close()


def connect_to_db():
    # connection
    con = sqlite3.connect('buddymove_holidayiq.sqlite3')
    cursor = con.cursor()

    # Count how many rows you have - it should be 249!
    row_num = cursor.execute("SELECT count(*) FROM buddymove_holidayiq;").fetchall()
    print(f'The table has {row_num} rows')

    # How many users who reviewed at least 100 Nature in the category also
    # reviewed at least 100 in the Shopping category?
    row_num_nat_shop = cursor.execute("SELECT count(*) FROM buddymove_holidayiq \
                                       WHERE Nature >= 100 \
                                       AND Shopping >= 100;").fetchall()
    print(f'The table has {row_num_nat_shop} rows, where reviews for Nature and Shopping are greater the 100')


def main():
    import_dataset()
    create_sql_db(data)
    connect_to_db()


if __name__ == "__main__":
    main()