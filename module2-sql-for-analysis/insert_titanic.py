"""
Help documentation for insert_titanic:


    This module is designed to insert data from the titanic csv into the
    local postgreSQL server running on my machine.

    This module will not work if used on any machine other than my own, as is.

    To make this file work in your local system, first ensure that you have
    a postgreSQL server running.
    
    Replace the 'dbname', 'user', 'password', 'host', and 'port' variables
    with the details for your own local server.

    This will allow you to be able to run this file locally.
"""

import psycopg2 as pg
import pandas as pd


# Get titanic data into suitable format
def get_data(csv=None):
    """
    Doc for get_data method:
        This method was designed such that you pass in a 
        string with the relative path to the csv to get.

        This method will take that csv file and read it into a
        pandas DataFrame.
    """
    assert csv != None
    assert 'csv' in csv
    df = pd.read_csv(csv)
    return df

dbname = 'titanic'
user = 'asherg1'
password = '*******'
host = 'localhost'
port = '5432'

def get_connection(
    dbname=dbname, 
    user=user, 
    password=password, 
    host=host, 
    port=port):

    """
    Doc for get_connection:
        
        This method opens up and instantiates a connection to a 
        postgres database.
    """

    # Establish connection
    pg_conn = pg.connect(
        dbname=dbname, 
        user=user, 
        password=password, 
        host=host, 
        port=port
    )

    # Instantiate cursor for executing commands to Database
    pg_cursor = pg_conn.cursor()

    return pg_conn, pg_cursor


def close_connection(cursor, connector):
    """
    Doc for close_connection:

        As the name implies, closes the currently open cursor and 
        commits changes, closing the socket connection.
    """
    cursor.close()
    connector.commit()
    return


if __name__ == '__main__':

    # Read in the data
    df = get_data('titanic.csv')

    # Open connection to Database
    conn, curs = get_connection(dbname, user, password, host, port)

    # Create schema for data transfer
    curs.execute(
        """
        CREATE TABLE titanic (
            Survived INT,
            Pclass INT,
            Name VARCHAR(150),
            Sex VARCHAR(10),
            Age NUMERIC(6),
            _5 INT,
            _6 INT,
            Fare NUMERIC(6)
        )
        """
    )

    # Input each row from the DataFrame into the Database
    sql_command = """
        INSERT INTO titanic (
            Survived, 
            Pclass, 
            Name, 
            Sex, 
            Age, 
            _5, 
            _6, 
            Fare 
        ) VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s);
        """

    data = [row for row in df.itertuples(index=False)]

    for item in data:
        curs.execute(
            sql_command, 
            item
        )
    
    # Close connections and commit changes
    close_connection(curs, conn)
