import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

#Part 2 - Question 1
price_query = '''	SELECT Id, ProductName, UnitPrice
					FROM Product
					ORDER BY UnitPrice DESC
					LIMIT 10;'''

curs.execute(price_query)
top_ten=curs.fetchall()
print(top_ten,'\n')

#Part 2 Question 2
emp_age_query='''SELECT AVG(HireDate - BirthDate) from Employee'''
curs.execute(emp_age_query)
avg_age=curs.fetchall()
print(avg_age,'\n')




#Part 3 Question 1
price_supp_query='''SELECT ProductName, UnitPrice, CompanyName
					FROM Product
					INNER JOIN Supplier
					ON Product.SupplierId = Supplier.Id
					ORDER BY UnitPrice DESC
					LIMIT 10;'''

curs.execute(price_supp_query)
top_ten_supp=curs.fetchall()
print(top_ten_supp,'\n')


#Part 3 Question 2
largest_cat_query='''	SELECT CategoryId,CategoryName,COUNT(CategoryName)
						FROM Product
						INNER JOIN Category
						ON Product.CategoryId = Category.Id
						GROUP BY CategoryName
						ORDER BY COUNT(CategoryName) DESC
						LIMIT 1;'''
curs.execute(largest_cat_query)
largest_cat=curs.fetchall()
print(largest_cat)



#In the Northwind database, what is the type of relationship between Employee and Territory
#Tables?

#EmployeeTerritories is a join of both Employees and Territories. EmployeeTerritories is 
#needed to make relation between the two tables. EmployeeTerritories matches EmployeeID's with
#Territory ID's. 



#What is a situation where a document store (like MongoDB) is appropriate, and 
#what is a situation where it is not appropriate?

#Document stores are useful because they can be implemented on very large and distributed
#scales. Large projects that require more data than what can easily fit in memory benefit from
#a DB like MongoDB, because the load can be shared by multiple servers/machines. The drawbacks
# of using MongoDB include: Difficulty implementing SQL style relations, Queries are more
#difficult to write. A document store would not be appropriate for small scale projects or
#applications.

