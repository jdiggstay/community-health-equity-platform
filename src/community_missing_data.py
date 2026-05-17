import pandas as pd

data = {
    "community": ["North Lawndale", "Austin", "Hyde Park"],
    "diabetes_rate": [14.2, None, 7.4],
    "clinic_count": [4, 7, None]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("\nMissing Values by Column")
print(df.isnull().sum())

df["diabetes_rate"] = df["diabetes_rate"].fillna(
    df["diabetes_rate"].mean()
)

df["clinic_count"] = df["clinic_count"].fillna(
    df["clinic_count"].mean()
)

print("\nCleaned Data")
print(df)