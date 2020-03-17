import os
import sqlite3
from rpg_just_queries import queries

connection = sqlite3.connect("rpg_db.sqlite3")
#connection.row_factory = sqlite3.Row
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)
print('--------------')

# Could not loop through each query because each one had different instructions

result1 = cursor.execute(queries[0]).fetchall()
print('How many total Characters are there?')
print(result1[0][0])
print('------------')

result2 = cursor.execute(queries[1]).fetchall()
print('How many of each specific subclass?')
print('Cleric:',result2[0][0])
print('Fighter',result2[0][1])
print('mage',result2[0][2])
print('Necromancer',result2[0][3])
print('thief',result2[0][4])
print('------------')

result3 = cursor.execute(queries[2]).fetchall()
print('How many total Items?')
print(result3[0][0])
print('------------')

result4 = cursor.execute(queries[3]).fetchall()
print('How many of the Items are weapons? How many are not?')
print('Weapons',result4[0][0])
print('Non-weapons',result4[0][1])
print('------------')


result5 = cursor.execute(queries[4]).fetchall()
print('How many Items does each character have? (Return first 20 rows)')
for x in range(20):
    print(result5[x])
print('------------')

result6 = cursor.execute(queries[5]).fetchall()
print('How many Weapons does each character have? (Return first 20 rows)')
for x in range(20):
    print(result6[x])
print('------------')

result7 = cursor.execute(queries[6]).fetchall()
print('On average, how many Items does each Character have?')
print(result7[0][0])
print('------------')

result8 = cursor.execute(queries[7]).fetchall()
print('On average, how many Weapons does each character have?')
print(result8[0][0])
print('------------')