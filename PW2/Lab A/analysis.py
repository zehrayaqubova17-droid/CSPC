
import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt

# ---------- Part 2: datanı oxu, sürət və təcil ----------
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)   # sürət = mövqenin törəməsi
a = np.gradient(v, t)   # təcil = sürətin törəməsi

print("Mean acceleration:", a.mean())

# ---------- Part 3: səs-küy ----------
print("Std of acceleration:", a.std())

# ---------- Part 4: inteqrasiya ilə geri qayıtmaq ----------
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y_rec - y))
print("Max position difference:", max_diff)

# ---------- Part 5: üç panelli qrafik ----------
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 9))

ax1.plot(t, y)
ax1.set_ylabel("Position y (m)")

ax2.plot(t, v)
ax2.set_ylabel("Velocity v (m/s)")

ax3.plot(t, a)
ax3.axhline(-9.81, color="red", linestyle="--", label="-9.81 m/s²")
ax3.set_ylabel("Acceleration a (m/s²)")
ax3.set_xlabel("Time t (s)")
ax3.legend()

plt.tight_layout()
plt.savefig("motion.png", dpi=150)

# ---------- Bonus: 2D trayektoriya ----------
d2 = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
tt, x2, y2 = d2[:, 0], d2[:, 1], d2[:, 2]

vx = np.gradient(x2, tt)
vy = np.gradient(y2, tt)
speed = np.sqrt(vx**2 + vy**2)

plt.figure()
plt.plot(x2, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Path")
plt.savefig("path.png", dpi=150)

plt.figure()
plt.plot(tt, speed)
plt.xlabel("Time t (s)")
plt.ylabel("Speed")
plt.title("Speed over time")
plt.savefig("speed.png", dpi=150)