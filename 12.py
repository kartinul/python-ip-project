import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
indexId = [100, 101, 102, 103]
df = pd.DataFrame(dic, index=indexId)


def printHead(str):
    print(str)


# Orginal Dataframe
printHead("Orginal Dataframe")
print(df)
print()

# Rename column
df = df.rename({"age": "currentAge"}, axis=1)
print(df)
print()

# Rename row
df = df.rename({100: 110}, axis=0)
print(df)
print()

# Count function
print(df.count(axis=0))
print()


# Update
toUpdate = pd.DataFrame({"currentAge": [17]}, index=[101])
df.update(toUpdate)
print(df)
# OR
df.loc[101, "currentAge"] = 63
print(df)


# Add row
df.loc[104] = ["e", 18]
print(df)

# Add column
df["DateOfDeath"] = 2065
print(df)
