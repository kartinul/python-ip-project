import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

print("df['name']", df["name"])
print("df.loc[2]", df.loc[2])
print("df[:]", df[:])
print("df.loc[:]", df.loc[:])
