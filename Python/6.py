from functions import *
import pandas as pd

s1 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
s2 = pd.Series([10, 20, 40, 60], index=["a", "b", "d", "f"])

printHeading("s1")
print(s1)
breaker()
printHeading("s2")
print(s2)
breaker()
printHeading("s1[::-1]")
print(s1[::-1])
breaker()
printHeading("s1[:2]")
print(s2[:2])
breaker()
printHeading("s1[:2] * 100")
print(s1[:2] * 100)
