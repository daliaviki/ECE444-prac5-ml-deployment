import requests
import json

# --- API endpoint ---
BASE_URL = "http://pra5-ml-api-env.eba-mvu2cj2p.us-east-2.elasticbeanstalk.com/predict"

# --- Four sample test cases ---
test_cases = {
    "fake1": "Breaking: The moon is made of cheese and NASA confirms it!",
    "fake2": "Aliens land in Toronto to attend Drake’s concert.",
    "real1": "The Bank of Canada announces interest rate changes this month.",
    "real2": "Toronto Maple Leafs win in overtime against Montreal Canadiens."
}

# --- Run tests ---
for name, text in test_cases.items():
    res = requests.post(BASE_URL, json={"text": text})
    print(f"{name} → {res.status_code} : {res.json()}")
