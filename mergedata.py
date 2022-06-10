

import pandas as pd

df = pd.read_csv('pokemon_data.csv')
df2=pd.read_csv('datafile2.csv')
dd = [df] + [df2]
print(dd)