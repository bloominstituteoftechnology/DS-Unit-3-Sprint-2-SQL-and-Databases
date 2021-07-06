import psycopg2

conn = psycopg2.connect(host='raja.db.elephantsql.com', dbname='wrtjhlzu', user='wrtjhlzu', password='axdJ0omUL_sc_ypWI3YucEu87AXdzIiQ')
cur = conn.cursor()
cur.execute("""

CREATE TYPE sex AS ENUM ('male', 'female');

CREATE TABLE titanic(
Survived bool,
Pclass INT,
Name VARCHAR(30) PRIMARY KEY,
Sex sex,
Age INT,
SiblingsSpousesAboard INT,
ParentsChildrenAboard INT,
Fare float(4))
""")

with open('titanic.csv', 'r') as f:
    next(f)
    
cur.copy_from(f, 'titanic', sep=',')
conn.commit()
