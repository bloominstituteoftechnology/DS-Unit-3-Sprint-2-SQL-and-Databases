import psycopg2


def connect_conn():
    """Establish connection to database and return connection object."""
    db = 'bgpuyxgj'
    user = 'bgpuyxgj'
    password = 'password'  # Don't commit!
    host = 'raja.db.elephantsql.com'

    conn = psycopg2.connect(dbname=db, user=user,
                            password=password, host=host)
    return conn


def create_db(conn):
    """Add a database named titanic to repo.

    Creates types for:
        sex: 'male', 'female' and
        pclass: '1', '2', '3'
    """
    create_enums = '''
    CREATE TYPE sex AS ENUM ('male', 'female');
    CREATE TYPE pclass AS ENUM ('1', '2', '3');
    '''
    curs = conn.cursor()
    curs.execute(create_enums)
    conn.commit()

    create_table = '''
    DROP TABLE titanic;
    CREATE TABLE titanic (
    id SERIAL PRIMARY KEY,
    survival BOOL,
    pclass pclass,
    name VARCHAR (255),
    sex sex,
    age FLOAT,
    sibsp INT,
    parch INT,
    fare FLOAT);
    '''

    curs = conn.cursor()
    curs.execute(create_table)
    conn.commit()
    return conn


def csv_to_db(file, conn):
    """Copy data from csv into new titanic database."""
    curs = conn.cursor()
    with open(file) as f:
        lines = f.readlines()[1:]
        for line in lines:
            surv, pclass, name, sex, age, sibsp, parch, fare = line.split(',')
            curs.execute("INSERT INTO titanic (survival, pclass, name, sex, age, sibsp, parch, fare)\
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (surv,
                                                                      str(pclass),
                                                                      str(name),
                                                                      sex,
                                                                      age,
                                                                      sibsp,
                                                                      parch,
                                                                      fare))
    conn.commit()
    curr = conn.cursor()
    curr.execute('''SELECT * FROM titanic LIMIT 10''')
    print(f'Return from query: {curr.fetchall()}\nSuccess!!!')


def query(conn, string: str):
    """Perform a query on titanic database and return result."""
    curs = conn.cursor()
    curs.execute(f'{string}')
    result = curs.fetchall()
    return result


def main():
    conn = connect_conn()
    create_db(conn)
    csv_to_db('titanic.csv', conn)
    a = '''SELECT titanic.name FROM 
    (SELECT t.name, t.survival FROM titanic t WHERE t.sex='male' and t.survival=FALSE) AS titanic'''
    print(query(conn, a))


if __name__ == "__main__":
    main()
