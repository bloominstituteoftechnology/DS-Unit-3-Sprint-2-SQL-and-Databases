# ACID and Database Scalability Tradeoffs

Comparing the costs and benefits of relational and non-relational approaches -
can we have the best of both worlds?

## Learning Objectives

- Understand and explain the advantages and disadvantages of traditional SQL
  databases
- Make informed decisions about alternative databases

## Before Lecture

So far in this sprint you've used SQLite, PostgreSQL, and MongoDB. For each of
these, consider the following questions:

- What was easy about using this technology?
- What was hard about using this technology?
- What more would you like to learn about it?

Write a summary in the style of a possible blog post, and bring the
questions/discussion to class. Bonus - later on, follow up and complete a real
blog post about different database technologies!

## Live Lecture Task

We covered a lot of ground this week - today we'll bring it together, both
summarizing and resolving lingering questions. We'll also continue the
discussion from the before lecture activity, and explore the cutting edge
"NewSQL" techniques in active development.

As time allows, we'll go back to practicing good old SQL. It's important to have
a broad awareness of the database universe, but SQL is a time-tested tool that
has and will continue to be useful across a wide range of situations. It will
also be the largest part of the sprint challenge, and likely a component of many
job interviews.

## Assignment

Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite). With PostgreSQL, answer the following:
- select all columns: \d+ titanic

- How many passengers survived, and how many died?

```SELECT CASE WHEN survived=1 THEN 'yes' ELSE 'no' END survived, COUNT(passenger) FROM titanic GROUP BY survived;```
```
survived | count
----------+-------
 no       |   545
 yes      |   342
```
- How many passengers were in each class?

``` SELECT pclass, COUNT(passenger) FROM titanic GROUP BY 1;```

```
pclass | count
--------+-------
      3 |   487
      2 |   184
      1 |   216
```

- How many passengers survived/died within each class?

``` SELECT pclass, CASE WHEN survived=1 THEN 'survived' ELSE 'not survived' END survival, COUNT (DISTINCT passenger) FROM titanic GROUP BY pclass, survived;```

```
pclass |   survival   | count
--------+--------------+-------
      1 | not survived |    80
      1 | survived     |   136
      2 | not survived |    97
      2 | survived     |    87
      3 | not survived |   368
      3 | survived     |   119
```
- What was the average age of survivors vs nonsurvivors?

``` SELECT CASE WHEN survived=1 THEN 'survived' ELSE 'not survived' END survival, ROUND(AVG(age)) average_age FROM titanic GROUP BY 1;```

```
 survival   | average_age
--------------+-------------
 survived     |          28
 not survived |          30
``` 

- What was the average age of each passenger class?

``` SELECT pclass, ROUND(AVG(age)) average_age FROM titanic GROUP BY pclass ORDER BY pclass;```

```
pclass | average_age
--------+-------------
      1 |          39
      2 |          30
      3 |          25
```

- What was the average fare by passenger class? By survival?

``` SELECT pclass, CASE WHEN survived=1 THEN 'survived' ELSE 'not survived' END survival, COUNT(DISTINCT passenger), ROUND(AVG(fare)) average_fare FROM titanic GROUP BY pclass, survival ORDER BY pclass;```

```
pclass |   survival   | count | average_fare
--------+--------------+-------+--------------
      1 | not survived |    80 |           65
      1 | survived     |   136 |           96
      2 | not survived |    97 |           19
      2 | survived     |    87 |           22
      3 | not survived |   368 |           14
      3 | survived     |   119 |           14

```

``` SELECT pclass, ROUND(AVG(fare)) avg_fare FROM titanic GROUP BY pclass ORDER BY pclass; ```

```
pclass | avg_fare
--------+----------
      1 |       84
      2 |       21
      3 |       14
```

- How many siblings/spouses aboard on average, by passenger class? By survival?

``` SELECT pclass, ROUND(AVG(siblings_spouses_aboard),2) average_sibling_spouse FROM titanic GROUP BY pclass ORDER BY pclass;```

```
pclass | average_sibling_spouse
--------+------------------------
      1 |                   0.42
      2 |                   0.40
      3 |                   0.62
```
``` SELECT CASE WHEN survived=1 THEN 'survived' ELSE 'not survived' END survival, ROUND(AVG(siblings_spouses_aboard),2) average_sibling_spouse FROM titanic GROUP BY survival;  ```

```
survival   | average_sibling_spouse
--------------+------------------------
 survived     |                   0.47
 not survived |                   0.56
```

- How many parents/children aboard on average, by passenger class? By survival?

``` SELECT pclass, ROUND(AVG(parents_children_aboard),2) average_parents_children FROM titanic GROUP BY 1 ORDER BY 1;```

```
pclass | average_parents_children
--------+--------------------------
      1 |                     0.36
      2 |                     0.38
      3 |                     0.40
```

``` SELECT CASE WHEN survived=1 THEN 'survived' ELSE 'not survived' END survival, ROUND(AVG(parents_children_aboard),2) average_parents_children FROM titanic GROUP BY survival; ```

```
survival   | average_parents_children
--------------+--------------------------
 survived     |                     0.46
 not survived |                     0.33
``` 

- Do any passengers have the same name?

``` SELECT passenger, COUNT(DISTINCT passenger) count FROM titanic GROUP BY passenger HAVING COUNT(DISTINCT passenger) > 1;```
 0?

- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.

``` SELECT COUNT(DISTINCT passenger) FROM titanic WHERE siblings_spouses_aboard > 0 AND sex='male' AND RIGHT(passenger, POSITION(' ' IN REVERSE(passenger))) LIKE ANY (SELECT RIGHT(passenger, POSITION(' ' IN REVERSE(passenger))) FROM titanic WHERE siblings_spouses_aboard > 0 AND sex='female' AND passenger NOT LIKE 'Miss.%');```

```
count
-------
63
```

## Resources and Stretch Goals

The assignment drilled core SQL, but *didn't* review joins - revisit the RPG
data, and do more joins (explicit or implicit) to make sure you understand how
to connect data across tables.

If you got the Titanic data in your MongoDB cluster - see if you can also answer
the above questions using MongoDB!

Read up on [database
normalization](https://en.wikipedia.org/wiki/Database_normalization) - a variety
of formal techniques for reducing the redundancy of data stored in a relational
database.

Keep working on your written summary from the "before lecture" exercise, and
grow it into a proper blog post. Consider focusing it on one particular
technology or technique, and compare/contrast it with the alternatives.

Get more reps in! Check out [SQLBolt](https://sqlbolt.com/) and [w3schools SQL
Tutorial](https://www.w3schools.com/sql/), both of which include interactive
exercises. Mastering SQL is all about practice, so get it down now and you'll be
confident for your job interviews.
