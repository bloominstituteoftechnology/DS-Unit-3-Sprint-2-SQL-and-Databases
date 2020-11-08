from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

import pymssql  ## http://www.pymssql.org/index.html

def main():
    # ____ Connect to SQL Server __________
    HOST = os.getenv("DS_DB_HOST")
    DBASE = os.getenv("DS_DB_NAME")
    USER = os.getenv("DS_DB_USER")
    PWORD = os.getenv("DS_DB_PASSWORD")
    conn = pymssql.connect(HOST, USER, PWORD, DBASE)

    df = pd.read_sql_query("select * from dbo.Customers", conn)
    df.set_index('id', inplace=True )
    
    print(df)

    print(df.columns[0])


    return


#  Launched from the command line
if __name__ == '__main__':
    main()
