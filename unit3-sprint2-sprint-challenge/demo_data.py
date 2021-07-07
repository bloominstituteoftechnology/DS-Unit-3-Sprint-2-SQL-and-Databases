import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

# Create a query string for creating the table 'demo'
create_table = """
    CREATE TABLE demo (
    s VARCHAR(1),
    x INT,
    y INT
    )
    """

# Try to create a new table 'demo'
# If one already exists, print the error
# Always close cursor and commit connection
curs0 = conn.cursor()
try:
    curs0.execute(create_table)
    print('Created Table demo')
except Exception as e:
    print(e)
finally:
    curs0.close()
    conn.commit()

# Create query string for inserting table data
insert_data = """
    INSERT INTO demo
    VALUES
        ('g',3,9),
        ('v',5,7),
        ('f',8,7)
    """

# Try to insert data into table 'demo'
# If data already exists, dont insert again
curs1 = conn.cursor()
if(curs1.execute('SELECT COUNT(*) FROM demo').fetchone()[0] == 0):
    curs1.execute(insert_data)
    print('Inserted Data')
else:
    print('Data Already Present')

curs1.close()
conn.commit()

# Test Queries
q0 = """
    SELECT COUNT(*) 
    FROM demo
    """
q1 = """
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5 AND y >= 5
    """
q2 = """
    SELECT COUNT(DISTINCT y)
    FROM demo
    """

# Executing test Queries
curs2 = conn.cursor()
curs2.execute(q0)
print('Total Rows: {}'.format(curs2.fetchone()[0]))

curs2.execute(q1)
print('Total Rows Where x>=5 and y>=5: {}'.format(curs2.fetchone()[0]))

curs2.execute(q2)
print('Distinct y values: {}'.format(curs2.fetchone()[0]))

curs2.close()
conn.commit()