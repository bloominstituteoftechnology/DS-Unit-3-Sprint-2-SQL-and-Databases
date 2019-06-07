# In the Northwind database, what is the type of relationship between the Employee and Territory tables?

- The type of relationship between Employee and the Territory tables is a 'many to many' relationship. In this example,the many to many relationship allows for one employee to be related to several territories. Additionally, the territories can be assigned several times to different employees.

# What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

- A document store may be appropriate in a situation where the structure of the data does not matter.  For example a simple note taking system would make use of this.  One can manipulate it, add tables, fields, that do not have to pertain to any rules.  A situation where it would not be appropriate is where a record and changes have to be kept tidy and structured.  Money transactions come to mind.  Essentially any system that requires ACID, is best used with options other than document stores.

# What is "NewSQL", and what is it trying to achieve?
- NewSQL is a new type of database related to both relational databases and graph databases.  NewSQL is trying to achieve the best of both worlds.  The advantages of the horizontal capabilities of graph databases, as well as the advantages of having ACID properties from relational databases.