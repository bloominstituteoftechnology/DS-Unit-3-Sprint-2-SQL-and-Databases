import sqlite3

conn = sqlite3.connect('demo_data.py')
curs = conn.cursor() 

create_table = """ 
    CREATE TABLE demodata(
    s VARCHAR(30), 
    x INT, 
    y INT
    );
""" 

curs.execute(create_table)

insert_table = """
    INSERT INTO demodata(s, x, y)
    VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
""" 

curs.execute(insert_table) 
conn.commit()

q1 = """
SELECT COUNT(*)
FROM demodata;
""" 

q2 = """ 
SELECT COUNT(*) 
FROM demodata
WHERE x >=5 AND y>=5; 
""" 

q3 = """
SELECT COUNT(
DISTINCT y
)
FROM demodata; 
""" 

curs1 = conn.cursor()
print('total number of rows:', curs1.execute(q1).fetchall())

curs2 = conn.cursor() 
print('# of rows where x&y are atleast 5:', curs2.execute(q2).fetchall())

curs3 = conn.cursor()
print('# of unique values of y:', curs3.execute(q3).fetchall())
