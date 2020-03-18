import pandas as pd
import sqlite3
from sqlalchemy import create_engine

df = pd.read_csv('buddymove_holidayiq.csv')

engine = sqlite3.connect("buddymove_holidayiq.sqlite3")

df.to_sql('review', engine, index=False)
