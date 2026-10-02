from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
from src.analytics.core import rfm, cohorts

root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root / "data/interim/transactions.csv", parse_dates=["order_date"])
out = root / "data/processed"
out.mkdir(parents=True, exist_ok=True)
rfm(df).to_csv(out / "customer_features.csv", index=False)
cohorts(df).to_csv(out / "cohort_features.csv", index=False)
print("Feature tables written to data/processed")
