
import psycopg2
import sqlite3



# This is a method that will add apostrophe 
# into the strings where an apostrophe already resides
def insert_apostrophe(obj):
    s = str(obj)
    #looping through adding apostrophe 
    #to each location where an apostrophe
    # is already found.
    startPoint = 0
    while(True):
        ind = s.find("\'", startPoint)
        if ind == -1:
            return s
        else:
            s = s[:ind] + "\'" + s[ind:]
            startPoint = ind + 2 


# Method to check if the table is found in the tuples
def check_if_table_found(list_of_tuples, tableName):
    for the_tuple in list_of_tuples:
        if tableName in the_tuple:
            return 1
    return 0        

# Method to check the number of row in the table
# This method will be used to check the size of the 
# table to see if anything has been placed in it
def isEmpty(the_cursor, tableName):
    the_cursor.execute("Select count(*)  From" + tableName)
    # check the size in rows
    r = the_cursor.fetchall()
    if r[0][0] == 0:
        return 1
    elif r[0][0] > 0:
        return 0
    else:
        return -1

# This method is used inside of the create_and_load_table
# and will load the data in to the table
def load_data(the_conn, the_cursor, charTable, load_query, check_if_table_empty, tableName):
    
    if check_if_table_empty:
        ans = isEmpty(the_cursor, tableName)
        if ans == 0:
            return
        if ans == -1:
            return 
        # The charTable is a list of tuples 
    for theRow_tuple in charTable:
        s = load_query + str(theRow_tuple[1:])
        the_cursor.execute(s)
        the_conn.commit()
    #the_conn.commit()


# This is the method that will load make the 
# table and then load the data if it hasn't been created 
# and loaded
def create_and_load_table(p_conn, charTable, create_query, insert_query, tableName, load_only=False,
                        check_if_table_empty=False):
    """
        p_conn: The connection for the postgresql database.

        charTable:  The list of tuples of the data to be loaded into the postgresql database

        create_query:   The string sql query to create the table in the postgresql database

        insert_query:   The string sql query to insert into the table. It will be used in a loop.

        tableName: The string representation of the table name. used to check if the table is already in the
        postgresql database

        check_if_table_empty:   boolean used to check if the table is empty in the postgresqly.
        When the check is set to true of the table is not empty it will not load more data into
        the table in the postgesql database.

        load_only:  If set to True then the function will not try to create the table but will 
        just try to load the data. If it is set to false and the table has been already created,
        then then this method will return before any loading is tried.

    """
    cur = p_conn.cursor()

    quer_show_table = """
        SELECT
            *
        FROM
            pg_catalog.pg_tables
        WHERE
            schemaname != 'pg_catalog'
        AND schemaname != 'information_schema';
    """

    
    if load_only == False:
        cur.execute(quer_show_table)
        if check_if_table_found(cur.fetchall(), tableName) == 1:
            return # doing nothing more if the table already exists

        cur.execute(create_query)
        p_conn.commit()
    
    # adding the info into the table
    load_data(p_conn, cur, charTable, insert_query , check_if_table_empty, tableName)

def load_from(conn, list_of_tuples, load_query, start_where):
    curs = conn.cursor()

    for i in range(len(list_of_tuples)):
        if i >= start_where:
            s = load_query + str(list_of_tuples[i][1:]) 
            curs.execute(s)
            conn.commit()
