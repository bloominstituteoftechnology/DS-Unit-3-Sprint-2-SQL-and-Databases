- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
  
The relationship between employee and territory is one to many because one employee can be in charge of multiple territories. 

Alternatively, if there are more than one employee in charge of one territory, then it would be a many to one relationship. 

And if there is one employee in charge of one territory, then it is a one to one relationship. 

Needs to more context to fully answer the question. 

- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
  
A document store like MongoDB is more appropriate for a database that is used to power a blog or news website where the data is primarily in text format. MongoDB is primarily for unstructured data that is not stored in rows and columns. NoSQL systems like MongoDB is very flexible and highly scalable. 

MongoDB is less appropriate when dealing with a database that powers a bank because the bank database needs to follow the ACID-compliant (Atomic, Consistency, Isolation, Durability) model. They need to have all their information structured and isolated. 

- What is "NewSQL", and what is it trying to achieve?
NewSQL is trying to combine the scalability of NoSQL systems like MongoDB with the reliability of the ACID system that financial institutions use. 

This way, companies won't have to purchase more powerful computers to scale their ACID systems, they will benefit from the scalability of NoSQL systems. 

Also, they won't have to worry about losing the consistency requirements that is lacking in NoSQL systems but available in ACID systems. 