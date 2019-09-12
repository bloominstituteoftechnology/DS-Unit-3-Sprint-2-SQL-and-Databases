**If a job has SQL in it, this is good prep for potential interview questions.**

What are the ACID properties and why are they important?

Atomicity:
If you choose to bundle some statements together, composing a transaction, then the database guarantees atomicity, which is that if any of the statements fail, the transaction fails to complete, all statements are rolled back and the database is left unchanged.

Consistency:
Any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers. This prevents database corruption by illegal transactions.

Isolation:
Isolate transactions to run things fast. Isolation ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially.

Durability:
Once a transaction is committed, it will remain committed even in the case of a system failure (e.g. power outage).

Practising SQL for the sprint challenge:

```SELECT * FROM Customers```

```SELECT City FROM Customers```

```SELECT DISTINCT Country FROM Customers```

```SELECT * FROM Customers
WHERE City = 'Berlin';```

```SELECT * FROM Customers
WHERE NOT City = 'Berlin'; # NOT comes before the condition
```

```SELECT * FROM Customers
WHERE CustomerID = 32```

```SELECT * FROM Customers
WHERE City = 'Berlin'
AND PostalCode = 12209;```

```SELECT * FROM Customers
WHERE City = 'Berlin'
OR City = 'London' # logical OR is equivalent to natural language and```

```SELECT * FROM Customers
ORDER BY City;  # sorting alphabetically```

```SELECT * FROM Customers
ORDER BY City DESC;```

```SELECT * FROM Customers
ORDER BY Country, City; # order by two columns```

# insert into table
```INSERT INTO Customers(
CustomerName,
Address,
City,
PostalCode,
Country)
VALUES (
'He',
'hhje'
'hjsfhkjd'
'sdfsdf'
'sdfd');```

# Select all records where the column is empty
```SELECT * FROM Customers
WHERE PostalCode IS NULL;```

```SELECT * FROM Customers
WHERE PostalCode IS NOT NULL;```

# Update
```UPDATE Customers
SET City = 'Oslo';```

```UPDATE Customers
SET City = 'Oslo'
WHERE Country  = 'Norway';```

```UPDATE Customers
SET City = 'Oslo',
Country  = 'Norway'
WHERE CustomerID = 32;```

```DELETE FROM Customers
WHERE Country = 'Norway';```

```DELETE FROM Customers;
```

```SELECT MIN(Price)
FROM Products;```

```SELECT MAX(Price)
FROM Products;```

```SELECT COUNT(*)
FROM Products
WHERE Price = 19```

```SELECT AVG(Price)
FROM PRODUCTS```

```SELECT SUM(Price)
FROM Products;```

```SELECT * FROM Customers
WHERE City LIKE 'a%'; # % is wild card character```

```SELECT * FROM Customers
WHERE City LIKE '%a'; # % is wild card character```

```SELECT * FROM Customers
WHERE City LIKE '%a%'; # % is wild card character```

```SELECT * FROM Customers
WHERE City LIKE 'a%b'; # starts with a, ends with b```

```SELECT * FROM Customers
WHERE City LIKE '_a%'; # second char is a```

```SELECT * FROM Customers
WHERE City LIKE '[acs]%'; # where first letter is a or c or s```

```SELECT * FROM Customers
WHERE City LIKE '[a-f]%'; # where first letter is a through f```

```SELECT * FROM Customers
WHERE City LIKE '[^acf]%'; # where first letter is not a, c or f```

```SELECT * FROM Customers
WHERE Country IN ('Norway', 'France')```

```SELECT * FROM Customers
WHERE Country NOT IN ('Norway', 'France')```

```SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;```

```SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;```

```SELECT * FROM Products
WHERE ProductNames BETWEEN 'Geitost' AND 'Pavlovla';```

```SELECT CustomerName,
Address,
PostalCode AS PNO```

```SELECT *
FROM Customers AS Consumers```

```SELECT *
FROM Orders
LEFT JOIN Customers
ON Orders.CustomerID = Customers.CustomerID;```

```SELECT *
FROM Orders
INNER JOIN Customers
ON Orders.CustomerID = Customers.CustomerID;```

```SELECT *
FROM Orders
RIGHT JOIN Customers
ON Orders.CustomerID = Customers.CustomerID; # RJ to select all the records from Customers table, plus all the matches in the Orders table```

```SELECT COUNT(CustomerID),
Country
FROM Customers
GROUP BY Country;```

```SELECT COUNT(CustomerID),
Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;```


SC
Mostly selects, a few create and a few inserts
