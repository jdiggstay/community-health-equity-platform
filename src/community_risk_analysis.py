import pandas as pd

df = pd.read_csv("../outputs/community_health.csv")

# Create calculated columns
df["high_risk"] = df["diabetes_rate"] >= 12
df["risk_level"] = df["diabetes_rate"].apply(
    lambda rate: "High Risk" if rate >= 12 else "Moderate Risk"
)

print("Community Risk Analysis")
print(df)

print("\nHigh-Risk Communities")
print(df[df["high_risk"]])

print("\nNumber of High-Risk Communities")
print(df["high_risk"].sum())