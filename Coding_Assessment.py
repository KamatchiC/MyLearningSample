import os
import csv
import numpy as np
import pandas as pd
import psycopg2
df = pd.read_csv("C:\\kamatchi\\Employee_data.csv")
print(df)

# Tablename cleanup
file = "Employee_Data"
clean_tbl_name = file.lower()
print(clean_tbl_name)

df.columns = [x.lower().replace("_","") for x in df.columns]
print(df.columns)
print(df.dtypes)
replacements = {
    'object':'varchar',
    'int64':'int'
}

print(replacements)

col_str = ", ".join("{} {}".format(n,d) for (n,d) in zip(df.columns,df.dtypes.replace(replacements)))
print(col_str)

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
cur = conn.cursor()
print("opened database successfully")

#drop tables with same name
cur.execute("drop table if exists Emp_data")

#Create table
cur.execute("CREATE TABLE Emp_data(empid int, ename varchar, dept varchar)")

#inserting values to table
df.to_csv('C:\\kamatchi\\Emp_data.csv', header=df.columns, index=False, encoding='utf-8')
my_file = open('C:\\kamatchi\\Emp_data.csv')
print('file opened in memory')


#Copying data to database
SQL_STATEMENT = """
COPY Emp_data from STDIN WITH 
CSV 
HEADER 
DELIMITER AS ','
"""

cur.copy_expert(sql=SQL_STATEMENT, file=my_file)
print('file copied')

cur.execute("Grant select on table Emp_Data to public")
conn.commit()
conn.close()