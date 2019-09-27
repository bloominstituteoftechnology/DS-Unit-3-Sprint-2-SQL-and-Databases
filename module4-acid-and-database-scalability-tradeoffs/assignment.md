# Assignment

Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite). With PostgreSQL, answer the following:

- How many passengers survived, and how many died?
> 342 survived and 545 died
- How many passengers were in each class?
> 1st - 216, 2nd - 184, 3rd - 487
- How many passengers survived/died within each class?
> 1st:	136 survived, 80 died
> 2nd: 87 suvived, 97 died
> 3rd: 119 survived, 368 died
- What was the average age of survivors vs nonsurvivors?
> The average age of survivors was 28; the average age of nonsurvivors was 30.
- What was the average age of each passenger class?
> 1st - 38, 2nd -29, 3rd - 25
- What was the average fare by passenger class? By survival?
> 1st - 84.15, 2nd - 20.66, 3rd - 13.71
> survived - 22.21, didn't survive - 48.40
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
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
