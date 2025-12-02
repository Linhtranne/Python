import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)
math_scores = np.random.normal(7.5, 1.2, 100)  # Trung bình 7.5
physical_scores = np.random.normal(6.8, 1.5, 100)     # Trung bình 6.8
chemical_scores = np.random.normal(7.0, 1.3, 100)    # Trung bình 7.0
math_scores = np.clip(math_scores, 0, 10)
physical_scores = np.clip(physical_scores, 0, 10)
chemical_scores = np.clip(chemical_scores, 0, 10)
df = pd.DataFrame({
    'subject': ['Toán']*100 + ['Lý']*100 + ['Hóa']*100,
    'score': np.concatenate([math_scores, physical_scores, chemical_scores])
})
sns.displot(df, x="score", hue="subject", kind="kde", fill=True, alpha=0.3, height=6, aspect=1.5)
plt.title("Phân phối điểm thi theo môn học", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Điểm thi", fontsize=12)
plt.ylabel("Mật độ", fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
print(f"\n{'='*60}")
print("PHÂN TÍCH ĐIỂM THI THEO MÔN HỌC:")
print(f"{'='*60}")

for subject in ['Toán', 'Lý', 'Hóa']:
    subject_scores = df[df['subject'] == subject]['score']
    print(f"\n{subject}:")
    print(f"  - Điểm trung bình: {subject_scores.mean():.2f}")
    print(f"  - Độ lệch chuẩn: {subject_scores.std():.2f}")
    print(f"  - Điểm thấp nhất: {subject_scores.min():.2f}")
    print(f"  - Điểm cao nhất: {subject_scores.max():.2f}")

print(f"\n{'='*60}")
print("NHẬN XÉT:")
print(f"{'='*60}")
toan_mean = df[df['subject'] == 'Toán']['score'].mean()
ly_mean = df[df['subject'] == 'Lý']['score'].mean()
hoa_mean = df[df['subject'] == 'Hóa']['score'].mean()
