from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.analytics.core import demo_transactions, monthly_forecast
root = Path(__file__).resolve().parents[1]
(root / "artifacts").mkdir(exist_ok=True)
_, future = monthly_forecast(demo_transactions(), 3)
future.to_csv(root / "artifacts/forecast.csv", index=False)
print("Forecast artifact written")
