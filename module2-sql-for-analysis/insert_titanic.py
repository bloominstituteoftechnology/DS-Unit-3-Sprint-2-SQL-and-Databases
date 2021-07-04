''' DOC String - Python file with objective of creating and inserting csv fikle into data'''

import psycopg2
import pandas as pd
import sqlite3


def create_db(csv, dbname, user, password, host):
    conn = psycopg2.connect(dbname=dbname, user=user,
                            password=password, host=host)

    ### A "cursor", a structure to iterate over db records to perform queries

    cur = conn.cursor()
    df = pd.read_csv(csv)

    def enum_pclass(file):
        with open(file, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            i = next(reader)
            lines = f.readlines()
            enums = []
            for line in lines:
                enum = line.split(',', 2)[1]
                enums.append(enum)
            t_enums = tuple(set(enums))
        return t_enums

    cur.execute('''DROP TABLE titanic''')
    cur.execute('''DROP TYPE pclass''')
    cur.execute('''CREATE TYPE pclass AS ENUM ''' + str(t_enums))

    create_table_query_type = '''CREATE TABLE titanic (id SERIAL PRIMARY KEY, survived BOOL NOT NULL,
    pclass pclass, name VARCHAR(255) NOT NULL, sex BOOL NOT NULL, age FLOAT, s_s INT, p_c INT, fare FLOAT);'''

    cur.execute(create_table_query_type)
    conn.commit()
    return conn


def create_table(file, conn):
    cur = conn.cursor()
    with open(file, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        i = next(reader)
        lines = f.readlines()
        for line in lines:
            survived, pclass = line.split(',', 2)[:2]
            name = line.split(',', 3)[2]
            if line.split(',', 4)[3] == 'male':
                sex = line.split(',', 4)[3].replace('male', '0')
            else:
                sex = line.split(',', 4)[3].replace('female', '1')
            age, s_s, p_c = line.split(',')[4:-1]
            fare = line.split(',')[-1].replace('\n', '')
            cur.execute('''INSERT INTO titanic (survived, pclass, name, sex, age, s_s, p_c, fare)
                        VALUES(%s, %s, %s, %s, %s, %s,%s, %s);''',
                        (survived, str(pclass), str(name), sex, age, s_s, p_c, fare)
                        )
    conn.commit()
    cur.execute('''SELECT * FROM titanic''')
    cur.close()
