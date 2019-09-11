import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()
#  ____________  CONNECT TO DATABASE ___________________
def db_connect(): 
    # __ Connect to AWS-RDS(postgres) (SQLalchemy.create_engine) ____
    dbname = os.getenv("DS_DB_NAME")
    user = os.getenv("DS_DB_USER")
    host = os.getenv("DS_DB_HOST")
    passw = os.getenv("DS_DB_PASSWORD")
    pgres_str = 'postgresql+psycopg2://'+user+':'+passw+'@'+host+'/'+dbname
    pgres_engine = create_engine(pgres_str)
    return pgres_engine

def insert_titanic(engine):
    # ___ load the CSV into a df ____
    csv_url = "titanic.csv"
    df = pd.read_csv(csv_url)
    # _____ Convert to postgres DB______
    df.to_sql('titanic', if_exists='replace', con=engine, method='multi')
    return


def main():
    # ____ Connect to postgres using SQLalchemy engine  __________
    engine = db_connect()

    # dbname = ''
    # user = ''
    # host = ''
    # passw = ''
    # file = open('elephant.pwd', 'r')
    # ctr = 1
    # for line in file:
    #     line=line.replace('\n', '')
    #     if ctr == 1:
    #         dbname = line
    #     if ctr == 2:
    #         user = line
    #     if ctr == 3:
    #         host = line
    #     if ctr == 4:
    #         passw = line
    #     ctr = ctr + 1
    # eng_str = 'postgresql+psycopg2://'+user+':'+passw+'@'+host+'/'+dbname
    # engine = create_engine(eng_str)

    # ____ Port titanic.csv to postgres ___
    insert_titanic(engine)

    #  _______ verify output  _________
    query = """
    SELECT *
    FROM public.titanic
    LIMIT 10 ;
    """
    print('--- public.titanic table from ', os.getenv("DS_DB_HOST"), '---')
    for row in engine.execute(query).fetchall():
        print(row)

    # ___ end main ___________
    return

#  Launched from the command line
if __name__ == '__main__':
    print('\n'*100)  # force teminal to clear screen
    main()
