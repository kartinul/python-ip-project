from functions import breaker
import pandas as pd

array1 = pd.array([10, 42, 523, 63, 85])

series = pd.Series(array1)

print(f"series:\n\n{series}")
breaker()
print(f"size = {series.size}")
print(f"index = {list(series.index)}")
print(f"shape = {series.shape}")
