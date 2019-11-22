- How many passengers survived, and how many died?

SELECT COUNT(*) FROM "public"."titanic"
WHERE survived='true';
342
SELECT COUNT(*) FROM "public"."titanic"
WHERE survived='false';
545

- How many passengers were in each class?

SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='1';
216

SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='2';
184

SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='3';
487

- How many passengers survived/died within each class?
SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='1' AND survived='true';
136

SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='1' AND survived='false';
80

SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='2' AND survived='true';
87

SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='2' AND survived='false';
97

SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='3' AND survived='true';
119

SELECT COUNT(*) FROM "public"."titanic"
WHERE pclass='3' AND survived='false';
386

- What was the average age of survivors vs nonsurvivors?

SELECT AVG(age) FROM "public"."titanic"
WHERE survived='true'
28.4

SELECT AVG(age) FROM "public"."titanic"
WHERE survived='false'
30.1

- What was the average age of each passenger class?
SELECT AVG(age) FROM "public"."titanic"
WHERE pclass='1';
38.71

SELECT AVG(age) FROM "public"."titanic"
WHERE pclass='2';
29.86

SELECT AVG(age) FROM "public"."titanic"
WHERE pclass='3';
25.18

- What was the average fare by passenger class? By survival?


- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.
