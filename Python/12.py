from functions import *
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
indexId = [100, 101, 102, 103]
df = pd.DataFrame(dic, index=indexId)


# Orginal Dataframe

printHeading("Orginal Dataframe")
print(df)
breaker()

# Rename column
df = df.rename({"age": "currentAge"}, axis=1)

printHeading("Renamed Dataframe's Column")
print(df)
breaker()

# Rename row
df = df.rename({100: 110}, axis=0)

printHeading("Renamed Dataframe's Row")
print(df)
breaker()

# Count function

printHeading("Count rows")
print(df.count(axis=0))
breaker()

# Count function

printHeading("Count columns")
print(df.count(axis=1))
breaker()

# Update
toUpdate = pd.DataFrame({"currentAge": [17]}, index=[101])
df.update(toUpdate)

printHeading("Updated Dataframe Value")
print(df)
breaker()

# OR
df.loc[101, "currentAge"] = 63

printHeading("Updated Dataframe Value")
print(df)
breaker()


# Add row
df.loc[104] = ["e", 18]

printHeading("Added row")
print(df)
breaker()

# Add column
df["DateOfDeath"] = 2065

printHeading("Added column")
print(df)
