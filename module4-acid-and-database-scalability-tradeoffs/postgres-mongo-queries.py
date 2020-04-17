
import pymongo
import psycopg2
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def main():
    print()
    print('Mongo Queries')
    print('------------------------------------------------------------------')
    mongo_queries()

    print()
    print('Postgres Queries')
    print('------------------------------------------------------------------')
    postgres_queries()

def mongo_queries():
    #connect to mongo db
    USER = os.getenv('MONGO_USER', default = 'oops')
    PASSWORD = os.getenv('MONGO_PASSWORD', default = 'oops')
    CLUSTER = os.getenv('MONGO_CLUSTER', default = 'oops')

    uri = f'mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}.mongodb.net/test?retryWrites=true&w=majority'

    client = pymongo.MongoClient(uri)

    db = client['rpg_db']

    
    # How many total Characters are there?
    tot_char = db['charactercreator_character'].count_documents({})
    print('Total Characters:', tot_char)

    # How many of each subclass?
    tot_cleric = db['charactercreator_cleric'].count_documents({})
    tot_fighter = db['charactercreator_fighter'].count_documents({})
    tot_mage = db['charactercreator_mage'].count_documents({})
    tot_necro = db['charactercreator_necromancer'].count_documents({})
    tot_thief = db['charactercreator_thief'].count_documents({})
    print('Clerics:', tot_cleric)
    print('Fighters:', tot_fighter)
    print('Mages:', tot_mage - tot_necro)
    print('Necromancer:', tot_necro)
    print('Thieves:', tot_thief)
    print('Sum:', tot_cleric + tot_fighter + (tot_mage - tot_necro) + tot_necro + tot_thief)

    # How many total items?
    tot_items = db['armory_item'].count_documents({})
    print('Total Items:', tot_items)

    # How many items are weapons? 
    tot_weapons = db['armory_weapon'].count_documents({})
    print('Total Weapons:', tot_weapons)

    # How many are not?
    # there is a cooler way to do this with filters, projections and using the
    # find method. Its also really cumbersome, so I'm doing it the easy way.
    print('Total Non-Weapons:', tot_items - tot_weapons)

    # How many items does each character have? (first 20)
    
    #this projection is to clear all the fields exept character_id, which I
    # will then use to count the documents for each. This is not very mongolike
    # because this is a clone of an sql database.  Ideally I'd keep a list of
    # the mongo hashes, or something like that.
    proj = {'_id': 0, 'dexterity': 0, 'exp': 0, 'hp': 0, 'intelligence': 0,
            'level': 0, 'name': 0, 'strength': 0, 'wisdom': 0}
    to_find = db['charactercreator_character'].find({}, projection = proj).limit(20)

    for doc in to_find:
        id = doc['character_id']

        # I only want item id
        proj = {'_id': 0, 'id': 0, 'character_id': 0}
        item_list = list(db['charactercreator_character_inventory'].find(doc, proj))

        # I could get this with a query, but it is also implicit with how I'm
        # identifying weapons.  So lets reduce the queries, thus reducing server
        # load.  Here is how I'd do it with a single query:
        # item_count = db['charactercreator_character_inventory'].count_documents(doc)
        item_count = len(item_list)

        # I can't see away around querying every single item idea a character
        # has.  This seem absurdly inefficient.  I'm blaming my inexperience 
        # and no clear pymongo documentation for array based searching (which
        # mongodb does support from the shell)
        prepped = [{'item_ptr_id': i['item_id']} for i in item_list]

        weapon_count = 0

        for i in prepped:
            weapon_count += db['armory_weapon'].count_documents(i)

        print(f'Character {id} has {item_count} items, of which {weapon_count} are weapons')

    # Average, how many items does each character have?
    # TODO

    # Average, how many Weapons does each character have?
    # TODO

def postgres_queries():
    #Connect to postgres
    HOST = os.getenv('POST_HOST', default = 'oops')
    NAME = os.getenv('POST_NAME', default = 'oops')
    USER = os.getenv('POST_USER', default = 'oops')
    PASSWORD = os.getenv('POST_PASSWORD', default = 'oops')

    con = psycopg2.connect(dbname = NAME,
                            user = USER,
                            password = PASSWORD,
                            host = HOST)

    cur = con.cursor()

    # How many passengers survived, and how many died?
    q1 = '''
    SELECT count(survived) as count
    FROM passengers
    WHERE survived = 1
    '''

    cur.execute(q1)

    surv = cur.fetchone()[0]

    print(f'There are a total of {surv} survivors')

    # How many passengers were in each class?
    q2 = '''
    SELECT count(survived) as passengers
        ,pclass as class
    FROM passengers
    GROUP BY pclass
    ORDER BY pclass
    '''

    cur.execute(q2)
    resp = cur.fetchall()

    for row in resp:
        print(str(row[0]) + ' passengers in ' + str(row[1]) + ' class')

    # How many passengers survived/died within each class?
    q3 = '''
    SELECT count(survived) as survivors
        ,pclass as class
    FROM passengers
    WHERE survived = 1
    GROUP BY pclass
    ORDER BY pclass
    '''

    cur.execute(q3)
    resp = cur.fetchall()

    for row in resp:
        print(str(row[0]) + ' passengers in ' + str(row[1]) + ' class survived')

    q4 = '''
    SELECT count(survived) as survivors
        ,pclass as class
    FROM passengers
    WHERE survived = 0
    GROUP BY pclass
    ORDER BY pclass
    '''

    cur.execute(q4)
    resp = cur.fetchall()

    for row in resp:
        print(str(row[0]) + ' passengers in ' + str(row[1]) + ' class died')

    # What was the average age of survivors vs nonsurvivors?
    q5 = '''
    SELECT avg(age) as avgerage_age
        ,survived
    FROM passengers
    GROUP BY survived
    ORDER BY survived
    '''

    cur.execute(q5)
    resp = cur.fetchall()

    print('The average age of survivors is', resp[0][0])
    print('The average age of nonsurvivors is', resp[1][0])

    # What was the average age of each passenger class?
    q6 = '''
    SELECT avg(age) as average_age
        ,pclass as class
    FROM passengers
    GROUP BY pclass
    ORDER BY pclass
    '''

    cur.execute(q6)
    resp = cur.fetchall()

    for row in resp:
        print('The average age of ' + str(row[1]) + ' class passengers is ' + str(round(row[0])))

    # What was the average fare by passenger class? By survival?
    q7 = '''
    SELECT avg(fare::numeric) as average_fare
        ,pclass as class
    FROM passengers
    GROUP BY pclass
    ORDER By pclass
    '''

    cur.execute(q7)
    resp = cur.fetchall()

    for row in resp:
        print('The average fare of ' + str(row[1]) + ' class passengers is ' + str(round(row[0], 2)))

    q8 = '''
    SELECT avg(fare::numeric) as average_fare
        ,survived
    FROM passengers
    GROUP BY survived
    ORDER By survived
    '''

    cur.execute(q8)
    resp = cur.fetchall()

    print('The average fare of survivors is', round(resp[0][0], 2))
    print('The average fare of nonsurvivors is', round(resp[1][0], 2))
    
    # How many siblings/spouses aboard on average, by passenger class? by Survival?
    # ew, this is kinda ugly, I would probably never do it like this I'm just
    # getting tired of writing queries
    q9 = '''
    SELECT *
    FROM(SELECT avg(siblings_spouse) as avg_sib_spo
            ,pclass
        FROM passengers
        GROUP BY pclass
        ORDER BY pclass) c
    FULL OUTER JOIN(SELECT avg(siblings_spouse) as avg_sib_spo
            ,survived
        FROM passengers
        GROUP BY survived
        ORDER BY survived) s ON s.avg_sib_spo = c.avg_sib_spo
    '''

    cur.execute(q9)
    resp = cur.fetchall()

    print('The average siblings/spouses for first class is', round(resp[0][0], 2))
    print('The average siblings/spouses for first class is', round(resp[1][0], 2))
    print('The average siblings/spouses for first class is', round(resp[2][0], 2))
    print('The average siblings/spouses for survivors is', round(resp[3][2], 2))
    print('The average siblings/spouses for survivors is', round(resp[4][2], 2))

    # How many paretns/children aboard on average, by passenger class? by survival?
    q10 = '''
    SELECT *
    FROM(SELECT avg(parents_children) as p_c
            ,pclass
        FROM passengers
        GROUP BY pclass
        ORDER BY pclass) c
    FULL OUTER JOIN(SELECT avg(parents_children) as p_c
            ,survived
        FROM passengers
        GROUP BY survived
        ORDER BY survived) s ON s.p_c = c.p_c
    '''

    cur.execute(q10)
    resp = cur.fetchall()

    print('The average parents/children for first class is', round(resp[0][0], 2))
    print('The average parents/children for first class is', round(resp[1][0], 2))
    print('The average parents/children for first class is', round(resp[2][0], 2))
    print('The average parents/children for survivors is', round(resp[3][2], 2))
    print('The average parents/children for survivors is', round(resp[4][2], 2))

    # Do any passengers have the same name?
    q11 = '''
    SELECT count(distinct name) as unique_names
        ,count(name) as total_names
    FROM passengers
    '''

    cur.execute(q11)
    resp = cur.fetchone()

    if resp[0] == resp[1]:
        print('No passengers have the same name')
    else:
        print('Some passengers have the same name')

    cur.close()
    con.close()

if __name__ == "__main__":
    main()