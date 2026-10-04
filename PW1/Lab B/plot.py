import numpy as np
import matplotlib
matplotlib.use("Agg")          # pəncərə açmadan faylı birbaşa yazır
import matplotlib.pyplot as plt

LAMBDA = 0.3

# 1. Məlumatı oxu (başlıq sətrini keç)
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# 2. N0 = ilk müşahidə, analitik qanun
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# 3. 1x2 subplot, ortaq oxlarla
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

ax1.scatter(t, observed)
ax1.set_title("Observed data")
ax1.set_xlabel("time")
ax1.set_ylabel("count")

ax2.plot(t, analytical)
ax2.set_title(r"Analytical law $N_0 e^{-\lambda t}$")
ax2.set_xlabel("time")
ax2.set_ylabel("count")

fig.tight_layout()

# 4. Saxla
fig.savefig("figure.png", dpi=150)
