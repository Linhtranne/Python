import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y = sin(x)', color='orange', linewidth=2)
plt.title("Đồ thị hàm số sin(x)", fontsize=14, fontweight='bold')
plt.xlabel("Giá trị x", fontsize=12)
plt.ylabel("Giá trị sin(x) ", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.scatter(np.pi/2, 1, color='red')
plt.text(np.pi/2, 1.1, 'Điểm cực đại (π/2, 1)', fontsize=10, ha='center')
plt.legend()
plt.show()