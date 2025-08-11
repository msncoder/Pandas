import pandas as pd

data = {
    "name" : ["saad","fahad","samad","asad"],
    "age" : [25,36,35,38],
    "salary":[320,600,200,400],
    "performance_score":[82,90,92,95]
}

df = pd.DataFrame(data)
print(pd)

#.loc[]
#df.loc[row_index,"column Name"] = new value

df.loc[0,"salary"] = 5000
print(df)