## Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job): <br>

### In the Northwind database, what is the type of relationship between the Employee and Territory tables? <br>
The relationship between the Employee and Territory tables is an example of a one-to-many relationship. For each Employee there are multiple territories that the employee is responsible for. In this relational database, each employee is linked to multiple territories in the territory table. In contrast, each territory is linked to only one employee. <br>

### What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate? <br>

Non-relational databases like MongoDB is most appropriate in situations where your data is unstructured and complex. MongoDB uses dynamic schemas wherin you do not have to pre-define the structure of your database. This will make your database more flexible as it scales. MongoDB is less appropriate when the data volumes are much smaller and there are legacy systems in place. MongoDB (NoSQL) is also open sourced and there are not many defined standards yet which can make interactions between two NoSQL databases complex. MongoDB is also less appropriate in situations where transactions are highly complex (i.e. banking) and ACID compliance is of upmost importance. MongoDB uses horizontal integration using multiple machines at once to increase computing power as opposed to a single centralized system. Unfortunately, the use of multiple machines means tehse systems cannot simultaneously ensure total consistency.  <br>

### What is "NewSQL", and what is it trying to achieve? <br>
'NewSQL' is a new class of relational database management systems. NewSQl is trying to match the scalability of NoSQL while ensuring the ACID compliance of traditional SQL systems. It is essentially attempting to combine the best of both worlds of traditional SQL systems and NoSQL systems like MongoDB.

