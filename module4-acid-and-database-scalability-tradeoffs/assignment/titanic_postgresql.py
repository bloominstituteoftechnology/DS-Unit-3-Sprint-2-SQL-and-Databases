"""Query titanic data from a PostgreSQL database."""

import os

import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

# establish environment
assert load_dotenv() == True, 'Failed to load .env'
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
assert DB_NAME is not None, 'DB_NAME not found in environment'
assert DB_USER is not None, 'DB_USER not found in environment'
assert DB_PASS is not None, 'DB_PASS not found in environment'
assert DB_HOST is not None, 'DB_HOST not found in environment'


def answer(query: str, connection):
    """Displays results of a SQL query as named tuples.

    Parameters:

    query: str, SQL query to get answer

    connection: connection to a SQL database

    Returns: nothing
    """
    with connection.cursor(
            cursor_factory=psycopg2.extras.NamedTupleCursor
    ) as cursor:
        cursor.execute(query)
        for answer in cursor.fetchall():
            print(answer)
    print()
    return


def main():
    # connect to PostgreSQL server
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST
    )

    try:
        # answer questions
        print('How many passengers survived, and how many died?')
        query = """
        SELECT
            survived
            ,COUNT(DISTINCT id) AS count
        FROM titanic
        GROUP BY survived;
        """
        answer(query, connection)

        print('How many passengers were in each class?')
        query = """
        SELECT
            pclass
            ,COUNT(DISTINCT id) AS count
        FROM titanic
        GROUP BY pclass;
        """
        answer(query, connection)

        print('How many passengers survived/died within each class?')
        query = """
        SELECT
            pclass
            ,survived
            ,COUNT(DISTINCT id) AS count
        FROM titanic
        GROUP BY pclass, survived;
        """
        answer(query, connection)

        print('What was the average age of survivors vs nonsurvivors?')
        query = """
        SELECT
            survived
            ,AVG(age) AS average_age
        FROM titanic
        GROUP BY survived;
        """
        answer(query, connection)

        print('What was the average age of each passenger class?')
        query = """
        SELECT
            pclass
            ,AVG(age) AS average_age
        FROM titanic
        GROUP BY pclass;
        """
        answer(query, connection)

        print('What was the average fare by passenger class? By survival?')
        query = """
        SELECT
            pclass
            ,AVG(fare) AS average_fare
        FROM titanic
        GROUP BY pclass;
        """
        answer(query, connection)
        query = """
        SELECT
            survived
            ,AVG(fare) AS average_fare
        FROM titanic
        GROUP BY survived;
        """
        answer(query, connection)

        print('How many siblings/spouses aboard on average, ' +
              'by passenger class? By survival?')
        query = """
        SELECT
            pclass
            ,AVG(sib_spouse_count) AS average_sib_spouse
        FROM titanic
        GROUP BY pclass;
        """
        answer(query, connection)
        query = """
        SELECT
            survived
            ,AVG(sib_spouse_count) AS average_sib_spouse
        FROM titanic
        GROUP BY survived;
        """
        answer(query, connection)

        print('How many parents/children aboard on average, ' +
              'by passenger class? By survival?')
        query = """
        SELECT
            pclass
            ,AVG(parent_child_count) AS average_parent_child
        FROM titanic
        GROUP BY pclass;
        """
        answer(query, connection)
        query = """
        SELECT
            survived
            ,AVG(parent_child_count) AS average_parent_child
        FROM titanic
        GROUP BY survived;
        """
        answer(query, connection)

        print('Do any passengers have the same name?')
        query = """
        SELECT
            COUNT(DISTINCT id) - COUNT(DISTINCT name) as num_repeat_names
        FROM titanic;
        """
        answer(query, connection)

        # (Bonus! Hard, may require pulling and processing with Python)
        # How many married couples were aboard the Titanic?
        # Assume that two people (one Mr. and one Mrs.) with the same
        # last name and with at least 1 sibling/spouse aboard are
        # a married couple.
        print('How many (assumed) married couples?')
        query = """
        SELECT
            COUNT(DISTINCT last_name) AS num_assumed_married
        FROM (
            SELECT
                last_name
                ,COUNT(title) AS num_candidates
            FROM (
                SELECT
                    SUBSTRING(name from '^Mrs?[.]') AS title
                    ,SUBSTRING(name from '[^ ]+$') AS last_name
                FROM titanic
                WHERE 
                    sib_spouse_count > 0
                    AND SUBSTRING(name, 1, 2) = 'Mr'
            ) as potential_couples
            GROUP BY last_name
        ) AS possibilities
        WHERE num_candidates > 1
        """
        answer(query, connection)
    finally:
        # always close connection
        connection.close()


if __name__ == '__main__':
    main()
