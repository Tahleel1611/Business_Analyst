"""Deterministic demo ETL and business analytics."""
from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score

def demo_transactions(n_customers: int = 80, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")
    rows = []
    for i in range(n_customers):
        cid = f"C{i+1:04d}"
        for _ in range(int(rng.poisson(3) + 1)):
            date = rng.choice(dates)
            qty = int(rng.integers(1, 4)); price = round(float(rng.uniform(12, 180)), 2)
            rows.append([f"O{len(rows)+1:06d}", cid, date, f"P{rng.integers(1, 26):03d}",
                         rng.choice(["Electronics", "Home", "Beauty", "Sports"]), qty, price,
                         rng.choice(["North", "South", "East", "West"])])
    return pd.DataFrame(rows, columns=["order_id","customer_id","order_date","product_id","category","quantity","unit_price","region"]).assign(order_value=lambda x: x.quantity*x.unit_price)

def kpis(df):
    return {"revenue": round(float(df.order_value.sum()), 2), "orders": int(df.order_id.nunique()),
            "customers": int(df.customer_id.nunique()), "aov": round(float(df.groupby("order_id").order_value.sum().mean()), 2)}

def rfm(df: pd.DataFrame) -> pd.DataFrame:
    ref = df.order_date.max() + pd.Timedelta(days=1)
    out = df.groupby("customer_id").agg(recency=("order_date", lambda s: (ref-s.max()).days), frequency=("order_id","nunique"), monetary=("order_value","sum")).reset_index()
    for col in ["recency", "frequency", "monetary"]:
        out[col+"_score"] = pd.qcut(out[col].rank(method="first"), 4, labels=[1,2,3,4]).astype(int)
    out["segment"] = np.select([out.recency_score>=4, (out.frequency_score>=3)&(out.monetary_score>=3), out.recency_score<=1], ["Champions","Loyal Customers","At Risk"], default="Potential Loyalists")
    return out

def cohorts(df):
    x = df.assign(month=df.order_date.dt.to_period("M"), cohort_month=df.groupby("customer_id").order_date.transform("min").dt.to_period("M"))
    x["period"] = (x["month"] - x["cohort_month"]).apply(lambda z: z.n)
    return x.groupby(["cohort_month","period"]).customer_id.nunique().reset_index(name="customers")

def monthly_forecast(df, periods=3):
    monthly = df.set_index("order_date").resample("MS").order_value.sum().rename("actual").reset_index()
    trend = float(monthly.actual.tail(3).mean()) if len(monthly) else 0
    future = pd.DataFrame({"order_date": pd.date_range(monthly.order_date.max()+pd.offsets.MonthBegin(), periods=periods, freq="MS"), "forecast": trend})
    return monthly, future

def churn_model(df):
    features = rfm(df)
    threshold = features.recency.median()
    features["inactive"] = (features.recency > threshold).astype(int)
    X = features[["recency","frequency","monetary"]]; y = features.inactive
    model = LogisticRegression(max_iter=500).fit(X, y)
    pred = model.predict(X); prob = model.predict_proba(X)[:,1]
    return {"f1": float(f1_score(y,pred,zero_division=0)), "roc_auc": float(roc_auc_score(y,prob)) if y.nunique()>1 else None, "customers": features.assign(churn_risk=prob).sort_values("churn_risk", ascending=False)}
