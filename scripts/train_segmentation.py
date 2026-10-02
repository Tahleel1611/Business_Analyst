from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.analytics.core import demo_transactions, rfm
root = Path(__file__).resolve().parents[1]
(root / "artifacts").mkdir(exist_ok=True)
rfm(demo_transactions()).to_csv(root / "artifacts/customer_segments.csv", index=False)
print("Segmentation artifact written")
