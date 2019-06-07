import sqlite3
#creating database
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
#creating table with columns with appropriate datatypes
create_table = '''CREATE TABLE "demo" (
                                        "s" TEXT,
                                        "x" INTEGER,
                                        "y" INTEGER
                                            );'''
curs.execute(create_table)
#populating table with values 
pop_table='''INSERT INTO demo 
              VALUES   ('g',3,9),
                       ('v',5,7),
                       ('f',8,7);
                                    '''
curs.execute(pop_table)
#saving/commiting
conn.commit()
#answering queuries as instructed
print('''answering these questions in order
Count how many rows you have - it should be 3!
How many rows are there where both x and y are at least 5?
How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?''')
a='SELECT COUNT(*) FROM demo'
b='SELECT COUNT(*) FROM demo WHERE x>5 AND y>5'
c='SELECT COUNT(DISTINCT y) FROM demo'
queries=[a,b,c]
for q in queries:
    print(curs.execute(q).fetchall()[0][0])