import numpy as np
from scipy.optimize import newton, minimize


def gradient_descent(fprime, x0, alpha, n=200):
    """Əl ilə qradient eniş: hər addımda meylin əksi istiqamətində irəlilə."""
    x = x0
    for _ in range(n):
        x = x - alpha * fprime(x)
    return x


# ---------- 2A: asan konveks funksiya ----------
f = lambda x: (x - 3) ** 2 + 1
fp = lambda x: 2 * (x - 3)      # f'(x)
fpp = lambda x: 2.0             # f''(x)

print("=== 2A: f(x) = (x-3)^2 + 1, x0 = 0 ===")
print("Gradient descent:", gradient_descent(fp, 0, alpha=0.1))
print("Newton:          ", newton(fp, 0, fprime=fpp))
print("SLSQP:           ", minimize(lambda p: f(p[0]), [0], method="SLSQP").x[0])

# ---------- 2B: çətin landşaft ----------
g = lambda x: x**4 - 3 * x**2 + x + 5
gp = lambda x: 4 * x**3 - 6 * x + 1     # g'(x)
gpp = lambda x: 12 * x**2 - 6           # g''(x)

for x0 in (0, 2):
    print(f"\n=== 2B: g(x) = x^4 - 3x^2 + x + 5, x0 = {x0} ===")

    x_gd = gradient_descent(gp, x0, alpha=0.05)
    print("Gradient descent:", x_gd, " g =", g(x_gd))

    x_nw = newton(gp, x0, fprime=gpp)
    kind = "MINIMUM" if gpp(x_nw) > 0 else "MAXIMUM"
    print("Newton:          ", x_nw, " g'' =", gpp(x_nw), "->", kind)

    x_sl = minimize(lambda p: g(p[0]), [x0], method="SLSQP").x[0]
    print("SLSQP:           ", x_sl, " g =", g(x_sl))