import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

print(df)
print()
print(f"df.size:\n{df.size}")
print()
print(f"df.shape:\n{df.shape}")
print()
print(f"df.index:\n{list(df.index)}")
print()
print(f"df.name:\n{df.name}")
print()
print(f"df.index.name:\n{df.index.name}")
print()
print(f"df.empty:\n{df.empty}")
