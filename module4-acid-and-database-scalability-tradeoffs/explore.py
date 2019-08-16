from pymongo import MongoClient
import numpy as np

# MONGO DB STUFF
client = MongoClient("mongodb+srv://admin:L2oz0xJtZmJwfTsg@cluster0-2wndt.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

# HOW MANY PASSENGERS SURVIVED?
survivors = db.test.find({'survived': 1})
print(f'{len(list(survivors))} passengers survived')

# HOW MANY PASSENGERS DIED?
dead_people = db.test.find({'survived': 0})
print(f'{len(list(dead_people))} passengers died')

# PEOPLE IN PCLASS 1
class_1 = db.test.find({'pclass': 1})
print(f'{len(list(class_1))} passengers were in Pclass 1')

# PEOPLE IN PCLASS 2
class_2 = db.test.find({'pclass': 2})
print(f'{len(list(class_2))} passengers were in Pclass 2')

# PEOPLE IN PCLASS 3
class_3 = db.test.find({'pclass': 3})
print(f'{len(list(class_3))} passengers were in Pclass 3')

# SURVIVORS OF CLASS 1
class_1_survivors = db.test.find({'pclass': 1, 'survived': 1})
print(f'{len(list(class_1_survivors))} survivors were in Pclass 1')

# SURVIVORS OF CLASS 2
class_2_survivors = db.test.find({'pclass': 2, 'survived': 1})
print(f'{len(list(class_2_survivors))} survivors were in Pclass 2')

# SURVIVORS OF CLASS 3
class_3_survivors = db.test.find({'pclass': 3, 'survived': 1})
print(f'{len(list(class_3_survivors))} survivors were in Pclass 3')

# NON_SURVIVORS OF CLASS 1
class_1_dead = db.test.find({'pclass': 1, 'survived': 0})
print(f'{len(list(class_1_dead))} people who died were in Pclass 1')

# NON_SURVIVORS OF CLASS 2
class_2_dead = db.test.find({'pclass': 2, 'survived': 0})
print(f'{len(list(class_2_dead))} people who died were in Pclass 2')

# NON_SURVIVORS OF CLASS 3
class_3_dead = db.test.find({'pclass': 3, 'survived': 0})
print(f'{len(list(class_3_dead))} people who died were in Pclass 3')

# AVERAGE AGE OF SURVIVORS
survivor_ages = []
for person in list(db.test.find({'survived': 1})):
    survivor_ages.append(list(person.values())[5])
print(f'The average age of the survivors was {round(np.mean(survivor_ages), 2)} years old')

# AVERAGE AGE OF NON SURVIVORS
dead_people_ages = []
for person in list(db.test.find({'survived': 0})):
    dead_people_ages.append(list(person.values())[5])
print(f'The average age of the dead people was {round(np.mean(dead_people_ages), 2)} years old')

# AVERAGE FARE OF CLASS 1
class_1_fares = []
for person in list(db.test.find({'pclass': 1})):
    class_1_fares.append(list(person.values())[9])
print(f'The average fare for class 1 was ${round(np.mean(class_1_fares), 2)}')

# AVERAGE FARE OF CLASS 2
class_2_fares = []
for person in list(db.test.find({'pclass': 2})):
    class_2_fares.append(list(person.values())[9])
print(f'The average fare for class 2 was ${round(np.mean(class_2_fares), 2)}')

# AVERAGE FARE OF CLASS 3
class_3_fares = []
for person in list(db.test.find({'pclass': 3})):
    class_3_fares.append(list(person.values())[9])
print(f'The average fare for class 3 was ${round(np.mean(class_3_fares), 2)}')

# AVERAGE FARE OF SURVIVORS
survivor_fares = []
for person in list(db.test.find({'survived': 1})):
    survivor_fares.append(list(person.values())[9])
print(f'The average fare for survivors was ${round(np.mean(survivor_fares), 2)}')

# AVERAGE FARE OF NON SURVIVORS
dead_people_fares = []
for person in list(db.test.find({'survived': 0})):
    dead_people_fares.append(list(person.values())[9])
print(f'The average fare for people who died was ${round(np.mean(dead_people_fares), 2)}')

# AVERAGE SIBLINGS/SPOUSES FOR CLASS 1
class_1_siblings_spouses = []
for person in list(db.test.find({'pclass': 1})):
    class_1_siblings_spouses.append(list(person.values())[6])
print(f'The average amount of siblings/spouses for class 1 was {round(np.mean(class_1_siblings_spouses), 2)}')

# AVERAGE SIBLINGS/SPOUSES FOR CLASS 2
class_2_siblings_spouses = []
for person in list(db.test.find({'pclass': 2})):
    class_2_siblings_spouses.append(list(person.values())[6])
print(f'The average amount of siblings/spouses for class 2 was {round(np.mean(class_2_siblings_spouses), 2)}')

# AVERAGE SIBLINGS/SPOUSES FOR CLASS 3
class_3_siblings_spouses = []
for person in list(db.test.find({'pclass': 3})):
    class_3_siblings_spouses.append(list(person.values())[6])
print(f'The average amount of siblings/spouses for class 3 was {round(np.mean(class_3_siblings_spouses), 2)}')

# AVERAGE SIBLINGS/SPOUSES FOR SURVIVORS
survivors_siblings_spouses = []
for person in list(db.test.find({'survived': 1})):
    survivors_siblings_spouses.append(list(person.values())[6])
print(f'The average amount of siblings/spouses for survivors was {round(np.mean(survivors_siblings_spouses), 2)}')

# AVERAGE SIBLINGS/SPOUSES FOR DEAD PEOPLE
dead_people_siblings_spouses = []
for person in list(db.test.find({'survived': 0})):
    dead_people_siblings_spouses.append(list(person.values())[6])
print(f'The average amount of siblings/spouses for dead people was {round(np.mean(dead_people_siblings_spouses), 2)}')

# AVERAGE PARENTS/CHILDREN FOR CLASS 1
class_1_parents_children = []
for person in list(db.test.find({'pclass': 1})):
    class_1_parents_children.append(list(person.values())[7])
print(f'The average amount of parnets/children for class 1 was {round(np.mean(class_1_parents_children), 2)}')

# AVERAGE PARENTS/CHILDREN FOR CLASS 2
class_2_parents_children = []
for person in list(db.test.find({'pclass': 2})):
    class_2_parents_children.append(list(person.values())[7])
print(f'The average amount of parents/children for class 2 was {round(np.mean(class_2_parents_children), 2)}')

# AVERAGE PARENTS/CHILDREN FOR CLASS 3
class_3_parents_children = []
for person in list(db.test.find({'pclass': 3})):
    class_3_parents_children.append(list(person.values())[7])
print(f'The average amount of parents/children for class 3 was {round(np.mean(class_3_parents_children), 2)}')

# AVERAGE PARENTS/CHILDREN FOR SURVIVORS
survivors_parents_children = []
for person in list(db.test.find({'survived': 1})):
    survivors_parents_children.append(list(person.values())[7])
print(f'The average amount of parents/children for survivors was {round(np.mean(survivors_parents_children), 2)}')

# AVERAGE PARENTS/CHILDREN FOR DEAD PEOPLE
dead_people_parents_children = []
for person in list(db.test.find({'survived': 0})):
    dead_people_parents_children.append(list(person.values())[7])
print(f'The average amount of parents/children for dead people was {round(np.mean(dead_people_parents_children), 2)}')

# NUMBER OF PASSENGERS WITH THE SAME NAME
passenger_names = []
dup_names = []
number_of_people_with_same_name = 0
for passenger in list(db.test.find()):
    passenger_names.append(str.split(list(passenger.values())[8])[-1])

for name in passenger_names:
    if passenger_names.count(name) > 1:
        if name not in dup_names:
            number_of_people_with_same_name += 1
            dup_names.append(name)

print(f'There are {number_of_people_with_same_name} with the same name!')
