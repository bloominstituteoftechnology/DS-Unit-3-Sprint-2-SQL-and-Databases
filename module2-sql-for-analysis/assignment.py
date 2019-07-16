import psycopg2


def create_db():
    db = 'bgpuyxgj'
    user = 'bgpuyxgj'
    password = 'V-Jx_5OuILdziMIe5MvVDu61OdhoWMCR'  # Don't commit!
    host = 'raja.db.elephantsql.com'

    conn = psycopg2.connect(dbname=db, user=user,
                            password=password, host=host)

    curs = conn.cursor()

    create_table = '''
    DROP TABLE titanic;
    CREATE TYPE pclass1 AS ENUM ('1', '2', '3');
    CREATE TABLE titanic (
    id SERIAL PRIMARY KEY,
    survival BOOL NOT NULL,
    pclass pclass1,
    name VARCHAR (255) NOT NULL,
    sex sex,
    age FLOAT,
    sibsp INT,
    parch INT,
    fare FLOAT);
    '''

    curs.execute(create_table)
    conn.commit()
    return conn


def csv_to_db(file, conn):
    curs = conn.cursor()
    with open(file) as f:
        lines = f.readlines()[1:]
        for line in lines:
            surv, pclass1, name, sex, age, sibsp, parch, fare = line.split(',')
            curs.execute("INSERT INTO titanic (survival, pclass, name, sex, age, sibsp, parch, fare)\
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (surv,
                                                                      str(pclass1),
                                                                      str(name),
                                                                      sex,
                                                                      age,
                                                                      sibsp,
                                                                      parch,
                                                                      fare))
    conn.commit()
    curr = conn.cursor()
    curr.execute('''SELECT * FROM titanic''')
    print(f'Return from query: {curr.fetchall()}\nSuccess!!!')


def main():
    conn = create_db()
    csv_to_db('titanic.csv', conn)


if __name__ == "__main__":
    main()
