import csv

communities = [
    {
        "community": "North Lawndale",
        "population": 34700,
        "diabetes_rate": 14.2
    },
    {
        "community": "Austin",
        "population": 95000,
        "diabetes_rate": 12.8
    },
    {
        "community": "Hyde Park",
        "population": 29000,
        "diabetes_rate": 7.4
    }
]

with open("../outputs/community_health.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["community", "population", "diabetes_rate"]
    )
    writer.writeheader()
    writer.writerows(communities)

print("Community health data exported successfully.")