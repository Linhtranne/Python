import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(7, 1.5, 200)
data = np.clip(data, 0, 10)
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=20, kde=True, color='skyblue', edgecolor='black')
sns.kdeplot(data, color='red', linewidth=2, label='Đường mật độ')
plt.title("Phân phối điểm thi của 200 học sinh", fontsize=14, fontweight='bold'
          )
plt.xlabel("Điểm thi", fontsize=12)
plt.ylabel("Tần suất", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.show()
mean_score = np.mean(data)
std_score = np.std(data)
median_score = np.median(data)

print(f"\n{'='*50}")
print("NHẬN XÉT VỀ PHÂN PHỐI ĐIỂM THI:")
print(f"{'='*50}")
print(f"Điểm trung bình: {mean_score:.2f}")
print(f"Độ lệch chuẩn: {std_score:.2f}")
print(f"Điểm trung vị: {median_score:.2f}")
print(f"Điểm thấp nhất: {np.min(data):.2f}")
print(f"Điểm cao nhất: {np.max(data):.2f}")
