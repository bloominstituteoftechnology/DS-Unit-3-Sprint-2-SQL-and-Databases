## Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the Employee and Territory tables?
The relationship between `Employee` and `Territory` is **Many-to-Many (M:M)**, which is resolved using a *junction table* - `EmployeeTerritory` which connects both `Employee` and `Territory` with **two** **One-to-Many (1:M)** relationship. So, we can say `Employee` and `Territory` is pair of **1:M** relationships.

Reference: [Many-to-Many](https://en.wikipedia.org/wiki/Many-to-many_%28data_model%29)

- What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

Document Store like MongoDB store documents as **Key-Value** pairs, they also allow nested **Key-Value** pairs which allows for *flexibility in storing data without preemptively specifying structure*. Which allows for faster prototyping, and is good for situations where you need to rapidly develop and deploy to get quick feedback. As oppose to Relational databases which require a rigid schema structure, NoSQl is schema-free. 

One situation where MongoDB would be appropriate is: When you are a small startup and need to rapidly develop and iterate through prototypes and scale easily, in order to demonstrate functionality to investors, and keep up with increasing demand.

Alternatively, when it's not appropriate: Is when you are a dealing with financial data, like Banks, where mission critical-data demands for high reliability and integrity than scalability. For example, Banks need a Relational database, that has a up-front schema, as oppose schema-free Document Store database.  

- What is "NewSQL", and what is it trying to achieve?

**NewSQL** is defines a class of RDBMS that seek to provide the scalability of NoSQL databases while maintaining the ACID guarantees of a traditional databases. Goal they are trying to achieve is high scalability of NoSQL databases and relational data model that confirms ACID properties. Think of how many transactions are made by Banks, or giant super stores like Walmart, where conventional relational databases fail to scale, NewSQL resolves this issue. 