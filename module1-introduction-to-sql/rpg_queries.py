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
        2: '', 
        3: '', 
        4: '', 
        5: '',
        6: ''}

total_characters = quer_fetch(queries[1])[0][0]

count_each_subclass = [quer_fetch(selcount(spec))[0][0] for spec in classes]

assert total_characters == sum(count_each_subclass)

def cartesianproducttest(l): 
    '''i think an implicit outer join was occurring in an attempt i made to combine select count queries. 
    
    it was returning four copies of a really large number rather than 4 separate smaller numbers. 
    
    this tests my hypothesis--- that the product of all 4 individuals is equal to the number i got. '''
    from functools import reduce
    assert 28090800 == reduce(lambda x,y: x*y, l)



print(total_characters)
print(count_each_subclass)

cartesianproducttest(count_each_subclass)
