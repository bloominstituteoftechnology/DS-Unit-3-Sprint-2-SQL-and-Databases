import psycopg2 as pig
dbname = 'ppdtwyrt'
user = 'ppdtwyrt'
password = '8lIzgnGAvLlp32uvxDdXBd8QuFDBhByh'
host = 'stampy.db.elephantsql.com'
conn = pig.connect(dbname=dbname,user=user,
                    password=password,host=host)
curse = conn.cursor()

make_titanic_table = curse.execute('''
    CREATE TABLE titanic_table(
        survived boolean PRIMARY KEY,
        pclass int,
        name varchar(40),
        sex text,
        age int,
        spouse_sibling text,
        parents_children text,
        fare numeric
    )
'''),conn.commit()


with open('titanic.csv', 'r') as f:
    next(f)
    curse.copy_from(f, 'titanic_table', sep = ',')
conn.commit()