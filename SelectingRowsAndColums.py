import pandas as pd

data = {
    "name" : ["saad","fahad","samad","asad"],
    "age" : [25,36,35,38],
    "salary":[320,600,200,400],
    "performance_score":[82,90,92,95]
}

# secting columns

df = pd.DataFrame(data)
# print(df)

# print("Names of single column return")
# name = df['name']
# print(name)

# name_and_age = df[['name','age']]
# print(name_and_age)


#selcting rows

# high_salary = df[df['salary'] > 500]
# print("Employees who have grater then salary 500")
# print(high_salary)

# filtered = df[(df['salary'] > 200) & (df['age'] > 20)]
# print(filtered)

filtered_2 = df[(df['performance_score'] > 320) | (df['age'] > 30)]
print(filtered_2)