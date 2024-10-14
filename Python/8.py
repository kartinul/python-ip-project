from functions import *
import pandas as pd

series = pd.Series([41, 52, 63, 72, 23])

printHeading("series")
print(series)
breaker()
printHeading("series.head(2)")
print(series.head(2))
breaker()
printHeading("series.tail(3)")
print(series.tail(3))
