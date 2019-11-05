""" Python SQL queries"""

import pandas as pd
import sqlite3
import os
from pandas import DataFrame
from sqlalchemy import create_engine

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
print(df.shape)

df.isnull().sum()

engine = create_engine('sqlite://', echo=False)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
os.listdir()
conn
curs = conn.cursor()

