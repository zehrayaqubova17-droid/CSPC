import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("PW3/chemicals_cancer.csv")
print(df.shape)
print(df.columns.tolist())
print(df.describe().round(2))

def find(keyword):
    return [c for c in df.columns if keyword in c.lower()][0]

benz = find("benz")
cad = find("cad")
pol = find("pollut")
mal = find("malig")
print("\nİstifadə olunan sütunlar:", benz, cad, pol, mal)

# ---------- ADDIM 6: naiv təhlil ----------
print("\n=== ADDIM 6: naiv ===")
for chem in [benz, cad]:
    r, p = stats.pearsonr(df[chem], df[mal])
    print(chem, "vs malignancy: r =", round(r, 3), " p =", p)

print("\nKorrelyasiya matrisi:")
print(df.corr().round(2))

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, chem in zip(axes, [benz, cad]):
    ax.scatter(df[chem], df[mal], alpha=0.4)
    ax.set_xlabel(chem)
    ax.set_ylabel(mal)
    ax.set_title(chem + " (all patients)")
plt.tight_layout()
plt.savefig("PW3/chem_naive.png", dpi=150)
plt.close()

# ---------- ADDIM 7: üçüncü dəyişəni sabit tut ----------
print("\n=== ADDIM 7: pollution sabit ===")
med = df[pol].median()
sub = df[(df[pol] > med - 5) & (df[pol] < med + 5)]
print("pollution median =", round(med, 1), " subset size =", len(sub))

for chem in [benz, cad]:
    r_all, _ = stats.pearsonr(df[chem], df[mal])
    r_sub, p_sub = stats.pearsonr(sub[chem], sub[mal])
    print(chem, ": all r =", round(r_all, 3), "| restricted r =", round(r_sub, 3), " p =", p_sub)

# əlavə yoxlama: pollution-un təsirini xətti çıxarıb qalıq (residual) korrelyasiyası
print("\nPartial correlation (pollution çıxarılıb):")
def resid(y, x):
    a, b = np.polyfit(x, y, 1)
    return y - (a * x + b)
for chem in [benz, cad]:
    r_part, p_part = stats.pearsonr(resid(df[chem], df[pol]), resid(df[mal], df[pol]))
    print(chem, ": partial r =", round(r_part, 3), " p =", p_part)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, chem in zip(axes, [benz, cad]):
    ax.scatter(sub[chem], sub[mal], alpha=0.5)
    ax.set_xlabel(chem)
    ax.set_ylabel(mal)
    ax.set_title(chem + " (pollution ≈ " + str(round(med)) + ")")
plt.tight_layout()
plt.savefig("PW3/chem_restricted.png", dpi=150)
plt.close()