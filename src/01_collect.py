import json, os, sys, time
from datetime import datetime, timezone
from dotenv import load_dotenv
sys.path.insert(0, ".")

import requests

from config.config import COMPANIES, MODES
from utils import month_ranges

load_dotenv()

company, mode, limit = sys.argv[1], sys.argv[2], int(sys.argv[3])

# 2. Read API key from env var (never hardcode)
# 3. Define balance() -> GET /v0/billing/credit-balance, return used_api_credits
def balance():
    r = requests.get("https://api.theirstack.com/v0/billing/credit-balance", headers=H)
    r.raise_for_status()
    return r.json()["used_api_credits"] 

def search(body, tries=3):
    for i in range(tries):
        try:
            t = time.time()
            r = requests.post(url, json=body, headers=H)
            latency = round(time.time() - t, 2)
            r.raise_for_status()
            return r.json(), r.status_code, latency
        except requests.exceptions.Timeout:
            print(f"timeout, retry {i + 1}/{tries}")
            time.sleep(5)
    raise RuntimeError("search failed after retries")

API_KEY = os.environ["THEIR_STACK_API"]
url = "https://api.theirstack.com/v1/jobs/search"
H = {"Authorization": f"Bearer {API_KEY}"}

for label, gte, lte in month_ranges((2025, 11), (2026, 10)):
    body = {
    "company_id_or": [COMPANIES[company]["id"]],
    "job_country_code_or": ["US"],
    "limit": limit,
    "page": 0,
    "posted_at_gte": gte,
    "posted_at_lte": lte,
    "include_total_results": True,
    **MODES[mode]  
    }
  
    before = balance()
    data, status, latency = search(body)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_path = f"data/raw/{company.lower()}/jobs"
    os.makedirs(output_path, exist_ok=True)
 
    with open(f"{output_path}/{stamp}_{company.lower()}_{mode}_{label}_p{body["page"]}.json", "w") as f_out:
        json.dump(data, f_out, indent=2)

    # Record balance AFTER the call
    after = balance()  

    log = {
        "ts": stamp, "company": company, "body": body, "status": status, "mode": mode, "latency_s": latency,
        "returned": len(data["data"]), "total_results": data["metadata"]["total_results"],
        "credits_used": after - before,
    }
    with open("data/call_log.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")
    print(log)