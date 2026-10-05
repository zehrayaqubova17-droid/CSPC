import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 16.0   # skeleton-da fərqli K varsa, onu yazın


def k_imbalance(x):
    """Tarazlıqda sıfır olan ifadə: (2x)^2 / ((1-x)(1-x)) - K"""
    return (2 * x) ** 2 / ((1 - x) * (1 - x)) - K


# 1) Newton (kök tapma)
x_newton = newton(k_imbalance, x0=0.5)

# 2) SLSQP: k_imbalance^2-ni minimallaşdır
res = minimize(lambda p: k_imbalance(p[0]) ** 2, x0=[0.5],
               method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]

print("x (Newton):", x_newton)
print("x (SLSQP): ", x_slsqp)

x_eq = x_newton
print("Equilibrium amounts (mol):")
print("  H2 =", 1 - x_eq)
print("  I2 =", 1 - x_eq)
print("  HI =", 2 * x_eq)

# qrafik
x = np.linspace(0, 1, 200)
plt.figure()
plt.plot(x, 1 - x, label="H2")
plt.plot(x, 1 - x, "--", label="I2")
plt.plot(x, 2 * x, label="HI")
plt.axvline(x_eq, color="gray", linestyle=":", label=f"equilibrium x = {x_eq:.3f}")
plt.xlabel("Extent x")
plt.ylabel("Amount (mol)")
plt.legend()
plt.savefig("equilibrium.png", dpi=150)
