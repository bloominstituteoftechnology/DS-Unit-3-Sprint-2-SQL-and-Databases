"""
This directory contains a file `rpg_db.sqlite3`, a database for a hypothetical
webapp role-playing game. This test data has dozens-to-hundreds of randomly
generated characters across the base classes (Fighter, Mage, Cleric, and Thief)
as well as a few Necromancers. Also generated are Items, Weapons, and
connections from characters to them. Note that, while the name field was
randomized, the numeric and boolean fields were left as defaults.

Use `sqlite3` to load and write queries to explore the data, and answer the
following questions:

- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?

You do not need all the tables - in particular, the `account_*`, `auth_*`,
`django_*`, and `socialaccount_*` tables are for the application and do not have
the data you need. the `charactercreator_*` and `armory_*` tables and where you
should focus your attention. `armory_item` and `charactercreator_character` are
the main tables for Items and Characters respectively - the other tables are
subsets of them by type (i.e. subclasses), connected via a key (`item_id` and
`character_id`).

You can use the DB Browser or other tools to explore the data and work on your
queries if you wish, but to complete the assignment you should write a file
`rpg_queries.py` that imports `sqlite3` and programmatically executes and
reports results for the above queries.

Some of these queries are challenging - that's OK! You can keep working on them
tomorrow as well (we'll visit loading the same data into PostgreSQL). It's also
OK to figure out the results partially with a query and partially with a bit of
logic or math afterwards, though doing things purely with SQL is a good goal.
[Subqueries](https://www.w3resource.com/sql/subqueries/understanding-sql-subqueries.php)
and [aggregation functions](https://www.sqltutorial.org/sql-aggregate-functions/)
may be helpful for putting together more complicated queries.
"""


import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query = 'SELECT COUNT(*) FROM charactercreator_character;'
total_char = curs.execute(query).fetchone()[0]
print("How many total Characters are there? \n", total_char)


__mage = 'SELECT COUNT(*) FROM charactercreator_mage;'
__necromancer = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
__thief = 'SELECT COUNT(*) FROM charactercreator_thief;'
__cleric = 'SELECT COUNT(*) FROM charactercreator_cleric;'
__fighter = 'SELECT COUNT(*) FROM charactercreator_fighter;'
query_subclass = ['Mage', 'Necromancers', 'Thief', 'Cleric', 'Fighter']
query_subclass.append([__mage, __necromancer, __thief, __cleric, __fighter])
for subclass in range(0, 5):
    total_char_subclass = curs.execute(
        query_subclass[5][subclass]).fetchone()[0]
    print('For the subclass {} there are {} \n'.format(
        query_subclass[subclass], str(total_char_subclass)))

query_total_items = 'SELECT COUNT(*) FROM armory_item;'
total_items = curs.execute(query_total_items).fetchone()[0]
print("There are a total of {} items".format(total_items))

query_total_items__weapons = 'SELECT COUNT(*) FROM armory_weapon;'
total_items__weapons = curs.execute(query_total_items__weapons).fetchone()[0]
print("There are a total of {} items considered weapons".format(total_items__weapons))
print("There are a total of {} items not considered weapons".format(
    (total_items-total_items__weapons)))

query_total_items_character = """
    SELECT character_id, COUNT(item_id)
    FROM charactercreator_character_inventory
    GROUP BY character_id;
    """
total_items_character = curs.execute(query_total_items_character).fetchmany(20)
print(total_items_character)

query_total_items_character__weapons = """
    SELECT cci.character_id, COUNT(cci.item_id)
    FROM charactercreator_character_inventory as cci,
    armory_weapon as aw
    WHERE cci.item_id=aw.item_ptr_id
    GROUP BY character_id;
    """
total_items_character__weapons = curs.execute(
    query_total_items_character__weapons).fetchmany(20)
print(total_items_character__weapons)

query_avg_items = """
    SELECT avg(counts) as avg_item_count 
    FROM (SELECT count(*) as counts 
    FROM charactercreator_character_inventory GROUP BY character_id);
    """
avg_items = curs.execute(query_avg_items).fetchall()
print(avg_items)

query_avg_items__weapons = """
    SELECT avg(counts) as avg_item_count 
    FROM (SELECT count(*) as counts 
    FROM charactercreator_character_inventory as cci,
    armory_weapon as aw
    WHERE cci.item_id=aw.item_ptr_id
    GROUP BY character_id);
    """
avg_items__weapons = curs.execute(query_avg_items__weapons).fetchall()
print(avg_items__weapons)
