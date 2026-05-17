import pandas as pd
import matplotlib.pyplot as plt

data = {
    "community": ["North Lawndale", "Austin", "Hyde Park"],
    "clinic_count": [4, 7, 3],
    "diabetes_rate": [14.2, 12.8, 7.4]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df["clinic_count"].corr(df["diabetes_rate"])
print(f"Correlation between clinic count and diabetes rate: {correlation:.2f}")

# Create scatter plot
df.plot(
    kind="scatter",
    x="clinic_count",
    y="diabetes_rate",
    figsize=(8, 5)
)

plt.title("Clinic Count vs Diabetes Rate")
plt.xlabel("Clinic Count")
plt.ylabel("Diabetes Rate (%)")
plt.grid(True)
plt.tight_layout()

plt.savefig("../outputs/clinics_vs_diabetes_scatter.png")
plt.show()