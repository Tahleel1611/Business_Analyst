from fastapi import FastAPI, Query
from src.analytics.core import demo_transactions, kpis, rfm, monthly_forecast, churn_model

app = FastAPI(title="CommerceIQ API", version="1.0.0")
df = demo_transactions()

@app.get("/health")
def health(): return {"status":"ok", "mode":"demo", "rows":len(df)}
@app.get("/analytics/kpis")
def analytics_kpis(): return kpis(df)
@app.get("/customers/segments")
def segments(): return rfm(df).to_dict(orient="records")
@app.get("/forecasts/demand")
def forecast(periods: int = Query(3, ge=1, le=12)): return monthly_forecast(df, periods)[1].to_dict(orient="records")
@app.get("/customers/churn-risk")
def churn(limit: int = Query(20, ge=1, le=100)): return churn_model(df)["customers"].head(limit).to_dict(orient="records")
