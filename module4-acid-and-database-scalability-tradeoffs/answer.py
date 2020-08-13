import pandas as pd
import psycopg2
import pymongo
import sqlite3


def create_characters(db):
    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the charactercreator_character table
    get_characters = "SELECT * FROM charactercreator_character;"
    characters = sl_curs.execute(get_characters).fetchall()

    db.characters.drop()

    for i in range(len(characters)):
        characters_doc = {
            "doc_type": "characters",
            "character_id": characters[i][0],
            "name": characters[i][1],
            "level": characters[i][2],
            "exp": characters[i][3],
            "hp": characters[i][4],
            "strength": characters[i][5],
            "intelligence": characters[i][6],
            "dexterity": characters[i][7],
            "wisdom": characters[i][8],
        }
        db.characters.insert_one(characters_doc)

    sl_curs.close()
    sl_conn.close()


def create_fighters(db):
    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the charactercreator_fighter table
    get_fighters = "SELECT * FROM charactercreator_fighter;"
    fighters = sl_curs.execute(get_fighters).fetchall()

    db.fighters.drop()

    for i in range(len(fighters)):
        fighters_doc = {
            "doc_type": "fighters",
            "character_ptr_id": fighters[i][0],
            "using_shield": fighters[i][1],
            "rage": fighters[i][2],
        }
        db.fighters.insert_one(fighters_doc)

    sl_curs.close()
    sl_conn.close()


def create_mages(db):
    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the charactercreator_mage table
    get_mages = "SELECT * FROM charactercreator_mage;"
    mages = sl_curs.execute(get_mages).fetchall()

    db.mages.drop()

    for i in range(len(mages)):
        mages_doc = {
            "doc_type": "mages",
            "character_ptr_id": mages[i][0],
            "has_pet": mages[i][1],
            "mana": mages[i][2],
        }
        db.mages.insert_one(mages_doc)

    sl_curs.close()
    sl_conn.close()


def create_clerics(db):
    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the charactercreator_cleric table
    get_clerics = "SELECT * FROM charactercreator_cleric;"
    clerics = sl_curs.execute(get_clerics).fetchall()

    db.clerics.drop()

    for i in range(len(clerics)):
        clerics_doc = {
            "doc_type": "clerics",
            "character_ptr_id": clerics[i][0],
            "using_shield": clerics[i][1],
            "mana": clerics[i][2],
        }
        db.clerics.insert_one(clerics_doc)

    sl_curs.close()
    sl_conn.close()


def create_thiefs(db):
    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the charactercreator_thief table
    get_thiefs = "SELECT * FROM charactercreator_thief;"
    thiefs = sl_curs.execute(get_thiefs).fetchall()

    db.thiefs.drop()

    for i in range(len(thiefs)):
        thiefs_doc = {
            "doc_type": "thiefs",
            "character_ptr_id": thiefs[i][0],
            "is_sneaking": thiefs[i][1],
            "energy": thiefs[i][2],
        }
        db.thiefs.insert_one(thiefs_doc)

    sl_curs.close()
    sl_conn.close()


def create_necromancers(db):
    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the charactercreator_necromancer table
    get_necromancers = "SELECT * FROM charactercreator_necromancer;"
    necromancers = sl_curs.execute(get_necromancers).fetchall()

    db.necromancers.drop()

    for i in range(len(necromancers)):
        necromancers_doc = {
            "doc_type": "necromancers",
            "mage_ptr_id": necromancers[i][0],
            "talisman_charged": necromancers[i][1],
        }
        db.necromancers.insert_one(necromancers_doc)

    sl_curs.close()
    sl_conn.close()


def create_items(db):
    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the armory_item table
    get_items = "SELECT * FROM armory_item;"
    items = sl_curs.execute(get_items).fetchall()

    db.items.drop()

    for i in range(len(items)):
        items_doc = {
            "doc_type": "items",
            "item_id": items[i][0],
            "name": items[i][1],
            "value": items[i][2],
            "weight": items[i][3],
        }
        db.items.insert_one(items_doc)

    sl_curs.close()
    sl_conn.close()


def create_weapons(db):
    # Step 1 - Extract, getting data out of SQLite3
    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    # Our goal - copy the armory_weapon table
    get_weapons = "SELECT * FROM armory_weapon;"
    weapons = sl_curs.execute(get_weapons).fetchall()

    db.weapons.drop()

    for i in range(len(weapons)):
        weapons_doc = {
            "doc_type": "weapons",
            "item_ptr_id": weapons[i][0],
            "power": weapons[i][1],
        }
        db.weapons.insert_one(weapons_doc)

    sl_curs.close()
    sl_conn.close()


if __name__ == "__main__":
    # Given code to connect to Mongo
    password = (  # Don't commit/share this! Reset it if it leaks
        "EtZkty4uluNwiVyb"
    )
    dbname = "rpg"
    client = pymongo.MongoClient(
        "mongodb+srv://xpandalord:"
        + password
        + "@cluster0.q6n34.mongodb.net/"
        + dbname
        + "?retryWrites=true&w=majority"
    )
    db = client.rpg

    # How many total Characters are there?
    # create_characters(db)
    num_characters = len(list(db.characters.find({"doc_type": "characters"})))
    print("There are %d total Characters." % (num_characters))

    # How many of each specific subclass?
    # create_fighters(db)
    num_fighters = len(list(db.fighters.find({"doc_type": "fighters"})))
    print("There are %d total Fighters." % (num_fighters))

    # create_mages(db)
    num_mages = len(list(db.mages.find({"doc_type": "mages"})))
    print("There are %d total Mages." % (num_mages))

    # create_clerics(db)
    num_clerics = len(list(db.clerics.find({"doc_type": "clerics"})))
    print("There are %d total Clerics." % (num_clerics))

    # create_thiefs(db)
    num_thiefs = len(list(db.thiefs.find({"doc_type": "thiefs"})))
    print("There are %d total Thiefs." % (num_thiefs))

    # create_necromancers(db)
    num_necromancers = len(
        list(db.necromancers.find({"doc_type": "necromancers"}))
    )
    print("There are %d total Necromancers." % (num_necromancers))

    # How many total Items?
    # create_items(db)
    num_items = len(list(db.items.find({"doc_type": "items"})))
    print("There are %d total Items." % (num_items))

    # How many of the Items are weapons? How many are not?
    # create_weapons(db)
    num_weapons = len(list(db.weapons.find({"doc_type": "weapons"})))
    print("There are %d total Weapons." % (num_weapons))
    non_weapons = len(
        list(db.items.find({"doc_type": "items", "item_id": {"$lt": 138}}))
    )
    print("There are %d total Non-Weapons." % (non_weapons))

    # Looks similar to sqlite3, but needs auth/host info to connect
    # Note - this is sensitive info (particularly password)
    # and shouldn't be checked into git! More on how to handle next week

    dbname = "ajkuvccu"
    user = "ajkuvccu"  # ElephantSQL happens to use same name for db and user
    password = (  # Sensitive! Don't share/commit
        "FBOFpSpFdAFrxYUG-DBqN39wDQ0Mjc4V"
    )
    host = "isilo.db.elephantsql.com"

    # If we make too many connections, the database complains! Be sure to close
    # cursors and connections
    pg_conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host
    )

    pg_curs = pg_conn.cursor()  # Works the same as SQLite!

    # How many passengers survived, and how many died?
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Survived" = 1;'
    )
    print("%d passengers survived." % (pg_curs.fetchall()[0][0]))
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Survived" = 0;'
    )
    print("%d passengers died." % (pg_curs.fetchall()[0][0]))

    # How many passengers were in each class?
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Pclass" = 1;'
    )
    print("%d passengers were from class 1." % (pg_curs.fetchall()[0][0]))
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Pclass" = 2;'
    )
    print("%d passengers were from class 2." % (pg_curs.fetchall()[0][0]))
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Pclass" = 3;'
    )
    print("%d passengers were from class 3." % (pg_curs.fetchall()[0][0]))

    # How many passengers survived/died within each class?
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Survived" = 1 AND'
        ' "Pclass" = 1;'
    )
    print(
        "%d passengers survived and were from class 1."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Survived" = 1 AND'
        ' "Pclass" = 2;'
    )
    print(
        "%d passengers survived and were from class 2."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Survived" = 1 AND'
        ' "Pclass" = 3;'
    )
    print(
        "%d passengers survived and were from class 3."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Survived" = 0 AND'
        ' "Pclass" = 1;'
    )
    print(
        "%d passengers died and were from class 1."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Survived" = 0 AND'
        ' "Pclass" = 2;'
    )
    print(
        "%d passengers died and were from class 2."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT COUNT(*) FROM titanic_postgres WHERE "Survived" = 0 AND'
        ' "Pclass" = 3;'
    )
    print(
        "%d passengers died and were from class 3."
        % (pg_curs.fetchall()[0][0])
    )

    # What was the average age of survivors vs nonsurvivors?
    pg_curs.execute(
        'SELECT AVG("Age") FROM titanic_postgres WHERE "Survived" = 1;'
    )
    print(
        "The average age of passengers who survived  was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Age") FROM titanic_postgres WHERE "Survived" = 0;'
    )
    print(
        "The average died of passengers who survived  was %f."
        % (pg_curs.fetchall()[0][0])
    )

    # What was the average age of each passenger class?
    pg_curs.execute(
        'SELECT AVG("Age") FROM titanic_postgres WHERE "Pclass" = 1;'
    )
    print(
        "The average age of passengers who were from class 1 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Age") FROM titanic_postgres WHERE "Pclass" = 2;'
    )
    print(
        "The average age of passengers who were from class 2 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Age") FROM titanic_postgres WHERE "Pclass" = 3;'
    )
    print(
        "The average age of passengers who were from class 3 was %f."
        % (pg_curs.fetchall()[0][0])
    )

    # What was the average fare by passenger class? By survival?
    pg_curs.execute(
        'SELECT AVG("Fare") FROM titanic_postgres WHERE "Pclass" = 1;'
    )
    print(
        "The average fare of passengers who were from class 1 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Fare") FROM titanic_postgres WHERE "Pclass" = 2;'
    )
    print(
        "The average fare of passengers who were from class 2 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Fare") FROM titanic_postgres WHERE "Pclass" = 3;'
    )
    print(
        "The average fare of passengers who were from class 3 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Fare") FROM titanic_postgres WHERE "Survived" = 1'
    )
    print(
        "The average fare of passengers who survived was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Fare") FROM titanic_postgres WHERE "Survived" = 0'
    )
    print(
        "The average fare of passengers who died was %f."
        % (pg_curs.fetchall()[0][0])
    )

    # How many siblings/spouses aboard on average, by passenger class? By survival?
    pg_curs.execute(
        'SELECT AVG("Siblings/Spouses Aboard") FROM titanic_postgres WHERE'
        ' "Pclass" = 1;'
    )
    print(
        "The average number of passengers' siblings/spouses aboard who"
        " were from class 1 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Siblings/Spouses Aboard") FROM titanic_postgres WHERE'
        ' "Pclass" = 2;'
    )
    print(
        "The average number of passengers' siblings/spouses aboard who"
        " were from class 2 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Siblings/Spouses Aboard") FROM titanic_postgres WHERE'
        ' "Pclass" = 3;'
    )
    print(
        "The average number of passengers' siblings/spouses aboard who"
        " were from class 3 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Siblings/Spouses Aboard") FROM titanic_postgres WHERE'
        ' "Survived" = 1'
    )
    print(
        "The average number of passengers' siblings/spouses aboard who"
        " survived was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Siblings/Spouses Aboard") FROM titanic_postgres WHERE'
        ' "Survived" = 0'
    )
    print(
        "The average number of passengers' siblings/spouses aboard who"
        " died was %f."
        % (pg_curs.fetchall()[0][0])
    )

    # How many parents/children aboard on average, by passenger class? By survival?
    pg_curs.execute(
        'SELECT AVG("Parents/Children Aboard") FROM titanic_postgres WHERE'
        ' "Pclass" = 1;'
    )
    print(
        "The average number of passengers' parents/children aboard who"
        " were from class 1 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Parents/Children Aboard") FROM titanic_postgres WHERE'
        ' "Pclass" = 2;'
    )
    print(
        "The average number of passengers' parents/children aboard who"
        " were from class 2 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Parents/Children Aboard") FROM titanic_postgres WHERE'
        ' "Pclass" = 3;'
    )
    print(
        "The average number of passengers' parents/children aboard who"
        " were from class 3 was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Parents/Children Aboard") FROM titanic_postgres WHERE'
        ' "Survived" = 1'
    )
    print(
        "The average number of passengers' parents/children aboard who"
        " survived was %f."
        % (pg_curs.fetchall()[0][0])
    )
    pg_curs.execute(
        'SELECT AVG("Parents/Children Aboard") FROM titanic_postgres WHERE'
        ' "Survived" = 0'
    )
    print(
        "The average number of passengers' parents/children aboard who"
        " died was %f."
        % (pg_curs.fetchall()[0][0])
    )

    # Do any passengers have the same name?
    pg_curs.execute("SELECT COUNT(*) FROM titanic_postgres")
    total = pg_curs.fetchall()[0][0]
    pg_curs.execute('SELECT COUNT(DISTINCT "Name") FROM titanic_postgres')
    print(
        "%d passengers have the same name" % (total - pg_curs.fetchall()[0][0])
    )
