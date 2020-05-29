# postgresql_titatnic.py


# Questions

# 1. How many passengers survived, and how many died?
# 2. How many passengers were in each class?
# 3. How many passengers survived/died within each class?
# 4. What was the average age of survivors vs nonsurvivors?
# 5. What was the average age of each passenger class?
# 6. What was the average fare by passenger class? By survival?
# 7. How many siblings/spouses aboard on average, by passenger class? By survival?
# 8. How many parents/children aboard on average, by passenger class? By survival?
# 9 Do any passengers have the same name?


# Imports

import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import DictCursor


# Load credentials for ElephantSQL

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")


# Connect to ElephantSQL server

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))


# Create SQL cursor

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
#cursor = connection.cursor()
print("CURSOR", type(cursor))


# 1. How many passengers survived, and how many died?

survivors = "SELECT COUNT(survived) FROM titanic WHERE survived = 1;"

cursor.execute(survivors)

survived = cursor.fetchall()

died = "SELECT COUNT(survived) FROM titanic WHERE survived = 0;"

cursor.execute(died)

died = cursor.fetchall()

print("ANSWER 1: passengers survived:", survived, "and passengers died:", died)


# 2. How many passengers were in each class?

class_count = "SELECT p_class,COUNT(*) FROM titanic GROUP BY p_class;"

cursor.execute(class_count)

class_count = cursor.fetchall()

print("ANSWER 2: passengers in each class:", class_count)


# 3. How many passengers survived/died within each class?

survived = "SELECT p_class,COUNT(p_class) FROM titanic WHERE survived = 1 GROUP BY p_class;"

cursor.execute(survived)

survived = cursor.fetchall()

died = "SELECT p_class,COUNT(p_class) FROM titanic WHERE survived = 0 GROUP BY p_class;"

cursor.execute(died)

died = cursor.fetchall()

print("ANSWER 3: passengers survived in each class:", survived, 
      "passengers died in each class:", died)


# 4. What was the average age of survivors vs nonsurvivors?

survivors_age = "SELECT AVG(age) from titanic WHERE survived = 1"

cursor.execute(survivors_age)

survivors_age = cursor.fetchall()

nonsurvivors_age = "SELECT AVG(age) from titanic WHERE survived = 0"

cursor.execute(nonsurvivors_age)

nonsurvivors_age = cursor.fetchall()

print("ANSWER 4: average age of survivors:", survivors_age, 
      "vs average age of nonsurvivors:", nonsurvivors_age)


# 5. What was the average age of each passenger class?

avg_age_passenger = "SELECT p_class,AVG(age) FROM titanic GROUP BY p_class;"

cursor.execute(avg_age_passenger)

avg_age_passenger = cursor.fetchall()

print("ANSWER 5: average age of survivors by class:", avg_age_passenger)


# 6. What was the average fare by passenger class? By survival?

avg_fare_p_class = "SELECT p_class,AVG(fare) FROM titanic GROUP BY p_class;"

cursor.execute(avg_fare_p_class)

avg_fare_p_class = cursor.fetchall()

avg_fare_survival = "SELECT survived,AVG(fare) FROM titanic GROUP BY survived"

cursor.execute(avg_fare_survival)

avg_fare_survival = cursor.fetchall()

print("ANSWER 6: average fare by passenger class:", avg_fare_p_class,
      "and average fare by survival:", avg_fare_survival)


# 7. How many siblings/spouses aboard on average, by passenger class? By survival?

avg_ss_class = "SELECT p_class,AVG(siblings_spouses_aboard) FROM titanic GROUP BY p_class;"

cursor.execute(avg_ss_class)

avg_ss_class = cursor.fetchall()

avg_ss_survival = "SELECT survived,AVG(siblings_spouses_aboard) FROM titanic GROUP BY survived;"

cursor.execute(avg_ss_survival)

avg_ss_survival = cursor.fetchall()

print("ANSWER 7: average siblings/spouses aboard on average by passenger class:", avg_ss_class,
      "and average siblings/spouses aboard on average by survival:", avg_ss_survival)


# 8. How many parents/children aboard on average, by passenger class? By survival?

avg_pc_class = "SELECT p_class,AVG(parents_children_aboard) FROM titanic GROUP BY p_class;"

cursor.execute(avg_pc_class)

avg_pc_class = cursor.fetchall()

avg_pc_survival = "SELECT survived,AVG(parents_children_aboard) FROM titanic GROUP BY survived;"

cursor.execute(avg_pc_survival)

avg_pc_survival = cursor.fetchall()

print("ANSWER 7: average parents/children aboard on average by passenger class:", avg_pc_class,
      "and average parents/children aboard on average by survival:", avg_pc_survival)


# 9 Do any passengers have the same name?

same_name = "SELECT name,COUNT(*) FROM titanic GROUP BY name HAVING COUNT(name) > 1;"

cursor.execute(same_name)

same_name = cursor.fetchall()

print("ANSWER 8: passengers with same name:", same_name)

