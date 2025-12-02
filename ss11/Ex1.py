import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = x**2 + 2*x
plt.plot(x, y, label='y = x² + 2x', color='blue')
plt.title("Biểu đồ đầu tay của Linh", fontsize=14, fontweight='bold')
plt.xlabel("Trục x", fontsize=12)
plt.ylabel("Trục y", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

