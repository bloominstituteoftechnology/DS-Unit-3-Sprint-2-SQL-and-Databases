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
# first *get* the first 20 characters
print()
print('Item counts of first 20 characters:')
ids = list(map(lambda x: x[0], runq(curs, '''
  SELECT `character_id`
  FROM `charactercreator_character`
  ORDER BY `character_id`
  LIMIT 20;
''')))

# then figure out how many items they have
# this can all be done in a single SQL query, dontchaknow
for chid in ids:
  c = runq(curs, '''
    SELECT COUNT(`item_id`)
    FROM `charactercreator_character_inventory`
    WHERE `character_id` = ''' + str(chid) + ''';
  ''')[0][0]
  noun = 'item' if c == 1 else 'items'
  print(f'Character {chid} has {c} {noun}! ;D')

# how many weapons do those 20 characters have?
print()
print('Weapon counts of first 20 characters:')
for chid in ids:
  c = runq(curs, '''
    SELECT COUNT(`charactercreator_character_inventory`.`item_id`)
    FROM `charactercreator_character_inventory`
      INNER JOIN `armory_item`
        ON `charactercreator_character_inventory`.`item_id` = `armory_item`.`item_id`
      INNER JOIN `armory_weapon`
        ON `armory_item`.`item_id` = `armory_weapon`.`item_ptr_id`
    WHERE `charactercreator_character_inventory`.`character_id` = ''' + str(chid) + ''';
  ''')[0][0]
  noun = 'weapon' if c == 1 else 'weapons'
  print(f'Character {chid} has {c} {noun}! XD')

# what is the average item count per character?
print()
counts = list(map(lambda x: x[0], runq(curs, '''
  SELECT COUNT(`item_id`)
  FROM `charactercreator_character_inventory`
  GROUP BY `character_id`;
''')))
avg = sum(counts) / len(counts)
noun = 'item' if avg == 1.0 else 'items'
print(f'On average, every character has {avg} {noun}! ,:)')

# what is the average weapon count per character?
counts = list(map(lambda x: x[0], runq(curs, '''
  SELECT COUNT(`item_ptr_id`)
  FROM `charactercreator_character_inventory`
    INNER JOIN `armory_item`
      ON `armory_item`.`item_id` = `charactercreator_character_inventory`.`item_id`
    INNER JOIN `armory_weapon`
      ON `armory_item`.`item_id` = `item_ptr_id`
  GROUP BY `character_id`
''')))
avg = sum(counts) / len(counts)
noun = 'weapon' if avg == 1.0 else 'weapons'
print(f'On average, every character has {avg} {noun}! ,:)')

# all done that's enough
curs.close()
khan.commit()