from functions import *
import pandas as pd

print("READING...\n")
dfr = pd.read_csv("./CSV/16r.csv")
print(dfr)

breaker()

print("READING and setting id as index...\n")
# Default index_col = None
dfrId = pd.read_csv("./CSV/16r.csv", index_col=0)
print(dfrId)

breaker()

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
dfw = pd.DataFrame(dic)

print(dfw)
print()
print("WRITING...")

dfw.to_csv("./CSV/16w.csv")
