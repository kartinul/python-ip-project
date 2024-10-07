from functions import breaker
import pandas as pd

dic = {"name": ["a", "b", "c", "d"], "age": [42, 63, 12, 51]}
df = pd.DataFrame(dic)

print(f'df:\n\n{df}')
breaker()
print(f"df[df['age' > 40]]:\n\n{df[df['age'] > 40]}")
