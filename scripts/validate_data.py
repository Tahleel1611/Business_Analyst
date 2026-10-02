from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root / "data/interim/transactions.csv")
checks = {"rows": len(df), "duplicate_rows": int(df.duplicated().sum()), "null_customer_ids": int(df.customer_id.isna().sum()), "negative_values": int(((df.quantity < 0) | (df.unit_price < 0)).sum())}
status = "PASS" if all(checks[key] == 0 for key in ["duplicate_rows", "null_customer_ids", "negative_values"]) else "FAIL"
print("DATA QUALITY REPORT")
for key, value in checks.items(): print(f"{key}: {value}")
print(f"validation_status: {status}")
if status == "FAIL": raise SystemExit(1)
