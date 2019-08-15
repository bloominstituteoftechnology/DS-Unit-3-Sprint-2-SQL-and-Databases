import pymongo
import sqlite3

SOURCE = 'C:/Users/Cactuar/Projects/DS-Unit-3-Sprint-2-SQL-and-Databases'
path = SOURCE + '/module1-introduction-to-sql/rpg_db.sqlite3'

sl_conn = sqlite3.connect(path)
sl_curs = sl_conn.cursor()

characters = sl_curs.execute(
    'SELECT * FROM charactercreator_character;'
    ).fetchall()


print(len(characters))
sl_curs.close()