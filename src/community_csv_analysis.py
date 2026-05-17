import pandas as pd

df = pd.read_csv("../outputs/community_health.csv")

print("Community Health Data")
print(df)

print("\nSummary Statistics")
print(df.describe())

print("\nHigh-Risk Communities (Diabetes Rate >= 12%)")
print(df[df["diabetes_rate"] >= 12])

print("\nAverage Diabetes Rate")
print(df["diabetes_rate"].mean())