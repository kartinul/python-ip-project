import pandas as pd

series = pd.Series([41, 63, 18, 52, 63])

series.index = ["a", "b", "c", "d", "e"]

print(f"series:\n{series}")
