## Assignment - Part 1, Querying a Database

From rpg_db

- How many total Characters are there?
total_characters = 302

- How many of each specific subclass?
necromancer_subclass = 11
cleric_subclass = 75
fighter_subclass = 68
mage_subclass = 108
thief_subclass = 51

- How many total Items?
total_armory = 174

- How many of the Items are weapons? How many are not?
armory_weapon = 37
not_weapon = total_armory[0][0] - armory_weapon[0][0]
not_weapon = 137

- How many Items does each character have? (Return first 20 rows)
character id, number of items for each character
[1, 3),
 (2, 3),
 (3, 2),
 (4, 4),
 (5, 4),
 (6, 1),
 (7, 5),
 (8, 3),
 (9, 4),
 (10, 4),
 (11, 3),
 (12, 3),
 (13, 4),
 (14, 4),
 (15, 4),
 (16, 1),
 (17, 5),
 (18, 5),
 (19, 3),
 (20, 1)]
 
- How many Weapons does each character have? (Return first 20 rows)
character id, number of weapons. 
[(5, 2),
 (7, 1),
 (11, 1),
 (20, 1),
 (22, 1),
 (23, 1),
 (26, 1),
 (27, 3),
 (29, 2),
 (30, 1),
 (32, 1),
 (34, 1),
 (35, 2),
 (36, 3),
 (37, 2),
 (38, 2),
 (39, 2),
 (40, 1),
 (41, 1),
 (47, 1)]
 
- On average, how many Items does each Character have?
character id, average items for each character
[(1, 54.0),
 (2, 114.0),
 (3, 26.0),
 (4, 81.0),
 (5, 97.0),
 (6, 93.0),
 (7, 91.0),
 (8, 70.0),
 (9, 95.0),
 (10, 128.0),
 (11, 107.0),
 (12, 102.0),
 (13, 67.0),
 (14, 52.0),
 (15, 62.0),
 (16, 87.0),
 (17, 102.0),
 (18, 59.0),
 (19, 57.0),
 (20, 156.0)]
 
- On average, how many Weapons does each character have?
character id, average items for each character
[(5, 0.0),
 (7, 0.0),
 (11, 0.0),
 (20, 0.0),
 (22, 0.0),
 (23, 0.0),
 (26, 0.0),
 (27, 0.0),
 (29, 0.0),
 (30, 0.0),
 (32, 0.0),
 (34, 0.0),
 (35, 0.0),
 (36, 0.0),
 (37, 0.0),
 (38, 0.0),
 (39, 0.0),
 (40, 0.0),
 (41, 0.0),
 (47, 0.0)]



## Assigment - Part 2, Making and populating a Database
from buddymove csv file

- Count how many rows you have - it should be 249!
number of rows = 249
- How many users who reviewed at least 100 `Nature` in the category also
  reviewed at least 100 in the `Shopping` category?
number of users = 78
- (*Stretch*) What are the average number of reviews for each category?
average sports = 12
average religious = 110
average nature = 125
average theatre = 116
average shopping = 113
average picnic = 120