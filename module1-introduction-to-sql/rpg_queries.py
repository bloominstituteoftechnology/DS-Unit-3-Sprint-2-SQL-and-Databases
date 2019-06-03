import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Q1: How many total characters are there? 

query = """SELECT COUNT(character_id) as 'Count of Characters'
           FROM charactercreator_character"""
result = curs.execute(query)

print('Q1: How many total characters are there?')
print(result.fetchall()[0][0])

# Q2: How many of each specific subclass?

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

print('Q2: How many of each specific subclass?')
print(result.fetchall()[0])

# Q3: How many total items?

query = """SELECT count(*) as 'Total Items'
           FROM armory_item;"""

result = curs.execute(query)

print('Q3: How many total items?')
print(result.fetchall()[0][0])

# Q4: How many of the Items are weapons? How many are not? 

query = """SELECT (
            SELECT count(*)
            FROM armory_weapon
            ) AS 'Total Weapon Types',
            (
            SELECT COUNT(item_id)
            FROM armory_item
            WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)
            ) AS 'Non-Weapons Types';"""

result = curs.execute(query)

print('Q4: How many of the Items are weapons? How many are not?')
print(result.fetchall()[0])

# Q5: How many items does each character have? (Return First 20 Rows)

query = """SELECT COUNT(item_id) AS 'Item Count'
           FROM charactercreator_character_inventory
           GROUP BY character_id
           LIMIT 20"""

result = curs.execute(query)

print('Q5: How many items does each character have? (Return First 20 Rows)')
print(result.fetchall())

# Q6: How many weapons does each character have? 

query = """SELECT COUNT(item_id) AS 'Item Count'
            FROM charactercreator_character_inventory
            WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
            GROUP BY character_id
            LIMIT 20"""

result = curs.execute(query)

print('Q6: How many weapons does each character have?')
print(result.fetchall())

# Q7: On average, how many items does each character have? 

query = """SELECT ROUND(1.0 * COUNT(item_id) / 
                        COUNT( DISTINCT character_id), 2) 
                  AS 'Avg. Items/Character'   
           FROM charactercreator_character_inventory"""

result = curs.execute(query)

print('Q7: On average, how many items does each character have?')
print(result.fetchall()[0][0])

# Q8: On Average, How many weapons does each character have? 

query = """SELECT ROUND(AVG(item_counts),2) AS 'Avg. Weapons Per Character'
           FROM (SELECT count(inventory.item_id) as item_counts
            from charactercreator_character_inventory as inventory
            INNER JOIN armory_weapon
            ON inventory.item_id = armory_weapon.item_ptr_id
            GROUP BY inventory.character_id)"""

result = curs.execute(query)

print('Q8: On Average, How many weapons does each character have?')
print(result.fetchall()[0][0])