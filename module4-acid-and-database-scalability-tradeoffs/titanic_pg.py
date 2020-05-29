import psycopg2
import os
from dotenv import load_dotenv
import json

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

cur = conn.cursor()

# How many pasengers survived, and how many died?
survived = 'SELECT COUNT("Survived") AS Survived FROM titanic WHERE "Survived" = 1;'
cur.execute(survived)
result_survived = cur.fetchall()

died = 'SELECT COUNT("Survived") AS Died FROM titanic WHERE "Survived" = 0;'
cur.execute(died)
result_died = cur.fetchall()

print(f'Number of people who survived: {result_survived[0][0]}, died: {result_died[0][0]}')
print("-----------------")

# How many passengers were in each class?
passengers = 'SELECT "Pclass", COUNT("Pclass") FROM titanic GROUP BY "Pclass" ORDER BY "Pclass"'
cur.execute(passengers)
result = cur.fetchall()

for i in range(0, len(result)):
    print(f'The number of passengers in class {result[i][0]}: {result[i][1]}')
print("-----------------")

# How many passengers survived/died within each class?
surv = 'SELECT "Pclass", COUNT(*) FROM titanic WHERE "Survived" = 1 GROUP BY "Pclass" ORDER BY "Pclass"'
cur.execute(surv)
result_surv = cur.fetchall()

died = 'SELECT "Pclass", COUNT(*) FROM titanic WHERE "Survived" = 0 GROUP BY "Pclass" ORDER BY "Pclass"'
cur.execute(died)
result_died = cur.fetchall()

for i in range(len(result_surv)):
    print(f'Number of people who survived in class {result_surv[i][0]}: {result_surv[i][1]}; Died: {result_died[i][1]}')
print("-----------------")

# What was the average age of survivors vs nonsurvivors?
avg_age = 'SELECT "Survived", AVG("Age") as "Avg Age" FROM titanic GROUP BY "Survived" ORDER BY "Survived" DESC'
cur.execute(avg_age)
result = cur.fetchall()

print(f'Average age of survivors: {result[0][1]:.2f}; Nonsurvivors: {result[1][1]:.2f}')
print("-----------------")

# What was the average age of each passenger class?
query = 'SELECT "Pclass", AVG("Age") FROM titanic GROUP BY "Pclass" ORDER BY "Pclass"'
cur.execute(query)
pclass_age = cur.fetchall()

for i in range(0, len(pclass_age)):
    print(f'Average age of passengers in class {pclass_age[i][0]}: {pclass_age[i][1]:.2f}')
print("-----------------")

# What was the average fare by passenger class?
query = 'SELECT "Pclass", AVG("Fare") FROM titanic GROUP BY "Pclass" ORDER BY "Pclass"'
cur.execute(query)
pclass_fare = cur.fetchall()

for i in range(0, len(pclass_fare)):
    print(f'Average fare of passengers in class {pclass_fare[i][0]}: ${pclass_fare[i][1]:.2f}')
print("-----------------")

# By survival?
query = 'SELECT "Survived", AVG("Fare") FROM titanic GROUP BY "Survived" ORDER BY "Survived" DESC'
cur.execute(query)
surv_fare = cur.fetchall()

print(f'Average fare of passengers that survived: ${surv_fare[0][1]:.2f}; Died: ${surv_fare[1][1]:.2f}')
print("-----------------")

# How many siblings/spouses aboard on average?
query = 'SELECT AVG("Siblings/Spouses Aboard") FROM titanic'
cur.execute(query)
avg = cur.fetchall()

print(f'Average siblings/spouses aboard: {avg[0][0]:.2f}')
print("-----------------")

# by passenger class?
query = 'SELECT "Pclass", AVG("Siblings/Spouses Aboard") FROM titanic GROUP BY "Pclass" ORDER BY "Pclass"'
cur.execute(query)
pclass_avg = cur.fetchall()

for i in range(0, len(pclass_avg)):
    print(f'Average sib/spouses aboard for class {pclass_avg[i][0]}: {pclass_avg[i][1]:.2f}')
print("-----------------")

# By survival?
query = 'SELECT "Survived", AVG("Siblings/Spouses Aboard") FROM titanic GROUP BY "Survived" ORDER BY "Survived" DESC'
cur. execute(query)
surv_avg = cur.fetchall()

print(f'Average sib/spouses aboard for survivors: {surv_avg[0][1]:.2f}; nonsurvivors: {surv_avg[1][1]:.2f}')
print("-----------------")

# How many parents/children aboard on average?
query = 'SELECT AVG("Parents/Children Aboard") FROM titanic'
cur.execute(query)
avg = cur.fetchall()

print(f'Average Parents/Children Aboard: {avg[0][0]:.2f}')
print("-----------------")

# by passenger class?
query = 'SELECT "Pclass", AVG("Parents/Children Aboard") FROM titanic GROUP BY "Pclass" ORDER BY "Pclass"'
cur.execute(query)
pclass_avg = cur.fetchall()

for i in range(0, len(pclass_avg)):
    print(f'Average Parents/Children Aboard for class {pclass_avg[i][0]}: {pclass_avg[i][1]:.2f}')
print("-----------------")

# By survival?
query = 'SELECT "Survived", AVG("Parents/Children Aboard") FROM titanic GROUP BY "Survived" ORDER BY "Survived" DESC'
cur. execute(query)
surv_avg = cur.fetchall()

print(f'Average Parents/Children Aboard for survivors: {surv_avg[0][1]:.2f}; nonsurvivors: {surv_avg[1][1]:.2f}')
print("-----------------")

# Do any passengers have the same name?
query = 'SELECT COUNT("Name") FROM titanic'
cur.execute(query)
count = cur.fetchall()

query = 'SELECT COUNT(DISTINCT "Name") FROM titanic'
cur.execute(query)
dist_count = cur.fetchall()
print(f'Number of duplicate names: {count[0][0] - dist_count[0][0]}')