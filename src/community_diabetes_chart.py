import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../outputs/community_health.csv")

df.plot(
    kind="bar",
    x="community",
    y="diabetes_rate",
    legend=False
)

plt.title("Community Diabetes Rates")
plt.ylabel("Diabetes Rate (%)")
plt.tight_layout()

plt.savefig("../outputs/community_diabetes_chart.png")
plt.show()