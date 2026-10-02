from pathlib import Path
import sys
import json
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.analytics.core import demo_transactions, kpis, rfm, cohorts, monthly_forecast, churn_model

root = Path(__file__).resolve().parents[1]
(root/"data/sample").mkdir(parents=True, exist_ok=True); (root/"artifacts").mkdir(exist_ok=True)
df = demo_transactions(); df.to_csv(root/"data/sample/transactions.csv", index=False)
rfm(df).to_csv(root/"artifacts/customer_segments.csv", index=False)
cohorts(df).to_csv(root/"artifacts/cohorts.csv", index=False)
monthly, future = monthly_forecast(df); monthly.to_csv(root/"artifacts/monthly_sales.csv", index=False); future.to_csv(root/"artifacts/forecast.csv", index=False)
metrics = {"kpis": kpis(df), "churn": {k:v for k,v in churn_model(df).items() if k != "customers"}, "rows": len(df)}
(root/"artifacts/metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
print(json.dumps(metrics, indent=2))
