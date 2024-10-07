from functions import breaker
import pandas as pd

s1 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
s2 = pd.Series([10, 20, 40, 60], index=["a", "b", "d", "f"])

print(f"s1:\n\n{s1}")
breaker()
print(f"s2:\n\n{s2}")
breaker()
print(f"s1[::-1]:\n\n{s1[::-1]}")
breaker()
print(f"s1[:2]:\n\n{s2[:2]}")
breaker()
print(f"s1[:2] * 100:\n\n{s1[:2] * 100}")
