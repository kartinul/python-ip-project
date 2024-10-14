from functions import *
import pandas as pd

dict1 = {
    6: 29,
    7: 27,
    8: 29,
    9: 30,
    10: 31,
}

series = pd.Series(dict1)


printHeading("series")
print(series)
