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

print("Community Health Summary")
print("-" * 40)

for record in communities:
    print(
        f"{record['community']}: "
        f"Population {record['population']:,}," 
        f"Diabetes Rate {record['diabetes_rate']}%"
    )