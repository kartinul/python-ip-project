from functions import breaker
import pandas as pd

array1 = pd.array([10, 42, 523, 63, 85])

series = pd.Series(array1)

print(f"series:\n{series}")
breaker()
print(f"size:\n{series.size}")
breaker()
print(f"index:\n{list(series.index)}")
breaker()
print(f"shape:\n{series.shape}")
