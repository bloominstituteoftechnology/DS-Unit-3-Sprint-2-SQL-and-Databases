import psycopg2
import pandas as pd
from sqlalchemy import create_engine


def run_conversion(engine):
    # ___ load the CSV into a df ____
    csv_url = "titanic.csv"
    df = pd.read_csv(csv_url)
    # _____ Convert to postgres DB______
    df.to_sql('titanic', if_exists='replace', con=engine, method='multi')
    return


def main():
    # ____ Connect to postgres using SQLalchemy engine  __________
    dbname = 'zoafqkfp'
    user = 'zoafqkfp'
    host = 'stampy.db.elephantsql.com'
    passw = 'MCJu21HwCynkStIs3FOmV-xHXSAXOSDD'
    eng_str = 'postgresql+psycopg2://'+user+':'+passw+'@'+host+'/'+dbname
    engine = create_engine(eng_str)

    # ____ Port titanic.csv to postgres ___
    run_conversion(engine)

    #  _______ verify output  _________
    query = """
    SELECT *
    FROM public.titanic
    LIMIT 10 ;
    """
    print('--- public.titanic table ---')
    for row in engine.execute(query).fetchall():
        print(row)

    # ___ end main ___________
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
