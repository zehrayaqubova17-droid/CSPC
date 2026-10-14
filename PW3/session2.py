import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("PW3/heart.csv")

# ---------- ADDIM 4: xəstə vs sağlam, thalach ----------
disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]
print("=== ADDIM 4 ===")
print("n (disease, healthy):", len(disease), len(healthy))
print("mean (disease, healthy):", round(disease.mean(), 2), round(healthy.mean(), 2))

u, p_mw = stats.mannwhitneyu(disease, healthy, alternative="two-sided")
print("Mann-Whitney U =", u, " p =", p_mw)

t, p_t = stats.ttest_ind(disease, healthy, equal_var=False)
print("Welch t =", round(t, 2), " p =", p_t)

# orta + qeyri-müəyyənlik
means = [disease.mean(), healthy.mean()]
sems = [disease.sem(), healthy.sem()]
cis = [1.96 * s for s in sems]
print("SEM (disease, healthy):", [round(s, 2) for s in sems])
print("95% CI half-width:", [round(c, 2) for c in cis])

plt.figure(figsize=(5, 5))
plt.errorbar(["disease", "healthy"], means, yerr=cis, fmt="o", capsize=8, markersize=8)
plt.ylabel("mean thalach (95% CI)")
plt.title("Max heart rate by group")
plt.savefig("PW3/thalach_means.png", dpi=150)
plt.close()

# ---------- ADDIM 5: age vs thalach ----------
print("\n=== ADDIM 5 ===")
r, p_r = stats.pearsonr(df["age"], df["thalach"])
rho, p_s = stats.spearmanr(df["age"], df["thalach"])
print("Pearson r =", round(r, 3), " p =", p_r)
print("Spearman rho =", round(rho, 3), " p =", p_s)

slope, intercept = np.polyfit(df["age"], df["thalach"], 1)
x = np.linspace(df["age"].min(), df["age"].max(), 100)
plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.plot(x, slope * x + intercept, color="red")
plt.xlabel("age")
plt.ylabel("thalach")
plt.savefig("PW3/age_vs_thalach.png", dpi=150)
plt.close()

# ---------- BONUS: target nə qədər balanslıdır ----------
print("\n=== BONUS ===")
pr = df["target"].value_counts(normalize=True)
print(pr)
entropy = -(pr * np.log2(pr)).sum()
gini = 1 - (pr ** 2).sum()
print("entropy (bits) =", round(entropy, 3), " gini =", round(gini, 3))