from sqlalchemy import create_engine
import pandas as pd
import pymssql  ## http://www.pymssql.org/index.html

def main():
    # ____ Connect to SQL Server __________
    SVR = os.getenv("DS_DB_NAME")
    DRIVER = os.getenv("DS_DB_USER")
    SVR = os.getenv("DS_DB_HOST")
    PWORD = os.getenv("DS_DB_PASSWORD")
    conn = pymssql.connect(SVR, USER, PWORD, DBASE)

    df = pd.read_sql_query("select * from dbo.Customers", conn)
    print(df)

    return


#  Launched from the command line
if __name__ == '__main__':
    main()
