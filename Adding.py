import pandas as pd

data = {
    "name" : ["saad","fahad","samad","asad"],
    "age" : [25,36,35,38],
    "salary":[320,600,200,400],
    "performance_score":[82,90,92,95]
}


df = pd.DataFrame(data)
print(df)

df["Bonus"] = df['salary'] * 0.1
print(df)

df.insert(0,"Employee_ID",[10,20,30,40])
print(df)