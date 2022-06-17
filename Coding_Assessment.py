import os
import numpy as np
import pandas as pd
import psycopg2
df = pd.read_csv("C:\\Users\\Employee_data.csv")

print(df)

# tablename cleanup
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

col_str =  ", ".join("{} {}".format(n,d) for (n,d) in zip(df.columns,df.dtypes.replace(replacements)))
print(col_str)


#drop tables with same name

cursor.execute("drop table if exists employeedata")
create table employeedata(empid int, ename varchar, dept varchar)

#inserting values to table

df.to_csv('employeedata.csv',header=df.columns, index=False)
myfile=open('employeedata.csv')
print('file opened')

#Copying data to database
SQLSTATEMENT = COPY employeedata from employeedate with csv HEADER DELIMITER AS ','
cursor.copy.expert(sql=SQL_STATEMENT, file=myfile)

