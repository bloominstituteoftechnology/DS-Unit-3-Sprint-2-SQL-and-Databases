import pandas as pd

file_path = 'https://github.com/RAV10K1/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/buddymove_holidayiq.csv'
df = pd.read_csv(file_path)

df.head()