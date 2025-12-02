import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
hours = np.linspace(1, 10, 50)

noise = np.random.normal(0, 1, 50)

score = hours * 1.2 + noise

df = pd.DataFrame({
    'hours': hours,
    'score': score
})

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x='hours', y='score', s=100, color='blue', alpha=0.6, edgecolor='black')

sns.regplot(data=df, x='hours', y='score', scatter=False, color='red', line_kws={'linewidth': 2, 'label': 'Đường xu hướng'})

plt.title("Mối quan hệ giữa số giờ học và điểm thi", fontsize=14, fontweight='bold')
plt.xlabel("Số giờ học", fontsize=12)
plt.ylabel("Điểm thi", fontsize=12)

plt.legend()

plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
correlation = df['hours'].corr(df['score'])
