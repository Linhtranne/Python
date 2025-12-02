
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
x = np.random.randint(0, 51, 100)
y = np.random.randint(0, 51, 100)
plt.figure(figsize=(8,6))
sns.scatterplot(x=x, y=y, color='purple', s=80, edgecolor='black', alpha=0.7)
plt.title("Biểu đồ scatter của x và y", fontsize=14, fontweight='bold')
plt.xlabel("Giá trị x", fontsize=12)
plt.ylabel("Giá trị y", fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
