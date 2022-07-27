import os
import pandas as pd
import csv
import psycopg2
from os import path
import glob
import re

with open('mydata.csv', 'rb') as f:
    csvreader = csv.reader(f, delimiter=' ')
    print(csvreader)
