# Methodology

The pipeline creates a reproducible transaction table, validates positive quantities and prices, then produces business KPIs, RFM scores, cohort retention counts, a trailing-average demand baseline, and a logistic-regression inactivity model. The demo uses a median-recency inactivity label to keep the example deterministic; production work should define the label against a forward observation window and use a time-based split to prevent leakage.

RFM segments are quantile-based and interpretable. Correlation is not causation. Forecasts are a baseline, not an inventory commitment. All demo values are synthetic.
