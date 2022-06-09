import pandas as pd
data = {'Name':['Alex','Aadhya','Kavin','Priya','Ashu','Vicky','Vinod','Vinay','Gayu','Janani'],
        'Age':[23,34,21,56,35,12,25,23,16,37],
        'Degree':['MCA','BCA','BE','MBA','MCA','BCA','BE','MBA','MCA','BCA']

                }
df=pd.DataFrame(data)

tt= df.head(3)

print("Top listed rows:\n",tt)





