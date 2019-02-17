import sqlite3
from read_db import*

df = Read_DB('rpg_db.sqlite3')

df.read_db("*", "armory_item")
