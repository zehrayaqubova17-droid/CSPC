import pandas as pd

cols = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
df = pd.read_csv("/home/zehra/Downloads/heart_uci/processed.cleveland.data",
                 header=None, names=cols, na_values="?")
df["target"] = (df["target"] > 0).astype(int)   # 0 = sağlam, 1 = xəstə
df.to_csv("PW3/heart.csv", index=False)
print(df.shape)
print(df["target"].value_counts())