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

Write a summary in the style of a possible blog post, and be prepared with questions and/or discussion topics into class. Bonus - later on, follow up and complete a real
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

Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the questions from the first module (when the RPG data was in
SQLite):
- How many total Characters are there?
- How many total Items?
- How many of the Items are Weapons? How many are not?
- How many Items does each Character have? (Return first 20 rows)
- How many Weapons does each Character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each Character have?


Then with PostgreSQL, answer the following about the your titanic database:

- How many passengers survived, and how many died?
- How many passengers were in each class?
- How many passengers survived/died within each class?
- What was the average age of survivors vs nonsurvivors?
- What was the average age of each passenger class?
- What was the average fare by passenger class? By survival?
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?

Please compare and contrast the difference between these forms of querying and relate it back to the differences discussed in lesson today.
Please turn into Canvas your list of PostGreSQL and MongoDB database queries - this can be in any format (`.py`, .`ipynb`, etc.).

## Resources and Stretch Goals

#### Stretch:
Using the PostGreSQL Titanic Database, how many married couples were aboard the Titanic? Assume that two people (one `Mr.` and one `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are a married couple.

The assignment covered core SQL, but *didn't* review joins - revisit the RPG
data, and do more joins (explicit or implicit) to make sure you understand how
to connect data across tables.

#### Resources: 

Read up on [database
normalization](https://en.wikipedia.org/wiki/Database_normalization) - a variety
of formal techniques for reducing the redundancy of data stored in a relational
database.

Get more reps in! Check out [SQLBolt](https://sqlbolt.com/) and [w3schools SQL
Tutorial](https://www.w3schools.com/sql/), both of which include interactive
exercises. Mastering SQL is all about practice, so continue to work on it regularly and you'll be
confident for your job interviews.
