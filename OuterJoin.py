import pandas as pd
df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)
df2 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)
print(df1)
print(df2)
print("Outer Join:")
result = pd.concat([df1, df2], axis=1)
Testdata = result.fillna('XX')
print(Testdata)

print("Inner Join:")
result1 = pd.concat([df1, df2], axis=1, join="inner")
print(result1)

