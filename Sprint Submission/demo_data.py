import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
create_table_query = '''
    CREATE TABLE demo_data(
        s VARCHAR(10),
        x INT,
        y INT
    )
    '''
insert_values_query1 = '''
    INSERT INTO demo_data (s, x, y) VALUES('g',3,9);
    '''
insert_values_query2 = '''
    INSERT INTO demo_data (s, x, y) VALUES('v',5,7);
    '''
insert_values_query3 = '''
    INSERT INTO demo_data (s, x, y) VALUES('f',8,7);
    '''
curs.execute(create_table_query)
curs.execute(insert_values_query1)
curs.execute(insert_values_query2)
curs.execute(insert_values_query3)
demo_data_print = curs.execute('SELECT * FROM demo_data;').fetchall()
print(demo_data_print)
row_count = curs.execute('SELECT COUNT(*) FROM demo_data;').fetchall()
print(row_count)
x_y_higher_than_5 = curs.execute('SELECT COUNT(*) FROM demo_data WHERE y>=5 AND x>=5;').fetchall()
print(x_y_higher_than_5)
y_unique = curs.execute('SELECT COUNT(DISTINCT y) FROM demo_data;').fetchall()
print(y_unique)
curs.close()
conn.commit()
