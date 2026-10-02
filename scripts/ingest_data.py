from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.analytics.core import demo_transactions

root = Path(__file__).resolve().parents[1]
source = root / "data/raw/transactions.csv"
out = root / "data/interim/transactions.csv"
out.parent.mkdir(parents=True, exist_ok=True)
if source.exists():
    out.write_bytes(source.read_bytes())
else:
    demo_transactions().to_csv(out, index=False)
print(f"Ingested data at {out}")
