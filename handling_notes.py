import pandas as pd

pathy = 'module2-sql-for-analysis/'

try: 
    x=0
    y=1/x
except ZeroDivisionError as e: 
    print(e) 
else: 
    report = "y has been computed to {}".format(y)
    try: 
        int(report)
    except ValueError as e:
        print(e)
    else: 
        print(report)
    
    print("y has been computed to ", y)
finally:
    print("fin") 

