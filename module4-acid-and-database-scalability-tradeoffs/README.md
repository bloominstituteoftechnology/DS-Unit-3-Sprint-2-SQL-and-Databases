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

- How many passengers survived, and how many died?
    SELECT SUM(survived)
    FROM titanic_table2;
    
    342

- How many passengers were in each class?
    SELECT pclass, SUM(pclass) AS total_passengers
    FROM titanic_table2
    GROUP BY pclass;

    1	216
    2	368
    3	1461

- How many passengers survived/died within each class?
    SELECT pclass, survived AS survived_died, Count(survived)
    FROM titanic_table2
    GROUP BY pclass, survived
    ORDER BY pclass, survived_died;

    pclass	survived_died	count
        1	      0	        80
        1	      1	        136
        2	      0	        97
        2	      1	        87
        3	      0	        368
        3	      1	        119

- What was the average age of survivors vs nonsurvivors?
    SELECT survived, AVG(age)
    FROM titanic_table2
    GROUP BY survived;

    survived	avg
        0	30.1385321100917
        1	28.4083918128272

- What was the average age of each passenger class?
    SELECT pclass, AVG(age)
    FROM titanic_table2
    GROUP BY pclass;

    pclass	avg
      1	    38.7889814815587
      2	    29.8686413042571
      3	    25.188747433238

- What was the average fare by passenger class? By survival?
    SELECT pclass, AVG(fare) AS avg_fare
    FROM titanic_table2
    GROUP BY pclass;

    pclass	avg_fare
        1	84.154687528257
        2	20.6621831810993
        3	13.7077075010452    

    SELECT survived, AVG(fare) AS avg_fare
    FROM titanic_table2
    GROUP BY survived;
    
    survived	avg_fare
        0	    22.2085840951412
        1	    48.3954076976107

- How many siblings/spouses aboard on average, by passenger class? By survival?
    SELECT pclass, AVG(siblings_spouses_aboard) avg_relatives
    FROM titanic_table2
    GROUP BY pclass;

    pclass	avg_relatives
        1	0.41666666666666666667e0
        2	0.40217391304347826087e0
        3	0.62012320328542094456e0

    SELECT survived, AVG(siblings_spouses_aboard) avg_relatives
    FROM titanic_table2
    GROUP BY survived;

    survived	avg_relatives
        0	    0.5577981651376146789e0
        1	    0.47368421052631578947e0

- How many parents/children aboard on average, by passenger class? By survival?
    SELECT pclass, AVG(parents_children_aboard) avg_parent_child
    FROM titanic_table2
    GROUP BY pclass;

    pclass	avg_parent_child
    1	    0.35648148148148148148e0
    2	    0.38043478260869565217e0
    3	    0.39630390143737166324e0

    SELECT survived, AVG(parents_children_aboard) avg_parent_child
    FROM titanic_table2
    GROUP BY survived;

    survived	avg_parent_child
    0	        0.33211009174311926606e0
    1	        0.46491228070175438596e0

- Do any passengers have the same name?
    SELECT name
    FROM titanic_table2
    GROUP BY name
    HAVING COUNT(*) > 1;

    NO RESULTS!!


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
