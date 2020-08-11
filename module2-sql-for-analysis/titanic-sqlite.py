"""
taking titanic file and transfering into sqlite3 file
"""

import pandas as pd
import sqlite3

df = pd.read_csv('titanic.csv')

conn = sqlite3.connect('titanic.sqlite3')

# df.to_sql('titanic', con=conn)

if __name__ == '__main__':
    df.to_sql('titanic', con=conn)
