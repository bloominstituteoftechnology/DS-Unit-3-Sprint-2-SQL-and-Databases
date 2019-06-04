import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query = 'SELECT COUNT(*) FROM charactercreator_character;'

result = curs.execute(query)

# total Characters 
print('Q1: Total Characters: ', (result.fetchall()[0][0]))

query = """SELECT (
                SELECT COUNT(*)
                FROM charactercreator_cleric
                ) AS 'Cleric Characters',
                (
                SELECT COUNT(*)
                FROM charactercreator_fighter
                ) AS 'Fighter Characters',
                (
                SELECT COUNT(*)
                FROM charactercreator_thief
                ) AS 'Thief Characters',
                (
                SELECT COUNT(*)
                FROM charactercreator_mage
                ) AS 'Mage Characters',
                (
                SELECT COUNT(*)
                FROM charactercreator_necromancer
                ) AS 'Necromancer Characters';"""

result = curs.execute(query)

num = result.fetchall()

#Initialize List
data = [['Cleric', print(num[0][0])], 
        ['Fighter',print(num[0][1])], 
        ['Thief',print(num[0][2])], 
        ['Mage', print(num[0][3])], 
        ['Necromancer', print(num[0][4])]]
#Create Table
df_subclass_totals = pd.DataFrame(data, columns=['Subclass', 'Count'])

df_subclass_totals

# # print(num[0][2])
# print(Q2:'Specific Subclass Totals ')
# # print()
# # print("Cleric Total: ", (result.fetchall()[0][0]))
# # # print("Fighter Total: ", (result.fetchall()[0]))