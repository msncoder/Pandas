import pandas as pd

data = {
    "name" : ["saad","fahad","samad","asad"],
    "age" : [25,None,35,38],
    "salary":[320,600,None,400],
    "performance_score":[82,90,92,95]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())