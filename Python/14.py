from functions import *
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

printHeading("df")
print(df)
breaker()
printHeading("df.name")
print(df.name)
breaker()
print(f"df.size = {df.size}")
print(f"df.shape = {df.shape}")
print(f"df.index = {list(df.index)}")
print(f"df.index.name = {df.index.name}")
print(f"df.empty = {df.empty}")
