import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# datanı oxu (ilk sətir başlıqdır)
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]          # başlanğıc qatılıq = ilk ölçü


def error(k):
    """Model ilə ölçmələr arasındakı kvadratik xətaların cəmi."""
    return np.sum((C - C0 * np.exp(-k * t)) ** 2)


res = minimize(lambda p: error(p[0]), x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print("Fitted k:", k_fit)

# qrafik
t_smooth = np.linspace(t.min(), t.max(), 200)
plt.figure()
plt.plot(t, C, "o", label="data")
plt.plot(t_smooth, C0 * np.exp(-k_fit * t_smooth), "-", label=f"fit, k = {k_fit:.3f}")
plt.xlabel("Time t")
plt.ylabel("Concentration C")
plt.legend()
plt.savefig("kinetics.png", dpi=150)
