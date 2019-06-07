import sqlite3

conn = sqlite3.connect("/Users/mattkirby/Desktop/Titanic")
curs = conn.cursor()


# 1. How many passengers survived, and how many died?
survived_query = """SELECT COUNT(Survived)
                    FROM titanic
                    WHERE Survived = 1;"""

survived_result = curs.execute(survived_query)

print('1. ')
print(survived_result.fetchall()[0][0],'passengers survived')
print('\n')


# 2. How many passengers were in each class?
class_query = """SELECT COUNT(Pclass)
                 FROM titanic
                 GROUP BY Pclass;"""

class_result = curs.execute(class_query)

print('2. ')
print(class_result.fetchall())
print('\n')


# 3. How many passengers survived/died within each class?
died_class_query = """SELECT Pclass, Count(Survived)
                      FROM titanic
                      GROUP BY Pclass;"""

died_class_result = curs.execute(died_class_query)

print('3. ')
print(died_class_result.fetchall())
print('\n')


# 4. What was the average age of survivors vs nonsurvivors?
ave_age_query = """SELECT Survived, AVG(Age)
                   FROM titanic
                   GROUP BY Survived;"""

ave_age_result = curs.execute(ave_age_query)

print('4. ')
print(ave_age_result.fetchall())
print('\n')


# 5. What was the average age of each passenger class?
ave_pass_query = """SELECT Pclass, AVG(Age)
                    FROM titanic
                    GROUP BY Pclass;"""

ave_pass_result = curs.execute(ave_pass_query)

print('5. ')
print(ave_pass_result.fetchall())
print('\n')


# 6. What was the average fare by passenger class? By survival?
ave_fare_query = """SELECT Pclass, AVG(Fare)
                    FROM titanic
                    GROUP BY Pclass;"""

ave_fare_result = curs.execute(ave_fare_query)

print('6. ')
print(ave_fare_result.fetchall())
print('\n')


# 7. How many siblings/spouses aboard on average,
#    by passenger class? By survival?
by_class_query = """SELECT Pclass, AVG(Siblings_Spouses_Aboard)
                    FROM titanic
                    GROUP BY Pclass;"""

by_class_result = curs.execute(by_class_query)

by_survival_query = """SELECT Survived, AVG(Siblings_Spouses_Aboard)
                       FROM titanic
                       GROUP BY Survived;"""

by_survival_result = curs.execute(by_survival_query)

print('7. ')
print(by_class_result.fetchall())
print('\n')
print(by_survival_result.fetchall())
print('\n')


# 8. How many parents/children aboard on average,
#    by passenger class? By survival?
parrents_by_class_query = """SELECT Pclass, AVG(Parents_Children_Aboard)
                             FROM titanic
                             GROUP BY Pclass;"""

parrents_by_class_result = curs.execute(parrents_by_class_query)

parrents_by_survival_query = """SELECT Survived, AVG(Parents_Children_Aboard)
                                FROM titanic
                                GROUP BY Survived;"""

parrents_by_survival_result = curs.execute(parrents_by_survival_query)

print('8. ')
print(parrents_by_class_result.fetchall())
print('\n')
print(parrents_by_survival_result.fetchall())
print('\n')


# 9. Do any passengers have the same name?
same_name_query = """SELECT Name, Count(*)
                     FROM titanic
                     GROUP BY Name
                     HAVING COUNT(*) > 1;"""

same_name_result = curs.execute(same_name_query)

print('9. ')
print(same_name_result.fetchall())
print('\n')
