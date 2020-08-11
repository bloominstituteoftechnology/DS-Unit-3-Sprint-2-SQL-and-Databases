import psycopg2
import sqlite3

# Defining a function to refresh connection and cursor
def refresh_connection_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


if __name__ == "__main__":

    # Looks similar to sqlite3, but needs auth/host info to connect
    # Note - this is sensitive info (particularly password)
    # and shouldn't be checked into git! More on how to handle next week

    dbname = "ajkuvccu"
    user = "ajkuvccu"  # ElephantSQL happens to use same name for db and user
    password = "FBOFpSpFdAFrxYUG-DBqN39wDQ0Mjc4V"  # Sensitive! Don't share/commit
    host = "isilo.db.elephantsql.com"

    # If we make too many connections, the database complains! Be sure to close
    # cursors and connections
    pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

    pg_curs = pg_conn.cursor()  # Works the same as SQLite!

    # We're connected, but db is empty
    # Let's run a simple example to populate (from the tk)
    create_table_statement = """
    CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
    );
    """
    # NOTE - these types are PostgreSQL specific. This won't work in SQLite!

    # pg_curs.execute(create_table_statement)
    pg_conn.commit()  # "Save" by committing

    # We're connected, let's see what is in the db
    pg_curs.execute("SELECT * FROM test_table;")
    pg_curs.fetchall()

    insert_statement = """
    INSERT INTO test_table (name, data) VALUES
    (
    'Zaphod Beeblebrox',
    '{"key": "value", "key2": true}'::JSONB
    )
    """

    pg_curs.execute(insert_statement)
    pg_conn.commit()

    pg_curs.execute("SELECT * FROM test_table;")
    pg_curs.fetchall()

    pg_curs.close()
    # pg_conn.close()  # If we were really done

    # Database constraints from the schema are enforced!
    # This is good - helps ensure data quality
    pg_curs = pg_conn.cursor()
    pg_curs.execute("INSERT INTO test_table (name, data) VALUES (null, null);")

    sl_conn = sqlite3.connect("rpg_db.sqlite3")
    sl_curs = sl_conn.cursor()

    get_characters = "SELECT * FROM charactercreator_character;"
    sl_curs.execute(get_characters)
    characters = sl_curs.fetchall()

    # Step 1 complete! We have a list of tuples with all our character data
    # NOTE - this is *not* a pandas dataframe
    # We don't know types - so, for "Transform" we need to figure that out
    # Because our destination (PostgreSQL) needs a schema for this data

    # Step 2 - Transform
    # Our goal is to make a schema to define a table that fits this data in Postgres
    # We can check the old schema!
    # This is an internal meta sort of query, will vary by database flavor
    sl_curs.execute("PRAGMA table_info(charactercreator_character);")
    sl_curs.fetchall()

    # A bunch of integers, and a varchar
    # We need to make a create statement for PostgreSQL that captures this
    create_character_table = """
    CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
    );
    """

    pg_conn, pg_curs = refresh_connection_and_cursor(pg_conn, pg_curs)

    # Execute the create table
    # pg_curs.execute(create_character_table)
    pg_conn.commit()

    # PostgreSQL comparison to the SQLite pragma
    # We can query tables if we want to check
    # This is a clever optional thing, showing postgresql internals
    show_tables = """
    SELECT
    *
    FROM
    pg_catalog.pg_tables
    WHERE
    schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
    """
    pg_curs.execute(show_tables)
    pg_curs.fetchall()

    # Done with step 2 (transform)
    # We didn't really change the data, just made sure we could fit it in our target
    # Step 3 - Load!
    characters[0]

    # We want to put this tuple in a string w/INSERT INTO...
    # But we don't want the first field (id) - PostgreSQL generates that
    characters[0][1:]

    example_insert = (
        """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """
        + str(characters[0][1:])
        + ";"
    )

    print(example_insert)  # Not running, just inspecting

    # If we ran this, we'd insert the first character
    # But we want them all - loops!
    for character in characters:
        insert_character = (
            """
            INSERT INTO charactercreator_character
            (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES """
            + str(character[1:])
            + ";"
        )
        pg_curs.execute(insert_character)

    # Note - we're executing each character one at a time
    # That works, and is simple, but inefficient (lots of roundtrips to database)
    # Stretch/afternoon goal - see if you can combine into a single
    # insert that does them all at once
    pg_conn.commit()

    # Let's look at what we've done
    pg_curs.execute("SELECT * FROM charactercreator_character LIMIT 5;")
    pg_curs.fetchall()

    # Ids are different (on first run, now fixed)!
    # That's because we had an aborted run
    # Let's fix this by deleting the data and DROPping the table
    # Other tables are fine, but we'll dump the data *and* schema to rerun
    # pg_curs.execute('DROP TABLE charactercreator_character;')
    # pg_conn.commit()

    # Now we need to rerun the above... scrolling up and down, because notebooks
    # Specifically rerunning character table create statement and data inserts

    # Now the data looks the same! But let's check it systematically
    pg_curs.execute("SELECT * FROM charactercreator_character;")
    pg_characters = pg_curs.fetchall()

    # We could do more spot checks, but let's loop and check them all
    # TODO/afternoon task - consider making this a more formal test
    for character, pg_character in zip(characters, pg_characters):
        assert character == pg_character

    # No complaints - which means they're all the same!
    # Closing out cursor/connection to wrap up
    pg_curs.close()
    pg_conn.close()
    sl_curs.close()
    sl_conn.close()
