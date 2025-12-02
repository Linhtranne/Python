import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], 'b-', linewidth=2, label='y = sin(x)')
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Hoạt hình hàm sin(x)', fontsize=14, fontweight='bold')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y = sin(x)', fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right')
x = np.linspace(0, 2 * np.pi, 200)
def init():
    line.set_data([], [])
    return line,
def update(frame):
    y = np.sin(x + frame / 10)
    line.set_data(x, y)
    return line,
anim = FuncAnimation(fig, update, init_func=init, 
                     frames=200, interval=50, blit=True, repeat=True)
plt.tight_layout()
plt.show()

