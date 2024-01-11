import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('favour N.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()