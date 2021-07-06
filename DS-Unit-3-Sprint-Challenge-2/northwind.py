#!/usr/bin/env python

import sqlite3


conn = sqlite3.connect('northwind_small.sqlite3')


def most_expensive():
    """Finds the most expensive units per price."""
    conn = sqlite3.connect('northwind_small.sqlite3')
    curs = conn.cursor()
    query = 'SELECT ProductName, UnitPrice FROM Product ' \
            'ORDER BY UnitPrice  DESC ' \
            'LIMIT 10;'
    result = curs.execute(query)
    top10 = result.fetchall()

    return print('10 Most Expensive Product:', top10)


def avg_hire_age():
    """Queries for the average age of employees at hire date"""
    conn = sqlite3.connect('northwind_small.sqlite3')
    curs = conn.cursor()
    query = 'SELECT AVG(HireDate - BirthDate) ' \
            'FROM Employee;'
    result = curs.execute(query)
    aha = result.fetchall()

    return print('Employee average age at hire date:', aha[0][0])


def most_expensive_with_supplier():
    """Finds the most expensive units per price."""
    conn = sqlite3.connect('northwind_small.sqlite3')
    curs = conn.cursor()
    query = 'SELECT ProductName, CompanyName, UnitPrice FROM Product ' \
            'INNER JOIN Supplier ' \
            'ON Product.SupplierID = Supplier.Id ' \
            'ORDER BY UnitPrice DESC ' \
            'LIMIT 10;'
    result = curs.execute(query)
    top10_ws = result.fetchall()

    return print('10 Most Expensive Product with Suppliers:', top10_ws)


def top_unique_category():
    """Queries for the largest unique
     category"""
    conn = sqlite3.connect('northwind_small.sqlite3')
    curs = conn.cursor()
    query = 'SELECT CategoryName, MAX(DISTINCT Description) ' \
            'FROM Category;'
    result = curs.execute(query)
    tulc = result.fetchall()

    return print('Largest unique category:', tulc[0])