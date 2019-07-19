### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?

The relationship between `Employee` and `Territory` tables is many-to-many. In other words, Employees can be assigned
to multiple Territories and vice versa. An indicator of this is the interconnecting table `EmployeeTerritories` which is
standard/required for implenting many-to-many relationships in RDMS's.
  
- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
  
A situation where a document store is appropriate would be one where there is unstructured data. More importantly, if you 
are required to utilize commit after every action or input a user is taking/providing, a document store is great. One example
would be a web application where interaction from the user is unpredictable. A document store would not be appropriate where
relational-databases are required and data accuracy is extremely important. Industries including Banking, Government, 
and Healthcare are known for using structured, relational-databases.
  
- What is "NewSQL", and what is it trying to achieve?

NewSQL is a relatively recent paradigm that seeks to provide the best features of non-structed document stores and structured
relational-databases. 
