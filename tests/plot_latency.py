import pandas as pd
import matplotlib.pyplot as plt
import glob

csv_files = glob.glob("latency_*.csv")

data = {}
for file in csv_files:
    label = file.replace("latency_", "").replace(".csv", "")
    df = pd.read_csv(file)
    data[label] = df["latency_seconds"]

plt.figure(figsize=(8,6))
plt.boxplot(data.values(), labels=data.keys())
plt.title("API Latency per Test Case (100 calls each)")
plt.ylabel("Latency (seconds)")
plt.grid(True)
plt.tight_layout()
plt.savefig("latency_boxplot.png")
plt.show()

# Print averages
for k, v in data.items():
    print(f"{k} average latency: {v.mean():.4f}s")
