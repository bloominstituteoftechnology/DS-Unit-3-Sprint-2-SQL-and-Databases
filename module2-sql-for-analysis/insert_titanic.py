import psycopg2 as pg
import pandas as pd


dbname = "srjbncyk"
user = "srjbncyk"
password = ""
host = "isilo.db.elephantsql.com"

def start_connection_elephantSQL(dbname, user, password, host):
    '''Start elephantSQL database connection'''
    conn = pg.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()
    return conn, cursor

def modify_database(cvFile='titanic.csv'):
    '''insert data from csv to elephantSQL'''
    conn, cursor = start_connection_elephantSQL(dbname, user, password, host)
    #
    create_table = """
    CREATE TYPE sex AS ENUM ('male', 'female');

    CREATE TABLE titanic (
        id SERIAL PRIMARY KEY,
        Survived int,
        Pclass int,
        Name text,
        Sex sex,
        Age int,
        Siblings_spouses_aboard int,
        Parents_children_aboard int,
        Fare float
    );
    """

    cursor.execute(create_table)
    conn.commit()

    # insert data into table
    df = pd.read_csv(cvFile)
    df.Name = df.Name.replace("'", '', regex=True)
    insert_data = df.values.tolist()
    for i in insert_data:
        insert_item = """INSERT INTO titanic (
        Survived, Pclass, Name, Sex, Age, Siblings_spouses_aboard,
        Parents_children_aboard, Fare)
        VALUES""" + str(tuple(i))
        cursor.execute(insert_item)
    conn.commit()

def main():
    modify_database()

if __name__ == '__main__':
    main()