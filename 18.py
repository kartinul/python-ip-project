import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("./18.csv")

df.plot(kind="bar")

plt.show()
