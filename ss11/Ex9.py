import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
x =np.arange(1, 31)
y = 20 + 10 * np.sin((x - 1) * (2 * np.pi / 30)) + np.random.normal(0, 2, 30)
df = pd.DataFrame({"day": x, "value": y})
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="day", y="value", marker="o")
plt.title("Biểu đồ dữ liệu nhiễu", fontsize=14, fontweight='bold')
plt.xlabel("Ngày", fontsize=12)
plt.ylabel("Giá trị", fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
