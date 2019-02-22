import psycopg2 as pg
import csv

conn = pg.connect("host=localhost dbname=titanic_db user=sammylee")
cur = conn.cursor()


query = """
CREATE TABLE IF NOT EXISTS public.titanic (
    "Survived" integer,
    "Pclass" integer,
    "Name" text,
    "Sex" text,
    "Age" numeric(4,2),
    "Siblings_Spouses_Aboard" integer,
    "Parents_Children_Aboard" integer,
    "Fare" numeric(7,4)
);
"""

cur.execute(query)


with open('titanic_cleaned.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		cur.execute("INSERT INTO titanic VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",row)



# How many passengers survived?
query1 = """
SELECT COUNT ("Survived") FROM titanic where "Survived"=1;
"""
# How many passengers did not survive?
query2 = """
SELECT COUNT ("Survived") FROM titanic where "Survived"=0;
"""
# How many passengers were in each class?
query3 = """
SELECT "Pclass", COUNT (*)
FROM titanic
GROUP BY "Pclass"
ORDER BY COUNT (*);
"""
# Number of Survivors from Pclass 1 
query4 = """
SELECT COUNT (*)
FROM titanic
WHERE "Pclass"=1 AND "Survived"=1;
"""
# Number of Survivors from Pclass 2
query5 = """
SELECT COUNT (*)
FROM titanic
WHERE "Pclass"=2 AND "Survived"=1;
"""
# Number of Survivors from Pclass3
query6 = """
SELECT COUNT (*)
FROM titanic
WHERE "Pclass"=3 AND "Survived"=1;
"""

# Number of Non-Survivors from Pclass1
query7 = """
SELECT COUNT (*)
FROM titanic
WHERE "Pclass"=1 AND "Survived"=0;
"""
# Number of Non-Survivors from Pclass2
query8 = """
SELECT COUNT (*)
FROM titanic
WHERE "Pclass"=2 AND "Survived"=0;
"""
# Number of Non-Survivors from Pclass3
query9 = """
SELECT COUNT (*)
FROM titanic
WHERE "Pclass"=3 AND "Survived"=0;
"""
# Average age of Survivors:
query10 = """
SELECT AVG ("Age")
FROM titanic
WHERE "Survived" = 1;
"""
# Average age of Non-Survivors:
query11 = """
SELECT AVG ("Age")
FROM titanic
WHERE "Survived" = 0;
"""
# Average age of passengers by Pclass:
query12 = """
SELECT "Pclass", AVG ("Age")
FROM titanic
GROUP BY "Pclass" 
ORDER BY "Pclass";
"""
# Average fare by class:
query13 = """
SELECT "Pclass", AVG ("Fare") AS average_fare
FROM titanic
GROUP BY "Pclass"
ORDER BY "Pclass";
"""
# Average fare by Survival:
query14 = """
SELECT "Survived", AVG ("Fare") AS average_fare
FROM titanic
GROUP BY "Survived";
"""
# Average Siblings/Spouses by Pclass:
query15 = """
SELECT "Pclass", AVG ("Siblings_Spouses_Aboard") AS average_siblings_spouses
FROM titanic
GROUP BY "Pclass";
"""
# Average Siblings/Spouses by Survival:
query16 = """
SELECT "Survived", AVG ("Siblings_Spouses_Aboard") AS average_siblings_spouses
FROM titanic
GROUP BY "Survived";
"""
# Average Parents/Children by Pclass:
query17 = """
SELECT "Pclass", AVG ("Parents_Children_Aboard")
FROM titanic
GROUP BY "Pclass"
ORDER BY "Pclass";
"""
# Average Parents/Children by Survival:
query18 = """
SELECT "Survived", AVG ("Parents_Children_Aboard")
FROM titanic
GROUP BY "Survived";
"""
# Any passengers share the same name?
query19 = """
SELECT "Name", "Name", COUNT (*)
FROM titanic
GROUP BY "Name", "Name"
HAVING COUNT (*) > 1;
"""

cur.execute(query1)
print("\nNumber of Survivors:", cur.fetchall())

cur.execute(query2)
print("Number of Deceased:", cur.fetchall())

cur.execute(query3)
print("Number of People in each class:", cur.fetchall())

print()
print("Survivors by Pclass")
print()

cur.execute(query4)
print("PClass 1 Survivors:", cur.fetchall())

cur.execute(query5)
print("PClass 2 Survivors:", cur.fetchall())

cur.execute(query6)
print("Pclass 3 Survivors:", cur.fetchall())

print()
print("Non-Survivors by Pclass")
print()

cur.execute(query7)
print("Pclass 1 Non-Survivors:", cur.fetchall())

cur.execute(query8)
print("Pclass 2 Non-Survivors:", cur.fetchall())

cur.execute(query9)
print("Pclass 3 Non-Survivors:", cur.fetchall())

print()

cur.execute(query10)
print("Average age of Survivors:", cur.fetchall())

cur.execute(query11)
print("Average age of Non-Survivors:", cur.fetchall())

print()

cur.execute(query12)
print("Average age of passengers grouped by Pclass:", cur.fetchall())

print()

cur.execute(query13)
print("Average fare by Pclass:", cur.fetchall())

cur.execute(query14)
print("\nAverage fare by Survival:", cur.fetchall())

cur.execute(query15)
print("\nAverage Siblings_Spouses_Aboard by Pclass:", cur.fetchall())

cur.execute(query16)
print("\nAverage Siblings_Spouses_Aboard by Survival:", cur.fetchall())

cur.execute(query17)
print("\nAverage Parents_Children_Aboard by Pclass:", cur.fetchall())

cur.execute(query18)
print("\nAverage Parents_Children_Aboard by Survival:", cur.fetchall())

cur.execute(query19)
print("\nCount of passengers sharing the same name:", cur.fetchall())
print()








