"""Normalize the UCI Online Retail workbook into the project transaction schema."""
from pathlib import Path
import sys
import pandas as pd

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
source = root / "data/raw/online-retail/Online Retail.xlsx"
if not source.exists():
    raise FileNotFoundError("Download the UCI workbook into data/raw/online-retail first")
raw = pd.read_excel(source)
raw = raw.dropna(subset=["CustomerID", "InvoiceDate"])
raw = raw[raw["Quantity"] > 0]
raw = raw[raw["UnitPrice"] >= 0]
out = pd.DataFrame({
    "order_id": raw["InvoiceNo"].astype(str),
    "customer_id": "C" + raw["CustomerID"].astype(int).astype(str),
    "order_date": pd.to_datetime(raw["InvoiceDate"]),
    "product_id": raw["StockCode"].astype(str),
    "category": raw["Description"].fillna("Unknown").astype(str).str[:80],
    "quantity": raw["Quantity"].astype(int),
    "unit_price": raw["UnitPrice"].astype(float),
    "region": raw["Country"].fillna("Unknown").astype(str),
})
out["order_value"] = out["quantity"] * out["unit_price"]
target = root / "data/processed/uci_transactions.csv"
target.parent.mkdir(parents=True, exist_ok=True)
out.to_csv(target, index=False)
print(f"Wrote {len(out):,} rows to {target}")
