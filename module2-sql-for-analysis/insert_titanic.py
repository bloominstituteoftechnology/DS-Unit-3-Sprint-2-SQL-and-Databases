import psycopg2


def connect_server():
    """connect to server database"""
    conn = psycopg2.connect(dbname='pbiqefej',
                            user='pbiqefej',
                            password=input('Password please:'),
                            host='rogue.db.elephantsql.com')
    return conn


def create_db(conn, file_csv):
    """create database 'titanic' and creates enumerate types 'SEX' and 'P_CLASS' """

    curs = conn.cursor()
    curs.execute("CREATE TYPE SEX AS ENUM ('female', 'male');\
                 CREATE TYPE P_CLASS AS ENUM ('1', '2', '3');")
    curs.execute("DROP TABLE IF EXISTS titanic;")
    curs.execute("CREATE TABLE titanic(\
                  id SERIAL PRIMARY KEY,\
                  survived BOOL,\
                  pclass P_CLASS,\
                  name VARCHAR (255),\
                  sex SEX,\
                  age INT,\
                  sib_spo INT,\
                  par_chi INT,\
                  fare FLOAT);")

    with open(file_csv) as f:
        rows = f.readlines()[1:]
        for row in rows:
            survived, pclass, name, sex, age, sib_spo, par_chi, fare = row.split(',')
            curs.execute("INSERT INTO titanic (survived, pclass, name, sex, age, sib_spo, par_chi, fare)\
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",\
                         (survived, str(pclass), str(name), sex, age, sib_spo, par_chi, fare)
    conn.commit()
    return conn


def main():
    conn = connect_server()
    create_db(conn, 'titanic.csv')
    curs = conn.cursor()
    return curs.execute('''SELECT name, age FROM titanic WHERE survived=FALSE''').fetchall()



if __name__ == "__main__":
    main()