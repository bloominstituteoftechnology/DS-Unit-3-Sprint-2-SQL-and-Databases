import psycopg2
import pandas as pd
import sqlite3

engine = sqlite3.connect('Titanic.sqlite3')


def manageTitanicFile():
    df = pd.read_csv('titanic.csv')
    df.columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age',
                  'Siblings_Spouses_Aboard', 'Parents_Children_Aboard', 'Fare']
    df['Name'] = df['Name'].str.replace("'", "")
    df.to_sql('Titanic', con=engine, if_exists='replace')


curs = engine.cursor()


def connecting(dbname, user, password, host):
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                               password=password, host=host)
    pg_curs = pg_conn.cursor()


def createEmpTab():
    create_titanic_table = '''
    CREATE TABLE Titanic (
      index SERIAL PRIMARY KEY,
      Survived INT,
      Pclass INT,
      Name TEXT,
      Sex TEXT,
      Age REAL,
      Siblings_Spouses_Aboard INT,
      Parents_Children_Aboard INT,
      Fare REAL
      );
      '''
    pg_curs.execute(create_titanic_table)


def fillTab():
    peoples = curs.execute('SELECT * FROM Titanic;').fetchall()
    for people in peoples:
        insert_person = '''
        INSERT INTO Titanic
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
         Parents_Children_Aboard, Fare)
        VALUES ''' + str(people[1:]) + ';'
        # print(insert_person)
        pg_curs.execute(insert_person)


def closeComm():
    pg_curs.close()
    pg_conn.commit()


if __name__ == '__main__':
    manageTitanicFile()
    connecting(dbname='todo', user='todo', password='todo', host='todo')
    createEmpTab()
    fillTab()
    closeComm()
