Part 4 - Questions (and your Answers)¶
Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

In the Northwind database, what is the type of relationship between the Employee and Territory tables?
What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
What is "NewSQL", and what is it trying to achieve?

There are a few different types of relationship between SQL tables:  One-to-Many, One-to-One, and Many-to-Many.  In this case it is a One-to-One as a single record in the first table is related to only one record in the second table.

MongoDB is a non-relational database system which stores the data in JSON which is much like a Python dictionary.  As such it is better for databases that have no clear schema definitions.  For example a start-up may be unsure of how exactly to organise its database, and having a MongoDB database would allow that database sturcture to evolve over time.  
In the case where you have more established business model, where accuracy and reliability are more important and you have a clear database structure that you could adhere to, SQL would be the much better choice.

NewSQL is a term for new types of relational database models that various companies are tryign to create.  These companies want the best of both worlds - i.e. the relaibility of SQL with the scalability of MongoDB style (noSQL) offerings.  They have been heavily used in teh realtively new businesses of transaction processing where you need total relaibility due to transactional nature of the business, but more freedom than traditional SQL allows.
