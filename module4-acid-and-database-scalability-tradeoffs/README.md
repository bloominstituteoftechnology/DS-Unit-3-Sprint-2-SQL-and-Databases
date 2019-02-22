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

1. sqlite - single user access; easy quick read/write/update; limit to one single application access.
2. PostgreSQL - multi-user usage; relational database; scalable; read/write can be slow when database reach certain size.
3. MongoDB - non-relational; read/write efficient. Update is hard.


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

### How many passengers survived, and how many died?
* SELECT count(*) FROM titanic WHERE Survived = 1 -> 342
* SELECT count(*) FROM titanic WHERE Survived = 0 -> 545

### How many passengers were in each class?
* SELECT Pclass, count(*) FROM titanic GROUP BY Pclass
* [(1, 216), (2, 184), (3, 487)]

### How many passengers survived/died within each class?
* SELECT Pclass, Survived, count(*) FROM titanic GROUP BY Pclass, Survived
* [(3, 0, 368), (3, 1, 119), (1, 0, 80), (2, 1, 87), (1, 1, 136), (2, 0, 97)]

### What was the average age of survivors vs nonsurvivors?
* SELECT AVG(age) FROM titanic where Survived = 1
* [(Decimal('28.4083918128654971'),)]
* SELECT AVG(age) FROM titanic where Survived = 0
* [(Decimal('30.1385321100917431'),)]

### What was the average age of each passenger class?
* SELECT Pclass, AVG(age) from titanic GROUP BY Pclass
* [(1, Decimal('38.7889814814814815')), (2, Decimal('29.8686413043478261')), (3, Decimal('25.1887474332648871'))]

### What was the average fare by passenger class? By survival?
* SELECT Pclass, Survived, AVG(fare) from titanic GROUP BY Pclass, Survived
* [(3, 0, Decimal('13.7118529891304348')), 
* (3, 1, Decimal('13.6948873949579832')), 
* (1, 0, Decimal('64.6840075000000000')), 
* (2, 1, Decimal('22.0557000000000000')), 
* (1, 1, Decimal('95.6080286764705882')), 
* (2, 0, Decimal('19.4123278350515464'))]

### How many siblings/spouses aboard on average, by passenger class? By survival?
* SELECT Pclass, Survived, COUNT(siblingSpouses) from titanic GROUP BY Pclass, Survived
* [(3, 0, 368), (3, 1, 119), (1, 0, 80), (2, 1, 87), (1, 1, 136), (2, 0, 97)]


### How many parents/children aboard on average, by passenger class? By survival?
* SELECT Pclass, Survived, COUNT(parentChildren) from titanic GROUP BY Pclass, Survived
* [(3, 0, 368), (3, 1, 119), (1, 0, 80), (2, 1, 87), (1, 1, 136), (2, 0, 97)]

### Do any passengers have the same name?
* SELECT name FROM titanic GROUP BY name HAVING COUNT(name) > 1
* None same name

- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.

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
