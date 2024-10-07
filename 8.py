from functions import breaker
import pandas as pd

series = pd.Series([41, 52, 63, 72, 23])

print(f"series:\n\n{series}")
breaker()
print(f"series.head(2):\n\n{series.head(2)}")
breaker()
print(f"series.tail(3):\n\n{series.tail(3)}")
