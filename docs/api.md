# API

FastAPI documentation is available at `/docs`.

| Endpoint | Purpose |
|---|---|
| `GET /health` | Service and data-mode check |
| `GET /analytics/kpis` | Revenue, orders, customers, AOV |
| `GET /customers/segments` | RFM customer segments |
| `GET /customers/churn-risk?limit=20` | Ranked inactivity risk |
| `GET /forecasts/demand?periods=3` | Monthly demand baseline |
