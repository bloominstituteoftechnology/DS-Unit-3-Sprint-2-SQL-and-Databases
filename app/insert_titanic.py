import os
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import sqlite3
import pandas as pd
DB_FILEPATH = os.path.join(os.path.dirname(__file__), '..','data', 'titanic.csv')
df = pd.read_csv('DB_FILEPATH')
df.head()