import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = np.random.normal(loc=50, scale=10, size=1000)
plt.figure(figsize=(8,6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Biểu đồ histogram", fontsize=14, fontweight='bold')
plt.xlabel("Giá trị", fontsize=12)
plt.ylabel("Tần suất", fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()