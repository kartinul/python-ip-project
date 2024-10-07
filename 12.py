from functions import breaker
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
indexId = [100, 101, 102, 103]
df = pd.DataFrame(dic, index=indexId)


# Orginal Dataframe

print(f"Orginal Dataframe:\n\n{df}")
breaker()

# Rename column
df = df.rename({"age": "currentAge"}, axis=1)
print(f"Renamed Dataframe's Column:\n\n{df}")
breaker()

# Rename row
df = df.rename({100: 110}, axis=0)
print(f"Renamed Dataframe's Row:\n\n{df}")
breaker()

# Count function
print(f"Count rows:\n\n{df.count(axis=0)}")
breaker()

# Count function
print(f"Count columns:\n\n{df.count(axis=1)}")
breaker()

# Update
toUpdate = pd.DataFrame({"currentAge": [17]}, index=[101])
df.update(toUpdate)
print(f"Updated Dataframe Value:\n\n{df}")
breaker()

# OR
df.loc[101, "currentAge"] = 63
print(f"Updated Dataframe Value:\n\n{df}")
breaker()


# Add row
df.loc[104] = ["e", 18]
print(f"Added row:\n\n{df}")
breaker()

# Add column
df["DateOfDeath"] = 2065
print(f"Added column:\n\n{df}")
