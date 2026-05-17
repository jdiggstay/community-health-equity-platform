import pandas as pd

df = pd.read_csv("../outputs/community_health.csv")

# Create risk level
df["risk_level"] = df["diabetes_rate"].apply(
    lambda rate: "High Risk" if rate >= 12 else "Moderate Risk"
)

# Group and summarize
summary = df.groupby("risk_level").agg({
    "community": "count",
    "population": "sum",
    "diabetes_rate": "mean"
})

# Rename columns
summary = summary.rename(columns={
    "community": "community_count",
    "population": "total_population",
    "diabetes_rate": "average_diabetes_rate"
})

print("Community Summary by Risk Level")
print(summary)