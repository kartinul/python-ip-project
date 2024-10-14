from functions import *
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

printHeading("df")
print(df)
breaker()
printHeading("df['name']")
print(df["name"])
breaker()
printHeading("df.loc[2]")
print(df.loc[2])
breaker()
printHeading("df[:]")
print(df[:])
breaker()
printHeading("df.loc[:]")
print(df.loc[:])
