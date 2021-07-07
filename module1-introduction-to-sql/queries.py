from rpg_queries import Querier

q = Querier()

# Question 1
q1 = 'SELECT COUNT(character_id) FROM charactercreator_character;'
question1result = q.query(q1)[0][0]
print('Total Characters:\t'+str(question1result))

# Question 2
tables = ['charactercreator_fighter', 'charactercreator_mage',        
          'charactercreator_cleric', 'charactercreator_thief',                  
          'charactercreator_necromancer']

counts = []
for x in tables:
    q2 = 'SELECT COUNT(*) FROM '+x+';'
    counts.append(q.query(q2)[0][0])

print('Counts of classes:\t'+str(counts))

# Question 3
q3 = 'SELECT count(item_id) FROM armory_item;'
question3result = q.query(q3)[0][0]
print('Total Items:\t'+str(question3result))

#Question 4
q4 = 'SELECT count(*) FROM armory_weapon;'
q5 = 'SELECT count(*) FROM armory_item WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);'

part1 = q.query(q4)[0][0]
part2 = q.query(q5)[0][0]

print('Total weapons:\t'+str(part1))
print('Total non-weapon items\t'+str(part2))

# Question 5 and 6
q6 = 'SELECT character_id FROM charactercreator_character'
char_id = q.query(q6)

for x in char_id[:20]:
    q0 = str('SELECT count(id) FROM charactercreator_character_inventory '+
             "WHERE character_id = '{}';".format(x[0]))
    q1 = str('SELECT count(item_id) FROM charactercreator_character_inventory '+
             "WHERE character_id = '{}' AND (item_id IN (SELECT item_ptr_id "+
             "FROM armory_weapon));").format(x[0])

    output = str('Character ID:{}\t\t'+
                 'Inventory Size:{}\t'+
                 'Weapons:{}'
                 ).format(x[0], q.query(q0)[0][0], q.query(q1)[0][0])
    print(output)

# Question 7
inventory_counts = []
for x in char_id:
    q0 = str('SELECT count(id) FROM charactercreator_character_inventory '+
             "WHERE character_id = '{}';".format(x[0]))
    inventory_counts.append(q.query(q0)[0][0])

avg = sum(inventory_counts)/question1result

print('Average Items per Character:\t'+str(avg))

# Question 8
weapon_counts = []
for x in char_id:
    q1 = str('SELECT count(item_id) FROM charactercreator_character_inventory '+
             "WHERE character_id = '{}' AND (item_id IN (SELECT item_ptr_id "+
             "FROM armory_weapon));").format(x[0])
    weapon_counts.append(q.query(q1)[0][0])

avg_weps = sum(weapon_counts)/question1result

print('Average Weapons per Character:\t'+str(avg_weps))