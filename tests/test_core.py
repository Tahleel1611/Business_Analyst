from src.analytics.core import demo_transactions, kpis, rfm, cohorts, monthly_forecast

def test_demo_data_is_valid():
    df = demo_transactions(); assert len(df) > 0; assert (df.order_value >= 0).all()
def test_kpis_and_rfm():
    df = demo_transactions(); assert kpis(df)["orders"] > 0; assert {"Champions","At Risk"}.intersection(set(rfm(df).segment))
def test_cohort_and_forecast():
    df = demo_transactions(); assert len(cohorts(df)) > 0; assert len(monthly_forecast(df, 2)[1]) == 2
