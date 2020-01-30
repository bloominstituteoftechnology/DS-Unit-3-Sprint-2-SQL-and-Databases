import os
import sqlite3
import buddy_file
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
DB_FILEPATH = buddy_file.BUDDY_FILEPATH
conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

df.to_sql(name="buddymove_holidayiq", con=conn, index_label="index_label", if_exists='replace')
curs.close()

def get_count():
    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    count_query = """
    select
        *
    from buddymove_holidayiq
    """

    results = curs.execute(count_query).fetchall()
    conn.close()

    return results

def get_filtered_count():
    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    filtered_count_query = """
    select
	   count(distinct [User Id]) as user_count
    from buddymove_holidayiq
    where Nature > 100 and Shopping > 100
    """

    results = curs.execute(filtered_count_query).fetchall()
    conn.close()

    return results

def get_category_avgs():
    conn = sqlite3.connect(DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()

    category_avgs_query = """
    select
	   avg(sports) as avg_sports,
	    avg(religious) as avg_religious,
	    avg(nature) as avg_nature,
	    avg(theatre) as avg_theatre,
	    avg(shopping) as avg_shopping,
	    avg(picnic) as avg_picnic
    from buddymove_holidayiq
    """

    results = curs.execute(category_avgs_query).fetchall()
    conn.close()

    return results
