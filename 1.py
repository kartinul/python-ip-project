import pandas as pd
import numpy as np


n = 5
array = np.arange(2, (n * 2) + 1, 2)
series = pd.Series(array)

# arraySelf = [2, 4, 6, 8, 10]
# series = pd.Series(arraySelf)

print(f"series:\n\n{series}")
