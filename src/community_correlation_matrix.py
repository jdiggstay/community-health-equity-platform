import pandas as pd
import matplotlib.pyplot as plt

data = {
    "population": [34700, 95000, 29000],
    "diabetes_rate": [14.2, 12.8, 7.4],
    "clinic_count": [4, 7, 3],
    "pharmacy_count": [6, 10, 5]
}

df = pd.DataFrame(data)

# Calculate correlation matrix
corr = df.corr()
print("Correlation Matrix")
print(corr)

# Create heatmap
plt.figure(figsize=(6, 5))
plt.imshow(corr, aspect="auto")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Community Correlation Matrix")
plt.tight_layout()

plt.savefig("../outputs/community_correlation_matrix.png")
plt.show()