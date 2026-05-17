import pandas as pd

data = {
    "community": ["North Lawndale", "Austin", "Hyde Park"],
    "population": [34700, 95000, 29000],
    "diabetes_rate": [14.2, 12.8, 7.4]
}

df = pd.DataFrame(data)

print("Community Health Data")
print(df)

print("\nSummary Statistics")
print(df.describe())

print("\nHigh-Risk Communities (Diabetes Rate >= 12%)")
print(df[df["diabetes_rate"] >= 12])