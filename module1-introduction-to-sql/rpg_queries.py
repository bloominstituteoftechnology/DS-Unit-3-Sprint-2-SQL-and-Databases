import sqlite3
import pandas as pd
from read_db import*

df = Read_DB('rpg_db.sqlite3')

print(df.create("*", "armory_item"))
