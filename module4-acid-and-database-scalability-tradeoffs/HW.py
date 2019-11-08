import pandas as pd
import sqlite3


conn = sqlite3.Connection('module2-sql-for-analysis\\titanic.sqlite3')
crs = conn.cursor()


# - How many passengers survived, and how many died?
crs.execute(
    """
    SELECT CASE
		WHEN Survived = 1 THEN 'Survivors:'
		ELSE  'Casualties:' 
		END 'Passengers', count(*)
from titanic GROUP BY Survived;
    """
).fetchall()

# - How many passengers were in each class?
crs.execute(
    """
    SELECT CASE
		WHEN Pclass = 1 THEN 'First_Class:'
		WHEN Pclass = 2 THEN 'Second_Class:'
		ELSE  'Third Class:' 
		END 'Passengers', count(*)
from titanic GROUP BY Pclass;
    """
).fetchall()

# - How many passengers survived/died within each class?
crs.execute(
    """
    SELECT CASE
	WHEN Pclass = 1 AND Survived = 0 THEN 'First_Class Causualties'
	WHEN Pclass = 1 AND Survived = 1 THEN 'First_Class Survivors'
	WHEN Pclass = 2 AND Survived = 0 THEN 'Second_Class Causualties'
	WHEN Pclass = 2 AND Survived = 1 THEN 'Second_Class Survivors'
	WHEN Pclass = 3 AND Survived = 0 THEN 'Third_Class Causualties'
	WHEN Pclass = 3 AND Survived = 1 THEN 'Third_Class Survivors'
	END 'Passengers', count(*) as 'Number'
    from titanic GROUP BY Pclass, Survived;
    """
).fetchall()

# - What was the average age of survivors vs nonsurvivors?
crs.execute(
    """
    SELECT CASE
	WHEN Survived = 1 THEN 'Survivors:'
	ELSE  'Casualties:' 
	END 'Passengers', Round(AVG(Age)) as 'Avg age'
    from titanic GROUP BY Survived;
    """
).fetchall()

# - What was the average age of each passenger class?
crs.execute(
    """
    SELECT CASE
	WHEN Pclass = 1 THEN 'First_Class:'
	WHEN Pclass = 2 THEN 'Second_Class:'
	ELSE  'Third Class:' 
	END 'Passengers', round(avg(Age)) as 'Avg Age'
    from titanic GROUP BY Pclass;
    """
).fetchall()

# - What was the average fare by passenger class? 
crs.execute(
    """
    SELECT CASE
	WHEN Pclass = 1 THEN 'First_Class:'
	WHEN Pclass = 2 THEN 'Second_Class:'
	ELSE  'Third Class:' 
	END 'Passengers', round(avg(Fare),2) as 'Avg Fare'
    from titanic GROUP BY Pclass;
    """
).fetchall()

#       By survival?
crs.execute(
    """
    SELECT CASE
    WHEN Survived = 1 THEN 'Survivors:'
    ELSE  'Casualties:' 
    END 'Passengers', Round(AVG(Fare)) as 'Avg Fare'
    from titanic GROUP BY Survived;
    """
).fetchall()

# - How many siblings/spouses aboard on average, by passenger class?
crs.execute(
    """
    SELECT CASE
	WHEN Pclass = 1 THEN 'First_Class:'
	WHEN Pclass = 2 THEN 'Second_Class:'
	ELSE  'Third Class:' 
    END 'Passengers', round(AVG([Siblings/Spouses Aboard]), 2) as 'Avg Party Size'
    from titanic GROUP BY Pclass;
    """
).fetchall()

#    By survival?
crs.execute(
    """
    SELECT CASE
    WHEN Survived = 1 THEN 'Survivors:'
    ELSE  'Casualties:' 
    END 'Passengers', Round(AVG([Siblings/Spouses Aboard])) as 'Avg Party Size'
    from titanic GROUP BY Survived;
    """
).fetchall()

# - How many parents/children aboard on average, by passenger class?
crs.execute(
    """
    SELECT CASE
    WHEN Pclass = 1 THEN 'First_Class:'
    WHEN Pclass = 2 THEN 'Second_Class:'
    ELSE  'Third Class:' 
    END 'Passengers', round(AVG([Parents/Children Aboard]), 2) as 'Avg Party Size'
    from titanic GROUP BY Pclass;
    """
).fetchall()

#    By survival?
crs.execute(
    """
    SELECT CASE
    WHEN Survived = 1 THEN 'Survivors:'
    ELSE  'Casualties:'
    END 'Passengers', round(AVG([Parents/Children Aboard]), 2) as 'Avg Party Size'
    from titanic GROUP BY Survived;
    """
)

# - Do any passengers have the same name?
crs.execute(
    """
    SELECT Name, count(*)
    FROM titanic
    GROUP BY Name 
    HAVING count(Name) > 1
    """
).fetchall() #No

# - (Bonus! Hard, may require pulling and processing with Python) How many married
#   couples were aboard the Titanic? Assume that two people (one `Mr.` and one
#   `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
#   a married couple.