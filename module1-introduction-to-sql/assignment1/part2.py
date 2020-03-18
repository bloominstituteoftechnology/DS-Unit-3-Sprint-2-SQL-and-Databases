import pandas as pd
import os
import sqlite3

file_path = '../buddymove_holidayiq.csv'

df = pd.read_csv(file_path)

print(df.head())
