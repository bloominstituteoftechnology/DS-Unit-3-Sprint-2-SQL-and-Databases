'''
ASSIGNMENT: construct sql commands for the following questions.

    1: How many total Characters are there?
    2: How many of each specific subclass?
    3: How many total Items?
    4: How many of the Items are weapons? How many are not?
    5: On average, how many Items does each Character have?
    6: On average, how many Weapons does each character have?
'''
import sqlite3 as sl
from numpy import divide as div
from numpy import mean
from functools import reduce

conn = sl.connect('rpg_db.sqlite3')

def quer_fetch(query):
    c = conn.cursor() 

    c.execute(query)

    return c.fetchall()

classes = ['cleric', 'fighter', 'mage', 'thief']

def selcount(tab): 
    q = lambda s: f'SELECT COUNT(*) FROM charactercreator_{s};'
    return q(tab)

queries = {1: selcount('character'), 
           2: '<~ this is too complicated because its four different queries rn~>', 
           3: 'SELECT COUNT(*) FROM armory_item;', 
           4: 'SELECT COUNT(*) FROM armory_weapon', 
           5: 'SELECT COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id;',
           6: '''SELECT COUNT(item_id) 
                FROM charactercreator_character_inventory as invs
                JOIN armory_weapon as weap
                ON weap.item_ptr_id = invs.item_id
                GROUP BY character_id;'''}

total_characters = quer_fetch(queries[1])[0][0]

count_each_subclass = [quer_fetch(selcount(spec))[0][0] for spec in classes]

assert total_characters == sum(count_each_subclass)

def cartesianproducttest(l): 
    '''i think an implicit outer join was occurring in an attempt i made to combine select count queries. 
    
    it was returning four copies of a really large number rather than 4 separate smaller numbers. 
    
    this tests my hypothesis--- that the product of all 4 individuals is equal to the number i got. '''
    
    assert 28090800 == reduce(lambda x,y: x*y, l)
    pass 

total_items = quer_fetch(queries[3])[0][0]
weapons_count = quer_fetch(queries[4])[0][0]

items_list = [t[0] for t in quer_fetch(queries[5])]

weaps_list = [t[0] for t in quer_fetch(queries[6])]

print(f'there are {total_characters} characters. ')
print(reduce(lambda s,t: s+t, [f'there are {num} {cla}s. ' for num,cla in zip(count_each_subclass, classes)]))

cartesianproducttest(count_each_subclass)

print(f'there are {total_items} total items')

print(f'{total_items-weapons_count} is the number of non-weapon items. ')

print(f'The mean number of items each character carries is {mean(items_list):.3}')

print(f'The mean number of weapons carried by a character is {mean(weaps_list):.3}')

