from functions import *
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

printHeading("df.iterrows()", end=":\n")
for i in df.iterrows():
    print(i)
    print("")

breaker()

printHeading("df.items()", end=":\n")
for i in df.items():
    print(i)
    print("")
