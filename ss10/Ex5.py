
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

majors = ["CNTT", "Kinh Tế", "Ngôn Ngữ"]
data = {
    "major": np.random.choice(majors, 250),
    "score": np.random.uniform(5, 10, 250)  
}

df = pd.DataFrame(data)


plt.figure(figsize=(7,4))
sns.boxplot(data=df, x="major", y="score")
plt.title("Boxplot phân phối điểm từng nhóm ngành")
plt.show()

### Violinplot
plt.figure(figsize=(7,4))
sns.violinplot(data=df, x="major", y="score")
plt.title("Violinplot phân phối điểm từng nhóm ngành")
plt.show()