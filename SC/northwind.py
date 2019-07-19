#!/usr/bin/env python3
import sqlite3

def query_db(query, con):
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchall()
    return res


def demo_data():
    '''
    Number of rows:  3
    Number of rows where x&y >=5:  2
    Unique y:  2
    '''
    print('PART 1')
    con = sqlite3.connect('demo_data.sqlite3')
    cur = con.cursor()
    cur.executescript(
        '''
        DROP TABLE IF EXISTS demo;
        CREATE TABLE demo(
            s char(1),
            x INTEGER,
            y INTEGER
        )
        '''
    )

    data = [
        ('g,', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)
    ]
    for i in data:
        cur.execute('INSERT INTO demo VALUES (?, ?, ?)', i)
    con.commit()
    row_cnt = query_db('SELECT COUNT(*) FROM demo', con)[0]
    gt_5_7 = query_db('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5',
                      con)[0]
    unique_y = query_db('SELECT COUNT(DISTINCT y) FROM demo', con)[0]
    print('Number of rows: ', row_cnt[0])
    print('Number of rows where x&y >=5: ', gt_5_7[0])
    print('Unique y: ', unique_y[0])

def north_wind():
    '''
    Most expensive products: 
        Côte de Blaye: 263.5
        Thüringer Rostbratwurst: 123.79
        Mishi Kobe Niku: 97
        Sir Rodney's Marmalade: 81
        Carnarvon Tigers: 62.5
        Raclette Courdavault: 55
        Manjimup Dried Apples: 53
        Tarte au sucre: 49.3
        Ipoh Coffee: 46
        Rössle Sauerkraut: 45.6
    Average hire date:  37.22222222222222
    Per City:
            City: Kirkland, Avg hire age: 29.0
            City: London, Avg hire age: 32.5
            City: Redmond, Avg hire age: 56.0
            City: Seattle, Avg hire age: 40.0
            City: Tacoma, Avg hire age: 40.0
    Employee with most territories: 
            id: 7, Robert King, territories: 10
    '''
    print('PART 2')
    con = sqlite3.connect('northwind_small.sqlite3')
    cur = con.cursor()
    res = query_db('SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10', con)
    print('Most expensive products: ')
    for product in res:
        print(f'\t{product[1]}: {product[5]}')
    
    res = query_db('SELECT AVG((HireDate - BirthDate)) FROM Employee', con)
    print('Average hire date: ', res[0][0])
    res = query_db('SELECT City, AVG((HireDate - BirthDate)) FROM Employee GROUP BY City', con)
    print('Per City:')
    for r in res:
        print(f'\tCity: {r[0]}, Avg hire age: {r[1]}')

    res = query_db('''
    SELECT ET.EmployeeId, E.FirstName, E.LastName, COUNT() AS territories
    FROM EmployeeTerritory AS ET
    JOIN Employee AS E ON E.Id = ET.EmployeeId
    GROUP BY EmployeeId
    ORDER BY territories DESC
    LIMIT 1
    ''', con)
    print('Employee with most territories: ')
    top = res[0]
    print(f'\tid: {top[0]}, {top[1]} {top[2]}, territories: {top[3]}')


def main():
    demo_data()
    north_wind()


if __name__ == "__main__":
    main()