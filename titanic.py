import sqlite3 as sql
import psycopg2 as pg
from sqlalchemy import create_engine
import os
#from dotenv import load_dotenv
import pandas as pd

titanic = pd.read_csv('titanic.csv')

URL = 'postgres://wywlalgk:vb6ja9HHMnqH2QMzocJuuGSRxJEVKHaJ@stampy.db.elephantsql.com:5432/wywlalgk'

engine = create_engine(URL)

titanic.to_sql(name="titanic_passangers", con=engine)
