import pandas as pd

dfr = pd.read_csv("./16r.csv")
print(dfr)

print()

# Default index_col = None
dfrId = pd.read_csv("./16r.csv", index_col=0)
print(dfrId)


dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
dfw = pd.DataFrame(dic)

dfw.to_csv("./16w.csv")
