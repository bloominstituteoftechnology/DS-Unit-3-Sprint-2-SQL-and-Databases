# NoSQL and Document-oriented databases

NoSQL, no worries? Not exactly, but it's still a powerful approach for some
problems.

## Learning Objectives

- Identify appropriate use cases for document-oriented databases
- Deploy and use a simple MongoDB instance

## Before Lecture

Sign up for an account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas),
the official hosted service of MongoDB with a generous (500mb) free tier. You
can also explore the many [MongoDB tools](http://mongodb-tools.com/) out there,
though none in particular are recommended or required for installation (we're
really just checking out MongoDB as a way to understand document-oriented
databases - it's unlikely to become a core part of your toolkit the way SQLite
and PostgreSQL may).

## Live Lecture Task

Another database, same data? Let's try to store the RPG data in our MongoDB
instance, and learn about the advantages and disadvantages of the NoSQL paradigm
in the process. We will depend on
[PyMongo](https://api.mongodb.com/python/current/) to connect to the database.

Note - the
[JSON](https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json)
representation of the data is likely to be particularly useful for this purpose.

## Assignment

Reproduce (debugging as needed) the live lecture task of setting up and
inserting the RPG data (specifically the `charactercreator_character`,
`charactercreator_character_inventory`, `armory_item`, and `armory_weapon`) into 
a MongoDB instance. Your documents in MongoDB should contain the character traits 
(name, lvel, etc.) and skills (strength, wisdom, etc.) and a list of their items. 
You should also store the weapons as a list in another key value pair (you will have 
duplicate items in both items and weapons) - see the example below.

Mongo document example:
```
mongo_document = {
  "name": <VALUE>,
  "level": <VALUE>,
  "exp": <VALUE>,
  "hp": <VALUE>,
  "strength": <VALUE>,
  "intelligence": <VALUE>,
  "dexterity": <VALUE>,
  "wisdom": <VALUE>,
  "items": [
    <ITEM NAME>,
    <ITEM NAME>
  ],
  "weapons" [
    <ITEM NAME>,
    <ITEM NAME>
  ]
}
```

Then answer the following question (can be a comment in the top of your code or in Markdown) - "How 
was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?"

ANSWER: 
------------------------------------------------------------------------------------------------------------------------

I found PostgreSQL to be easier then MongoDB; to elucidate, creating a function that iterated upon the passengers list within the titanic dataset was intuitive, and adding those passengers to our PostgreSQL using Elephant SQL was also intuitive; understanding the concept of using sqlite3 to create a connection to 'bridge the gap' between our final insertion into PostgreSQL was essential. I ran into some errors but finally was able to get it to work well. On the other hand, while MongoDB's interface makes it easier to query data through its implementation of key value pairs using dictionaries, I was not able to input all of my titanic dataset onto Mongo (just parts of it, like we did in class).
------------------------------------------------------------------------------------------------------------------------

There is no other required tasks to turn in, but it is suggested to then revisit
the first two modules, rework/complete things as needed, and just check out with
fresh eyes the SQL approach. Compare and contrast, and come with questions
tomorrow - the main topic will be database differences and tradeoffs!

## Resources and Stretch Goals

Try to insert all the SQLite RPG data tables into your MongoDB cluster.

Put Titanic data in Big Data! That is, try to load `titanic.csv` from yesterday
into your MongoDB cluster.

Push MongoDB - it is flexible and can support fast iteration. Design your own
database to save some key/value pairs for an application you'd like to work on
or data you'd like to analyze, and build it out as much as you can!
