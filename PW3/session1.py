import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# 1. Datanı yüklə
df = pd.read_csv("PW3/heart.csv")
print(df.shape)
print(df.head())

cont = df[["age", "chol", "trestbps", "thalach"]]
print(cont.describe())

# 2. Paylanmalar (histoqram)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flat, cont.columns):
    ax.hist(cont[col], bins=20, edgecolor="black")
    ax.set_title(col)
    ax.set_xlabel(col)
    ax.set_ylabel("count")
plt.tight_layout()
plt.savefig("PW3/distributions.png", dpi=150)
plt.close()

# 3. Normallıq: Q-Q plot və Shapiro testi
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flat, cont.columns):
    stats.probplot(cont[col], dist="norm", plot=ax)
    ax.set_title("Q-Q plot: " + col)
plt.tight_layout()
plt.savefig("PW3/qqplots.png", dpi=150)
plt.close()

print("\nNormality tests (Shapiro-Wilk):")
for col in cont.columns:
    W, p = stats.shapiro(cont[col])
    print(col, "W =", round(W, 3), "p =", p, "skew =", round(stats.skew(cont[col]), 2))