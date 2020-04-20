import sqlite3

DB_FILEPATH = 'data/Review_Chinook_Sqlite.sqlite'

conn =sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()
print(type(conn))

#queries the avg invoice
print("---------------")
query = """
SELECT I.customerID, AVG(I.Total) AS Spent
FROM Invoice I
GROUP BY I.customerID
ORDER BY I.customerID 
LIMIT 5;
"""
curs.execute(query)
result = curs.fetchall()
print("Average Customer Invoice:", result) 

# query for customers in the USA
print("---------------")
query = """SELECT *
FROM Customer C
WHERE C.Country = "USA"
LIMIT 5;
"""
curs.execute(query)
result = curs.fetchall()
print("Customers in the U.S:", result) 

# query for employee with no boss
print("---------------")
query = """ SELECT E.FirstName, E.LastName,
E.Employeeid, E.ReportsTo
FROM Employee E
WHERE E.ReportsTo is NULL
"""
curs.execute(query)
result = curs.fetchall()
print("The Founder has no boss:", result)


# query for number of unique composers
print("---------------")
query = """ SELECT Count(DISTINCT t.Composer)
FROM Track t
"""
curs.execute(query)
result = curs.fetchall()
print("Number of Unique Composers:", result)

print("---------------")
query = """ SELECT Count(DISTINCT t.TrackId)
FROM Track t
"""
curs.execute(query)
result = curs.fetchall()
print("Number of unique Tracks:", result)

#JOINS

#query for all black sbbath tracks
print("---------------")
query = """
SELECT Album.AlbumId, Artist.Name, Album.Title, Track.Name
FROM Artist
LEFT JOIN Album ON Artist.ArtistID = Album.ArtistID
LEFT JOIN Track on Track.AlbumId = Album.AlbumId
WHERE Artist.Name = "Black Sabbath"
ORDER BY Album.AlbumID 
"""
curs.execute(query)
result = curs.fetchall()
print("Black Sabbath Tracks:", result)

#query for most popular genre by num of tracks
print("---------------")
query = """
SELECT Count(t.GenreId) as MostTracks, G.Name
FROM Genre G
JOIN Track t ON G.GenreId = t.GenreId
GROUP By t.GenreId
ORDER BY MostTracks DESC
LIMIT 1;
"""
curs.execute(query)
result = curs.fetchall()
print("Most popular genre:", result)

#query for customers that spent over $45
print("---------------")
query = """
SELECT Sum(I.Total) as Spent, I.CustomerId
FROM Invoice I
GROUP BY 2
    HAVING Spent > 45
"""
curs.execute(query)
result = curs.fetchall()
print("Customers who spend over $45:", result)

# 9. Find the first and last name, title, 
# and the number of customers each employee
#  has helped. If the customer count is 0 for 
#  an employee, it doesn't need to be displayed. 
#  Order the employees from most to least customers.

#query for Employee Customer-Help Count
print("---------------")
query = """
SELECT E.EmployeeId, E.FirstName, E.LastName, E. Title,
COUNT(C.SupportRepId) as HelpCount
FROM Employee E
JOIN Customer C on E.EmployeeId = C.SupportRepId
GROUP By E.EmployeeId
ORDER BY HelpCount DESC;
"""
curs.execute(query)
result = curs.fetchall()
print("Employee-Customer Help Count:", result)


#query for Organization Chart
print("---------------")
query = """ 
SELECT E.EmployeeId, E.FirstName, E.LastName, E.ReportsTo
FROM Employee E
"""
curs.execute(query)
result = curs.fetchall()
print("Company Org Chart:", result)
