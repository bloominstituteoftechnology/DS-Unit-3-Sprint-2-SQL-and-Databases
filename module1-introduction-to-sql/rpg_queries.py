import sqlite3
import pandas as pd

# Establish Connection
conn = sqlite3.connect('rpg_db.sqlite3')

# Define cursor
curs = conn.cursor()

# Q1: How many total Characters are there?
# Define query
query1 = """SELECT COUNT(*) FROM charactercreator_character;"""

# Execute query 
result = curs.execute(query1)

# Print Total Characters 
print('Q1: Total Characters: ', (result.fetchall()[0][0]))


# Q2: EACH SPECIFIC SUBCLASS
query2 = """SELECT (
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

result = curs.execute(query2)

num = result.fetchall()

# Print Q2:
print('Q2:')

#Initialize List
data = [['Cleric', print(num[0][0])], #75
        ['Fighter',print(num[0][1])], #68
        ['Thief',print(num[0][2])], #51
        ['Mage', print(num[0][3])], #108
        ['Necromancer', print(num[0][4])]] #11
#Create Table
df_subclass_totals = pd.DataFrame(data, columns=['Subclass', 'Count'])

# View Table
df_subclass_totals

# Q3: Total Items?

query3 = """SELECT COUNT(*)
            AS 'TOTAL ITEMS'
        FROM armory_item;"""

result = curs.execute(query3) 

print('Q3: Total Items: ' , result.fetchall()[0][0])

# Q4: Items = weapons? Items != Weapons? 

query4 = """SELECT (
            SELECT count(*)
            FROM armory_weapon
            ) AS 'Total Weapon',
            (
            SELECT COUNT(item_id)
            FROM armory_item
            WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)
            ) AS 'Non-Weapons';"""

result = curs.execute(query4)

print('Q4: Total Weapon and Non Weapons: ', result.fetchall()[0])

# Q5: How many items do each character have? (20 rows)

query5 = """SELECT COUNT(item_id) AS 'Item Count'
            FROM charactercreator_character_inventory
            GROUP BY character_id
            LIMIT 20"""

result = curs.execute(query5)

print('Q5: Items each character: ', result.fetchall())

query6 = """SELECT COUNT(item_id) AS 'Item Count'
            FROM charactercreator_character_inventory
            WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
            GROUP BY character_id
            LIMIT 20"""

result = curs.execute(query6)

print('Q6: weapons each character: ', result.fetchall())

# Q7: On average, how many items does each character have? 

query7 = """SELECT ROUND(1.0 * COUNT(item_id) / 
                        COUNT( DISTINCT character_id), 2) 
                  AS 'Avg. Items/Character'   
           FROM charactercreator_character_inventory"""

result = curs.execute(query7)

print('Q7: Average Items Each Character: ', result.fetchall()[0][0])

# Q8: Average weapons each character

query8 = """SELECT ROUND(AVG(item_counts),2) AS 'Avg. Weapons Per Character'
           FROM (SELECT count(inventory.item_id) as item_counts
            from charactercreator_character_inventory as inventory
            INNER JOIN armory_weapon
            ON inventory.item_id = armory_weapon.item_ptr_id
            GROUP BY inventory.character_id)"""

result = curs.execute(query8)

print('Q8: Average weapons each character: ', result.fetchall()[0][0])

