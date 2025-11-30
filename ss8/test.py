from pathlib import Path
from datetime import datetime
import json
import pandas as pd

log_dir = Path("logs")

records = []

for path in log_dir.glob("log_*.json"):
    date_str = path.stem.split("_", maxsplit=1)[1]  
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f) 


    for entry in data:
        entry["date"] = date_obj
        records.append(entry)

df = pd.DataFrame(records)

daily = (
    df.groupby("date")["duration"]
      .sum()
      .reset_index()
      .rename(columns={"duration": "total_duration"})
)

daily.to_csv("daily_report.csv", index=False)
print("✔ Done! File daily_report.csv đã được tạo:")
print(daily)