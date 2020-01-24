import sqlite3
conn = sqlite3.connect('/Users/julie/Desktop/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3')

# How many total Characters are there?
cur1 = conn.cursor()
query1 = '''select count(*) from charactercreator_character;'''
a = cur1.execute(query1).fetchall()[0]
print("total Characters is : ",a[0])
cur1.close()

#How many of each specific subclass?
cur2 = conn.cursor()
query2 = '''select count(*) from charactercreator_cleric'''
b = cur2.execute(query2).fetchall()[0]
print("total charactercreator_cleric :", b[0])
cur2.close()

cur3 = conn.cursor()
query3 = '''select count(*) from charactercreator_character_inventory'''
c = cur3.execute(query3).fetchall()[0]
print("total charactercreator_character_inventory ", c[0])
cur3.close()

cur4 = conn.cursor()
query4 = '''select count(*) from charactercreator_fighter'''
d = cur4.execute(query4).fetchall()[0]
print("total charactercreator_fighter :",d[0])
cur4.close()

cur5 = conn.cursor()
query5 = '''select count(*) from charactercreator_mage'''
e = cur5.execute(query5).fetchall()[0]
print("total charactercreator_mage :",e[0])
cur5.close()

cur6 = conn.cursor()
query6 = '''select count(*) from charactercreator_necromancer'''
f = cur6.execute(query6).fetchall()[0]
print("total charactercreator_necromancer :",f[0])
cur6.close()

cur7 = conn.cursor()
query7 = '''select count(*) from charactercreator_thief'''
g = cur7.execute(query7).fetchall()[0]
print('total charactercreator_thief :',g[0])
cur7.close()

# How many total Items?
cur8 = conn.cursor()
query8 = '''select count(*) from armory_item'''
h = cur8.execute(query8).fetchall()[0]
print('total Items is :',h[0])

#How many of the Items are weapons? How many are not?
cur9 = conn.cursor()
query9 = '''select count(*) from armory_weapon'''
i = cur9.execute(query9).fetchall()[0]
print('total weapons Items is :',i[0])

print('total NON-weapons Items is :',h[0]-i[0])
cur8.close()
cur9.close()

#How many Items does each character have? (Return first 20 rows)
cur10 = conn.cursor()
query10 = '''SELECT cc.character_id, cc.name AS character_name, COUNT(ai.item_id) AS num_items
            FROM charactercreator_character AS cc,
                armory_item AS ai,
                charactercreator_character_inventory AS cci
            WHERE cc.character_id = cci.character_id
            AND ai.item_id = cci.item_id
            GROUP BY cc.character_id
            ORDER BY num_items DESC
            LIMIT 20;'''
print("\nQ：How many Items does each character have? (Return first 20 rows) :\n")
print(cur10.execute(query10).fetchall())


#How many Weapons does each character have? (Return first 20 rows)
cur11 = conn.cursor()
query11 = '''SELECT cc.character_id, cc.name AS character_name, COUNT(ai.item_ptr_id) AS num_items
                FROM charactercreator_character AS cc,
                    armory_weapon AS ai,
                    charactercreator_character_inventory AS cci
            WHERE cc.character_id = cci.character_id
            AND ai.item_ptr_id = cci.item_id
            GROUP BY cc.character_id
            ORDER BY num_items DESC
            LIMIT 20;'''
print('\n Q：How many Weapons does each character have? (Return first 20 rows):\n')
print(cur11.execute(query11).fetchall())



#On average, how many Items does each Character have?

cur12 = conn.cursor()
query12 = '''SELECT ROUND(AVG(num_items) ,2)
            FROM (
                SELECT COUNT(ai.item_id) AS num_items
                    FROM charactercreator_character AS cc,armory_item AS ai,
                        charactercreator_character_inventory AS cci
                    WHERE cc.character_id = cci.character_id
                        AND ai.item_id = cci.item_id
                        GROUP BY cc.character_id
                ) as counts;'''

print('\n Q：On average, how many Items does each Character have? :\n')
p1  = cur12.execute(query12).fetchall()[0]
print(p1[0])


#On average, how many Weapons does each character have?


cur13 = conn.cursor()
query13 = '''select round(avg(num_items),2)
            from (
                SELECT cc.character_id, cc.name AS character_name, COUNT(ai.item_ptr_id) AS num_items
                    FROM charactercreator_character AS cc,
                        armory_weapon AS ai,
                    charactercreator_character_inventory AS cci
                WHERE cc.character_id = cci.character_id
                AND ai.item_ptr_id = cci.item_id
                GROUP BY cc.character_id
                ) as counts;'''

print('\n Q：On average, how many Weapons does each Character have? :\n')
p2  = cur13.execute(query13).fetchall()[0]
print(p2[0])
cur10.close()
cur11.close()
cur12.close()
cur13.close()