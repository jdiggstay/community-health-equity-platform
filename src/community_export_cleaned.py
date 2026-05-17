import pandas as pd

data = {
    "community": ["North Lawndale", "Austin", "Hyde Park"],
    "diabetes_rate": [14.2, None, 7.4],
    "clinic_count": [4, 7, None]
}

df = pd.DataFrame(data)

# Fill missing values
df["diabetes_rate"] = df["diabetes_rate"].fillna(
    df["diabetes_rate"].mean()
)
df["clinic_count"] = df["clinic_count"].fillna(
    df["clinic_count"].mean()
)

# Export cleaned data
df.to_csv("../outputs/community_cleaned.csv", index=False)

print("Cleaned community data exported successfully.")