import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
day = np.arange(1, 31)
sales = np.random.uniform(100, 300, 30) + np.random.normal(0, 15, 30)  # random + noise

df = pd.DataFrame({"day": day, "sales": sales})


plt.figure(figsize=(7,4))
sns.lineplot(data=df, x="day", y="sales", marker="o")
plt.title("Biến động doanh thu theo ngày")
plt.xlabel("Ngày")
plt.ylabel("Doanh thu")
plt.grid(True)
plt.show()

plt.figure(figsize=(7,4))
sns.regplot(data=df, x="day", y="sales", scatter_kws={"s":40})
plt.title("Hồi quy xu hướng doanh thu (Regplot)")
plt.xlabel("Ngày")
plt.ylabel("Doanh thu")
plt.grid(True)
plt.show()