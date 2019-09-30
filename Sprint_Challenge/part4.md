In the Northwind database, what is the type of relationship between the Employee and Territory tables?
Employee and Territory tables are related to each other via a Employee Territory. When these are joined by using Id columns we get One to Many relation between Employee and Territory tables. This is because each employee as many territories. 

What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
MongoDB is a no SQL database management system. This mean there is no need to have a strict schema and partitioning of data. This gives more flexibility of adding data. Different types of data can be added quickly without having to re-structure. MongoDB is ideal for systems where there are a number of different types of records to be stored whose format might change at a rapid pace. A downside of MongoDB is that its not as strongly ACID-compliant (Atomic, Consistency, Isolation, Durability) as the more well-established SQL systems. 

What is "NewSQL", and what is it trying to achieve?
NewSQL is defines a class of RDBMS(Relational Database Management Systems) that seek to provide the scalability of NoSQL databases while maintaining the ACID guarantees of a traditional databases.
By joining SQL reliability with NoSQL speed and performance, NewSQL provides better functionality and services.