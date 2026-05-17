import pandas as pd

health_data = pd.read_csv("../outputs/community_health.csv")

resources = pd.DataFrame({
    "community": ["North Lawndale", "Austin", "Hyde Park"],
    "clinic_count": [4, 7, 3],
    "pharmacy_count": [6, 10, 5]
})

merged = pd.merge(health_data, resources, on="community")

print("Community Health and Resource Data")
print(merged)