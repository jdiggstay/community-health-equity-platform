import pandas as pd

df = pd.read_csv("../outputs/community_health.csv")

# Sort by diabetes rate descending
df = df.sort_values("diabetes_rate", ascending=False)

# Create ranking
df["risk_rank"] = range(1, len(df) + 1)

print("Community Risk Ranking")
print(df)
