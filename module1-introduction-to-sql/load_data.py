
class Load_Data():

    def __init__(self, db_file):
        self.db_file = db_file

    def create_dataframe(self, columns, table):
        '''
        Convert a SQLite3 database into a pandas DataFrame
        --------------------------------------------------
        Parameters
        columns: (string) Enter the column or columns desired
                 example 1- "column_desired"
                 example 2- "column_1, column_2"
                 example 3- "*" to select all columns. If using this format
                             the pandas dataframe will not have column names
        table: (string) Enter the table desired
                example 1- "table_desired"

        '''
        import sqlite3
        import pandas as pd
        data = []
        col_names = columns.split(",")
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        for row in c.execute('SELECT {} FROM {}'.format(columns, table)):
            pre_data = []
            for i in row:
                pre_data.append(i)
            data.append(pre_data)

        if columns == '*':
            return pd.DataFrame(data=data)
        else:
            return pd.DataFrame(data=data, columns=col_names)

    def make_query(self, SELECT, FROM, STATEMENT=None, query=None):

        '''
        Make basic queries using sqlite3
        ---------------------------------
        Parameters
        SELECT: (string) Enter the column or columns from the database
                 example 1- "column_desired"
                 example 2- "column_1, column_2"
                 example 3- "*" to select all columns
                 May also combined simple queries
                 example 4- "COUNT(column_desired)" or "COUNT(*)"
                 example 5- "ROUND(AVG(column_desired))"
                 example 6- "MIN(column_desired)" or "MAX(column_1, column_2)"

        FROM: (string) Enter the table desired
                 example 1- "table_desired"

        STATEMENT: (string) Enter the statement desired
                 example 1- "LIMIT"
                 example 2- "WHERE"
                 example 3- "ORDER BY"

        query: (string) Enter the an additional query after query1
                 example 1- "column_desired <= 1 OR column_desired >=8"
                 example 2- "column_desired ASC"
        '''
        import sqlite3
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        if (STATEMENT and query) == None:
            for row in c.execute('SELECT {} FROM {}'.format(SELECT, FROM)):
                print(row)

        elif (STATEMENT and query) != None:
            for row in c.execute('SELECT {} FROM {} {} {}'.format(SELECT, FROM,
                                                                  STATEMENT,
                                                                  query)):
                print(row)
