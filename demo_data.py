import sqlite3
connection = sqlite3.connect("demo_data.sqlite3") 
crsr = connection.cursor() 
sql_command = """CREATE TABLE demos(
s varchar(1)PRIMARY KEY,  
x integer not null,  
y integer not null 
);"""
crsr.execute(sql_command) 
sql_command = """INSERT INTO demos VALUES ('g', 3, 9);"""
crsr.execute(sql_command)
sql_command = """INSERT INTO demos VALUES ('v', 5, 7);"""
crsr.execute(sql_command)
sql_command = """INSERT INTO demos VALUES ('f', 8, 7);"""
crsr.execute(sql_command)
connection.commit() 
connection.close()
connection = sqlite3.connect("demo_data.sqlite3") 
crsr = connection.cursor() 
crsr.execute("SELECT COUNT(*) FROM demos")  
ans= crsr.fetchall()  
for i in ans: 
    print(i) 
ans= crsr.fetchall()  
for i in ans: 
    print(i)
crsr.execute("SELECT COUNT (DISTINCT y) FROM demo")  
ans= crsr.fetchall()  
for i in ans: 
    print(i)
 
