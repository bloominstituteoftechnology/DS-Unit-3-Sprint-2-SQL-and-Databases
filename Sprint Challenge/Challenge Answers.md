# Data Science Unit 3 Sprint Challenge 2

### Part 4 - Questions (and your Answers)

**In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?**
- The `employee` and `territory` tables have a one-to-many relationship. This is because each territory is only assigned to one employee, but employees can have multiple territories assigend to them. 

**What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?**
- A document-oriented database, such as MongoDB, tends to be built for horizontal scaling (distributing the database across many servers). The advantage this provides is cheaper compute expenses and high scalability. The disadvantage is that document-oriented databses do not have the ACID gaurantees of traditional relational databases. This makes document store databases inappropraite for datasets where integrity, consistency, and isolation are critical (e.g., banking, traffic control, health records). A document store could be an appropraite choice for a situation that does not require these gaurantees but is extremely large. For example, a database that informs an article recommender system could be a canidate for a document-store database. 

**What is "NewSQL", and what is it trying to achieve?**
- In short, 'NewSQL' is trying to achieve (horizontal) scalability while maintaing the gaurantees typically provided by traditional relational databases (ACID). 