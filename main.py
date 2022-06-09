
#print(df.iloc[1,2])

#print(df.head(3))

# df.iterrows()

# print(index,Row)

print(df.iloc[5,2])

print(df.head(6))


dd=df.loc[df['Name'] == "Chespin"]
print(dd)


#print(df.describe())

df.sort_values('Type 1',ascending=0)
print(df)

#print(df.info())