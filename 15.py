import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

print("df.iterrows():")
for i in df.iterrows():
    print(i)

print()

print("df.items():")
for i in df.items():
    print(i)
