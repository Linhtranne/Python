import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

class_A = ['A'] * 30
class_B = ['B'] * 30
class_C = ['C'] * 30

score_A = np.random.normal(8.0, 0.8, 30) 
score_B = np.random.normal(7.0, 1.0, 30) 
score_C = np.random.normal(8.5, 0.7, 30) 

score_A = np.clip(score_A, 0, 10)
score_B = np.clip(score_B, 0, 10)
score_C = np.clip(score_C, 0, 10)
df = pd.DataFrame({
    'class': class_A + class_B + class_C,
    'score': np.concatenate([score_A, score_B, score_C])
})

plt.figure(figsize=(10, 6))

sns.barplot(data=df, x='class', y='score', palette='Set2', 
            edgecolor='black', linewidth=1.5, errorbar='sd')

plt.title("So sánh điểm trung bình của các lớp A, B, C", fontsize=14, fontweight='bold')
plt.xlabel("Lớp", fontsize=12)
plt.ylabel("Điểm trung bình", fontsize=12)

plt.grid(True, alpha=0.3, axis='y')

for i, class_name in enumerate(['A', 'B', 'C']):
    mean_score = df[df['class'] == class_name]['score'].mean()
    plt.text(i, mean_score + 0.2, f'{mean_score:.2f}', 
             ha='center', fontsize=11, fontweight='bold', color='darkblue')

plt.tight_layout()
plt.show()
