import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42) 

n_students = 500

hours = np.random.uniform(1, 10, n_students)
noise = np.random.normal(0, 1.5, n_students) 
raw_score = hours * 1.5 + noise           
score = np.clip(raw_score, 0, 10)         

majors = np.random.choice(["A", "B", "C"], n_students)

df = pd.DataFrame({
    "hours": hours,
    "score": score,
    "major": majors
})

sns.set(style="whitegrid")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(df["score"], kde=True, bins=20, ax=axes[0])
axes[0].set_title("Phân phối điểm (Histplot)")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Frequency")

sns.scatterplot(data=df, x="hours", y="score", hue="major", alpha=0.7, ax=axes[1])
axes[1].set_title("Quan hệ giữa giờ học và điểm (Scatterplot)")
axes[1].set_xlabel("Hours")
axes[1].set_ylabel("Score")

sns.boxplot(data=df, x="major", y="score", ax=axes[2])
axes[2].set_title("Phân phối điểm theo ngành (Boxplot)")
axes[2].set_xlabel("Major")
axes[2].set_ylabel("Score")

plt.tight_layout()
plt.show()