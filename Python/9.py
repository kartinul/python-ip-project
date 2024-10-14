from functions import *
import pandas as pd

nestedList = [[40, 15, 125, 73, 52], [52, 125, 66, 73, 23], [42, 52, 74, 25, 24]]

df = pd.DataFrame(nestedList)

printHeading("df")
print(df)
