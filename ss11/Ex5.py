import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
x = np.linspace(0, 10, 100)
y1 = x
y2 = x**2
axs[0, 0].plot(x, y1, label='y = x', color='blue', linewidth=2)
axs[0, 0].set_title("Đường thẳng y = x", fontsize=14, fontweight='bold')
axs[0, 0].set_xlabel("Trục x", fontsize=12)
axs[0, 0].set_ylabel("Trục y", fontsize=12)
axs[0, 0].legend()
axs[1, 0].plot(x, y2, label='y = x²', color='green', linewidth=2)
axs[1, 0].set_title("Đường parabol y = x²", fontsize=14, fontweight='bold')
axs[1, 0].set_xlabel("Trục x", fontsize=12)
axs[1, 0].set_ylabel("Trục y", fontsize=12)
axs[1, 0].legend()
x_scatter = np.random.randint(0, 51, 100)
y_scatter = np.random.randint(0, 51, 100)
sns.scatterplot(x=x_scatter, y=y_scatter, color='purple', s=80, edgecolor='black', alpha=0.7, ax=axs[0, 1])
axs[0, 1].set_title("Biểu đồ scatter của x và y",fontsize =14, fontweight='bold')
axs[0, 1].set_xlabel("Giá trị x", fontsize=12)
axs[0, 1].set_ylabel("Giá trị y", fontsize=12)
axs[0, 1].legend()
x_lin = np.linspace(1, 10, 50)
noise = np.random.normal(0, 1, 50)
y_lin = x_lin * 1.2 + noise
df = pd.DataFrame({'hours': x_lin, 'score': y_lin})
sns.scatterplot(data=df, x='hours', y='score', s=100, color='blue', alpha=0.6, edgecolor='black', ax=axs[1, 1])
sns.regplot(data=df, x='hours', y='score', scatter=False, color='red', line_kws={'linewidth': 2, 'label': 'Đường xu hướng'}, ax=axs[1, 1])
axs[1, 1].set_title("Mối quan hệ giữa số giờ học và điểm thi", fontsize=14, fontweight='bold')
axs[1, 1].set_xlabel("Số giờ học", fontsize=12)
axs[1, 1].set_ylabel("Điểm thi", fontsize=12)
axs[1, 1].legend()
plt.show()