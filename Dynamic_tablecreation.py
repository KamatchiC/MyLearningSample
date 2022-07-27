import os
import pandas as pd
import csv
import psycopg2
from os import path
import glob
import re

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
print("Connecting to Database")

path_to_dir = "C:\\Python_data\\Employee"
for f in os.listdir(path_to_dir):
    name, extension = path.splitext(f)
    print(name)

# Create a table name
table_name = name
print(table_name)

# Open file
fileInput = open('path_to_dir'/name.csv, "r")

# Extract first line of file
firstLine = fileInput.readline().strip()

# Extract second line of file
secondLine = fileInput.readline()

# Split columns into an array [...]
columns = firstLine.split(",")
col_vals = secondLine.split(",")

# Build SQL code to drop table if exists and create table
sqlQueryCreate = 'DROP TABLE IF EXISTS ' + " abs.ABS_" + table_name + ";\n"
sqlQueryCreate += 'CREATE TABLE' + " abs.ABS_" + table_name + "("

# Define columns for table

for column in columns:
    for dtype in col_vals:
        dt = bool(re.match(r"^\d+?\.\d+?$", dtype))
        if dtype.isdigit():
            dtype = "INTEGER"

        elif dt == True:
            dtype = "FLOAT(2)"

        else:
            dtype = "VARCHAR(64)"

    sqlQueryCreate += column + " " + dtype + ",\n"

sqlQueryCreate = sqlQueryCreate[:-2]
sqlQueryCreate += ");"

print(sqlQueryCreate)

cur = conn.cursor()
cur.execute(sqlQueryCreate)
conn.commit()
cur.close()
