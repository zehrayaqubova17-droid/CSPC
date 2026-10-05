import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]     # əlavə olunan əsas həcmi (mL)
pH = data[:, 1]

slope = np.gradient(pH, V)      # pH əyrisinin meyli
i = np.argmax(slope)            # ən böyük meylin indeksi
V_eq = V[i]
print("Equivalence point (mL):", V_eq)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(V, pH)
ax1.axvline(V_eq, color="red", linestyle="--", label=f"V_eq = {V_eq:.1f} mL")
ax1.set_xlabel("Volume of base (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration curve")
ax1.legend()

ax2.plot(V, slope)
ax2.axvline(V_eq, color="red", linestyle="--")
ax2.set_xlabel("Volume of base (mL)")
ax2.set_ylabel("dpH/dV")
ax2.set_title("Slope")

plt.tight_layout()
plt.savefig("titration.png", dpi=150)
