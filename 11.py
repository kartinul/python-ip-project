from functions import breaker
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

print(f'df:\n\n{df}')
breaker()
print(f"df['name']:\n\n{df["name"]}")
breaker()
print(f"df.loc[2]:\n\n{df.loc[2]}")
breaker()
print(f"df[:]:\n\n{df[:]}")
breaker()
print(f"df.loc[:]:\n\n{df.loc[:]}")
