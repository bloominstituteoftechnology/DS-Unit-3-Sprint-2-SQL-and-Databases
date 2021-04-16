/* 10 most expensive items (per unit price) */
SELECT ProductName, UnitPrice 
	from Product
	ORDER BY UnitPrice DESC
	LIMIT 10;

/* Average Age of Employees at Hire */
SELECT ROUND(AVG(HireDate - BirthDate)) as "average hire age" 
	from Employee;

/* Average Age of Employees at Hire by City */
SELECT City, ROUND(AVG(HireDate - BirthDate)) as "average hire age by City" 
	from Employee
	GROUP BY City;
