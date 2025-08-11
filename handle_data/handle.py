import pandas as pd

data = {
    "name" : ["saad","fahad","samad","asad"],
    "age" : [25,None,35,38],
    "salary":[320,600,None,400],
    "performance_score":[82,90,92,95]
}

df = pd.DataFrame(data)
print(df)
#ye null value k rows ko frop kr dy ga
# df.dropna(inplace=True)
# print(df)

# ye null value ko 0 assign kr dy ga
df.fillna(0,inplace=True)
print(df)

df['age'].fillna(df['age'].mean(),inplace=True)