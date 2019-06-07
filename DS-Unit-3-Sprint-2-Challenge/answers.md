- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables? The Employee and Territory tables has a 'Many to Many' relationship. Therefore we make a EmployeeTerritories table to normalize it.
- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate? Document store is appropriate in a situation when scale is important or schema is impossible. But its not appropriate in the situation where ACID is a must, for example, bank records.
- What is "NewSQL", and what is it trying to achieve? NewSQL is a combination of relational database and NoSQL. It tries to get some advantage from relational database and NoSQL by considering their tradeoff, CAP.