import psycopg2

dbname = 'vbmmjeoc'
user = 'vbmmjeoc'  # ElephantSQL happens to use same name for db and user
password = 'qiPPfJeCLmtX5-yUZcV27SmlTz75PQka'  # Sensitive! Don't share/commit
host = 'isilo.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
c = pg_conn.cursor()
"""Practice queries of the titanic data"""
"""
- How many passengers survived, and how many died?
"""
c.execute("""
    SELECT COUNT(*) || ' died.'
    FROM titanic
    WHERE Survived = 0;
""")
c.fetchone()
c.execute("""
    SELECT COUNT(*) || ' survived.'
    FROM titanic
    WHERE Survived = 1;
""")
c.fetchone()

"""
- How many passengers were in each class?
"""
c.execute("""
    SELECT COUNT(*) || ' passengers in class ' || Pclass
    FROM titanic
    GROUP BY Pclass
""")
c.fetchall()

"""
- How many passengers survived/died within each class?
"""
c.execute("""
    SELECT COUNT(*) || ' passengers in class ' || Pclass || (CASE WHEN Survived = 1 THEN ' survived.' ELSE ' died.' END)
    FROM titanic
    GROUP BY Pclass, Survived
""")
c.fetchall()

"""
- What was the average age of survivors vs nonsurvivors?
"""
c.execute("""SELECT AVG(Age) || (CASE WHEN Survived = 1 THEN ' was the average age of survivors' ELSE ' was the 
average age of nonsurvivors' END) FROM titanic GROUP BY Survived;""")
c.fetchall()

"""What was the average age of each passenger class?"""
c.execute("""
SELECT 'Average age of: ' || (
        CASE
            WHEN Pclass = 1 THEN 'first class'
            WHEN Pclass = 2 THEN 'second class'
            WHEN Pclass = 3 THEN 'third class'
        END
    ) || ':' || AVG(Age)
    FROM titanic
    GROUP BY Pclass
""")
c.fetchall()

"""
#- What was the average fare by passenger class? By survival?
"""
c.execute("""
    SELECT 'Average fare of: ' || (
        CASE
            WHEN Pclass = 1 THEN 'first class'
            WHEN Pclass = 2 THEN 'second class'
            WHEN Pclass = 3 THEN 'third class'
        END
    ) || ': ' || AVG(Fare)
    FROM titanic
    GROUP BY Pclass
""")
c.fetchall()

c.execute("""
    SELECT 'Average fare of: ' || (
        CASE
            WHEN Survived = 1 THEN 'surivors'
            WHEN Survived = 0 THEN 'nonsurvivors'
        END
    ) || ': ' || AVG(Fare)
    FROM titanic
    GROUP BY Survived
""")
c.fetchall()
"""
- How many siblings/spouses aboard on average, by passenger class? By survival?
"""
c.execute("""
    SELECT 'Average number of siblings/spouses of: ' || (
        CASE
            WHEN Pclass = 1 THEN 'first class'
            WHEN Pclass = 2 THEN 'second class'
            WHEN Pclass = 3 THEN 'third class'
        END
    ) || ': ' || AVG(Siblings/Spouses Aboard)
    FROM titanic
    GROUP BY Pclass
""")
c.fetchall()

c.execute("""
    SELECT 'Average number of siblings/spouses of: ' || (
        CASE
            WHEN Survived = 1 THEN 'surivors'
            WHEN Survived = 0 THEN 'nonsurvivors'
        END
    ) || ': ' || AVG(Siblings/Spouses Aboard)
    FROM titanic
    GROUP BY Survived
""")
c.fetchall()

"""
#- How many parents/children aboard on average, by passenger class? By survival?
"""
c.execute("""
    SELECT 'Average number of parents/children of ' || (
        CASE
            WHEN Pclass = 1 THEN 'first class'
            WHEN Pclass = 2 THEN 'second class'
            WHEN Pclass = 3 THEN 'third class'
        END
    ) || ': ' || AVG(Parents_or_children_aboard)
    FROM titanic
    GROUP BY Pclass
""")
c.fetchall()

c.execute("""
    SELECT 'Average number of parents/children of: ' || (
        CASE
            WHEN Survived = 1 THEN 'surivors'
            WHEN Survived = 0 THEN 'nonsurvivors'
        END
    ) || ': ' || AVG(Parents_or_children_aboard)
    FROM titanic
    GROUP BY Survived
""")
c.fetchall()

""""
#- Do any passengers have the same name?
"""
c.execute("""
    SELECT *
    FROM (
        SELECT COUNT(*) as name_count, Name
        FROM titanic
        GROUP BY Name
    ) AS q
    WHERE q.name_count > 1;
""")
c.fetchall()

"""
- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.
"""
c.execute("""
    SELECT Name
    FROM titanic
    WHERE ((Name LIKE 'Mr.%') OR (Name LIKE 'Mrs.%'))
        AND Siblings_or_spouses_aboard > 0;
""")
names = c.fetchall()
male_last_names = [name.split(" ")[-1] for name, in names if name.startswith("Mr.")]
female_last_names = [name.split(" ")[-1] for name, in names if name.startswith("Mrs.")]

overlap = set(male_last_names) & set(female_last_names)
"Number married couples:", len(overlap)
