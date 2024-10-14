from functions import *
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

printHeading("df")
print(df)
breaker()
printHeading("df[df['age' > 40]]")
print(df[df["age"] > 40])
