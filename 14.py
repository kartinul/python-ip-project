from functions import breaker
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

print(f'df:\n\n{df}')
breaker()
print(f"df.name:\n\n{df.name}")
breaker()
print(f"df.size = {df.size}")
print(f"df.shape = {df.shape}")
print(f"df.index = {list(df.index)}")
print(f"df.index.name = {df.index.name}")
print(f"df.empty = {df.empty}")
