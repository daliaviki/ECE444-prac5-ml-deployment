import requests
import csv
import time
from statistics import mean

BASE_URL = "http://pra5-ml-api-env.eba-mvu2cj2p.us-east-2.elasticbeanstalk.com/predict"

test_cases = {
    "fake1": "Breaking: The moon is made of cheese and NASA confirms it!",
    "fake2": "Aliens land in Toronto to attend Drake’s concert.",
    "real1": "The Bank of Canada announces interest rate changes this month.",
    "real2": "Toronto Maple Leafs win in overtime against Montreal Canadiens."
}

N_CALLS = 100

for name, text in test_cases.items():
    filename = f"latency_{name}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["call_number", "latency_seconds"])

        latencies = []
        for i in range(N_CALLS):
            start = time.time()
            res = requests.post(BASE_URL, json={"text": text})
            end = time.time()
            latency = end - start
            latencies.append(latency)
            writer.writerow([i + 1, latency])
            print(f"{name} #{i+1}: {latency:.3f}s")

    print(f"{name} average latency: {mean(latencies):.3f}s")
