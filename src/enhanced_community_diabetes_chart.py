import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../outputs/community_health.csv")

df.plot(
    kind="bar",
    x="community",
    y="diabetes_rate",
    legend=False,
    figsize=(8, 5)
)

plt.title("Community Diabetes Rates")
plt.ylabel("Diabetes Rate (%)")
plt.xlabel("Community")
plt.grid(axis="y")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("../outputs/enhanced_community_diabetes_chart.png")
plt.show()