import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.head())
print(df.shape)
print(df.isnull().sum())
