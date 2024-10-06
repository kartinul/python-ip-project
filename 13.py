import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

print(f"df: {df}")
print()
print(f"df[df['age' > 40]]: {df[df['age'] > 40]}")
