import numpy as np
import matplotlib.pyplot as plt

# інтервал від 0 до 15
x = np.linspace(0, 15, 400)

# y = sin(2x) * cos(x) + ln(x+1) - exp(-0.2x)
y = np.sin(2 * x) * np.cos(x) + np.log(x + 1) - np.exp(-0.2 * x)

# графік
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = \sin(2x)\cos(x) + \ln(x+1) - e^{-0.2x}$', color='blue', linewidth=2)

plt.title('Графік складної функції')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()

plt.show()