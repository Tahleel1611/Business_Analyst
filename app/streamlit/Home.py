import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st
import plotly.express as px
from src.analytics.core import demo_transactions, kpis, rfm, cohorts, monthly_forecast, churn_model

st.set_page_config(page_title="CommerceIQ", page_icon="📈", layout="wide")
df = demo_transactions(); st.title("CommerceIQ"); st.caption("E-Commerce Customer Intelligence Platform · DEMO DATA")
cards = kpis(df); cols = st.columns(4)
for c, (label, value) in zip(cols, [("Revenue", f"${cards['revenue']:,.0f}"),("Orders",cards["orders"]),("Customers",cards["customers"]),("Average order",f"${cards['aov']:,.2f}")]): c.metric(label, value)
tab1, tab2, tab3, tab4 = st.tabs(["Sales", "Customers", "Retention", "Forecast"])
with tab1:
    st.plotly_chart(px.line(df.groupby(df.order_date.dt.to_period("M")).order_value.sum().reset_index().assign(order_date=lambda x:x.order_date.astype(str)), x="order_date", y="order_value", title="Monthly revenue"), use_container_width=True)
with tab2:
    seg = rfm(df); st.plotly_chart(px.scatter(seg, x="frequency", y="monetary", color="segment", hover_name="customer_id", title="Customer segments"), use_container_width=True); st.dataframe(seg, use_container_width=True)
with tab3:
    st.plotly_chart(px.density_heatmap(cohorts(df), x="period", y="first", z="customers", title="Cohort customers"), use_container_width=True)
with tab4:
    actual, future = monthly_forecast(df); st.plotly_chart(px.line(actual, x="order_date", y="actual", title="Demand history"), use_container_width=True); st.dataframe(future)
st.sidebar.info("Run `python scripts/run_pipeline.py` to materialize CSV artifacts.")
