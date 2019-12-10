import sqlite3
runq = lambda c, q: c.execute(q).fetchall()

# connect to db & prepare for queryin'
khan = sqlite3.connect('rpg_db.sqlite3')
curs = khan.cursor()

# how many characters?
def dispnum(x, noun):
  singular = x == 1
  verb = 'is' if singular else 'are'
  noun = noun if singular else f'{noun}s'
  print(f'There {verb} {x} {noun} in this game! :D')

def quickp(n, q):
  dispnum(runq(curs, q)[0][0], n)

quickp('character', 'SELECT COUNT(`character_id`) FROM `charactercreator_character`;')

# how many mages?
quickp('mage', 'SELECT COUNT(`character_ptr_id`) FROM `charactercreator_mage`;')

# how many necros?
quickp('necromancer', 'SELECT COUNT(`mage_ptr_id`) FROM `charactercreator_necromancer`')

# how many thiefs?
quickp('thief', 'SELECT COUNT(`character_ptr_id`) FROM `charactercreator_thief`;')

# how many clerics?
quickp('cleric', 'SELECT COUNT(`character_ptr_id`) FROM `charactercreator_cleric`;')

# how many fighters?
quickp('fighter', 'SELECT COUNT(`character_ptr_id`) FROM `charactercreator_fighter`;')

# how many items?
quickp('item', 'SELECT COUNT(`item_id`) FROM `armory_item`;')

# how many weapons?
quickp('weapon', 'SELECT COUNT(`item_ptr_id`) FROM `armory_weapon`;')

# how many non-weapons?
quickp('non-weapon', '''
  SELECT COUNT(`item_id`)
  FROM `armory_item`
    LEFT JOIN `armory_weapon`
    ON `armory_item`.`item_id` = `armory_weapon`.`item_ptr_id`
  WHERE `item_ptr_id` IS NULL;
''')

# how many items for each character? (first 20)
print()
print('Item counts of first 20 characters:')
counts = runq(curs, '''
  SELECT `name`, COUNT(`item_id`)
  FROM `charactercreator_character`
  LEFT JOIN `charactercreator_character_inventory`
  GROUP BY `name`
  ORDER BY `name`
  LIMIT 20;
''')

for x in counts:
  print(f' - {x[0]}: {x[1]}')

# all done that's enough
curs.close()
khan.commit()