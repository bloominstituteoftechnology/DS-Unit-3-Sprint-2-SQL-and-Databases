import sqlite3
import pandas as pd
from read_db import*

df = Load_Data('rpg_db.sqlite3')

print(df.create_dataframe("*", "armory_item"))
