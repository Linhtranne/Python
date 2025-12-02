import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y1 = x
y2 = x**2
y3 = x**3
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = x', color='blue', linewidth=2)
plt.plot(x, y2, label='y = x²', color='green', linewidth =2)
plt.plot(x, y3, label='y = x³', color='red', linewidth=2)
plt.legend()
plt.show()