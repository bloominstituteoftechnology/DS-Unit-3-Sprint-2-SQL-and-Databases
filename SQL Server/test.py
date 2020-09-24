from sqlalchemy import create_engine
import pandas as pd
import pymssql


def main():
    # ____ Connect to SQL Server __________
    SVR = "172.24.44.234"
    DRIVER = "SQL Server Native Client 11.0"
    DBASE = 'tutorials'
    USER = 'sa'
    PWORD = '@Ec621006'
    conn = pymssql.connect(SVR, USER, PWORD, DBASE)



    df = pd.read_sql_query("select * from dbo.Customers", conn)
    print(df)

    return


#  Launched from the command line
if __name__ == '__main__':
    main()

