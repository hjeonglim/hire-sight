import json
import csv
import os

input_path = "data/raw/20261105_001846_micron_p0_memory_pool_filters.json"

with open(input_path, 'r') as f:
    data = json.load(f)["data"]

os.makedirs("outputs", exist_ok=True)
output_path = "outputs/20261105_001846_micron_p0_memory_pool_filters.csv"
headers = ["id", "job_title", "job_description"]

with open(output_path, "w", newline="") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=headers)
    writer.writeheader()
    for post in data:
        writer.writerow({
            "id": post["id"],
            "job_title": post["job_title"],
            "job_description": post["description"][:2000]
        })
