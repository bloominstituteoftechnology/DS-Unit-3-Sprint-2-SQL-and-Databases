
class Load_Data():

    def __init__(self, db_file):
        self.db_file = db_file

    def create_dataframe(self, columns, table):
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
