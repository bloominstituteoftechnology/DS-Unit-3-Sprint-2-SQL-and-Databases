## Part 4 Interview Questions

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?

  There is a many to many relationship between Employees and Territories.
  The table EmployeeTerritories joins Employee with each Employee has many entries in EmployeeTerritories. Territories joins EmployeeTerritories where each territory has multiple entries in EmployeeTerritories as well.
  This sets up the Many to Many relationship by having a table inbetween the two tables that serves to allow SQL to implement the Many to Many relationship.

- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?

  One example of where a Document Store Database would be appropriate is in a Medical Professional's Office. Each patient must have their own individual file. And there should be no easy way to cross information between patients, each one should be completely separate and individually isolated. This goes into confidentiality, and regulations put on the medical professionals.

- What is "NewSQL", and what is it trying to achieve?

  NewSQL is a new database type that mixes the traditional SQL Database, and other types of Databases. The goal is to keep some relationships as they really improve performance times, while allowing for flexibility in the requirements of the physical hardware they exist on. One example I can think of now, is using SQL databases with document store databases, all ofthe relational data can be kept in SQL, and the data that is not able to be indexed is placed in a document store database while the whole time the SQL database keeps up with that data as SQL isn't good with handling unindexed data.
