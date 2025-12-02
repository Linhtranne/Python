import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

months = np.tile(np.arange(1, 13), 3)        
categories = np.repeat(["Shoes", "Clothes", "Bags"], 12)

base = months * 10
noise = np.random.normal(0, 15, len(months))

revenue = base + noise

df = pd.DataFrame({
    "month": months,
    "revenue": revenue,
    "category": categories
})

sns.set(style="whitegrid")

plt.figure(figsize=(7, 4))
sns.lineplot(data=df, x="month", y="revenue", hue="category", marker="o")
plt.title("Doanh thu theo tháng theo từng nhóm sản phẩm (Lineplot)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(range(1, 13))
plt.show()

plt.figure(figsize=(7, 4))
sns.violinplot(data=df, x="category", y="revenue")
plt.title("Phân phối doanh thu theo nhóm sản phẩm (Violinplot)")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

plt.figure(figsize=(7, 4))
sns.regplot(data=df, x="month", y="revenue")
plt.title("Xu hướng doanh thu chung theo tháng (Regplot)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(range(1, 13))
plt.show()