# Part 4 Answers

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?

  The type of relationship between the `Employee` and `Territory` tables is
  that of one-to-one, where each row in the `Employee` table correspond
  to one row in the `Territory` table and vice-versa.
  
  In this case, the intermediary table is `EmployeeTerritory`, and the
  relathionship between `Employee` and `EmployeeTerritory` is one-to-one
  through `Employee.Id` and `EmployeeTerritory.EmployeeID`, and
  `EmployeeTerritory` to `Territory` is one-to-one through
  `EmployeeTerritory.TerritoryID` and `Territory.Id`. Together, this makes the
  relationship one-to-one.

- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?

  A document store is appropriate in use for mobile and social networking sites.
  This is because it is much faster than standard RDBMS systems when dealing
  with large amounts of data, especially when needing scalable performance,
  that need to be retrieved quickly and there is not a high need for each
  transaction to be done completely sequentially.

  A document store is not appropriate when there is a need for transactions to
  absolutely be done sequentially, especially in banking situations, where 2
  transactions occurring simultaneously can lead to incorrect balances or
  transactions beween accounts creating possible errors.

- (*Stretch*) What is "NewSQL", and what is it trying to achieve?

  NewSQL is basically a combination of old SQL reliability (ACID) and NoSQL
  scalable performance. It relies heavily on the relational data model of old
  SQL as well as having SQL as the query language. The most mature NewSQL
  system is probably VoltDB, but there are some disadvantages to this model as
  well. Firstly, it is not as general-purpose as SQL, where there needs to be
  serious planning in how the system is used. As well as this, if it is dealing
  with huge amounts of data, it is not as good as NoSQL, as it could require
  terabytes of memory (RAM) for storing certain volumes of data.