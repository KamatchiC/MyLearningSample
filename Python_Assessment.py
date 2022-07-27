import csv
import psycopg2
import os
import glob
import re

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
cur = conn.cursor()
print("opened database successfully")
csvPath = "C:\\kamatchi\\Employee_data.csv"

# Loop through each CSV
for filename in glob.glob(csvPath + "*.csv"):
    # Create a table name
    table_name = filename.replace("C:\\kamatchi\\Employee_data.csv", "").replace(".csv", "")
    print(table_name)

    # Open file
    fileInput = open(filename, "r")

    # Extract first line of file
    firstLine = fileInput.readline().strip()

    # Extract seconf line of file
    secondLine = fileInput.readline()

    # Split columns into an array [...]
    columns = firstLine.split(",")
    colvals = secondLine.split(",")

    # Build SQL code to drop table if exists and create table
    sqlQueryCreate = 'DROP TABLE IF EXISTS ' + " abs.ABS_" + tablename + ";\n"
    sqlQueryCreate += 'CREATE TABLE' + " abs.ABS_" + tablename + "("

    # Define columns for table
    for column in columns:
        for dtype in colvals:
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