from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.analytics.core import demo_transactions, churn_model
result = churn_model(demo_transactions())
print({key: value for key, value in result.items() if key != "customers"})
