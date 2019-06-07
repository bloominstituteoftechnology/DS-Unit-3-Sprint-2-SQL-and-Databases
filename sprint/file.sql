SELECT ProductName, UnitPrice from Product order by UnitPrice DESC limit 10;

SELECT AVG(DATE(HireDate)-DATE(BirthDate)) FROM Employee;

SELECT city, AVG(DATE(HireDate)-DATE(BirthDate)) FROM Employee GROUP BY City;

SELECT ProductName, CompanyName FROM Product 
INNER JOIN Supplier ON Product.SupplierId = supplier.Id
ORDER BY UnitPrice DESC limit 10;

SELECT CategoryName, COUNT(ProductName) FROM Category
INNER JOIN Product ON category.Id = CategoryId
GROUP BY CategoryId ORDER BY COUNT(ProductName) DESC LIMIT 1;

SELECT FirstName, LastName, COUNT(TerritoryId) FROM Employee
INNER JOIN EmployeeTerritory ON EmployeeTerritory.EmployeeId = Employee.Id
GROUP BY EmployeeId ORDER BY COUNT(TerritoryId) DESC;
