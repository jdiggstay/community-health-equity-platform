import pandas as pd
import matplotlib.pyplot as plt

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "diabetes_rate": [14.2, 14.0, 13.8, 13.6, 13.4, 13.1]
}

df = pd.DataFrame(data)

df.plot(
    kind="line",
    x="month",
    y="diabetes_rate",
    marker="o",
    figsize=(8, 5)
)

plt.title("Community Diabetes Rate Trend")
plt.ylabel("Diabetes Rate (%)")
plt.xlabel("Month")
plt.grid(True)
plt.tight_layout()

plt.savefig("../outputs/community_diabetes_trend.png")
plt.show()