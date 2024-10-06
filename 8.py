import pandas as pd

series = pd.Series([41, 52, 63, 72, 23])

print(f"series:\n{series}")
print()
print(f"series.head(2):\n{series.head(2)}")
print()
print(f"series.tail(3):\n{series.tail(3)}")
