import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = np.random.rand(10, 10)
plt.figure(figsize=(8,6))
sns.heatmap(data, annot=True, cmap='YlGnBu', cbar=True)
plt.title("Biểu đồ heatmap của ma trận 10x10", fontsize=14, fontweight='bold')
plt.xlabel("Cột", fontsize=12)
plt.ylabel("Hàng", fontsize=12)
plt.show()