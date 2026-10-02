# Power BI deliverable

Power BI-ready exports are available in this folder. In Power BI Desktop, use **Get data → Text/CSV** and import:

1. `data/sample/transactions.csv` as `FactOrders`
2. `powerbi/exports/customer_features.csv` as `CustomerFeatures`
3. `powerbi/exports/cohort_features.csv` as `Cohorts`
4. `powerbi/exports/monthly_sales.csv` as `MonthlySales`
5. `powerbi/exports/forecast.csv` as `Forecast`

Create relationships from `FactOrders[customer_id]` to `CustomerFeatures[customer_id]`. Suggested report pages are Executive Overview, Customer Segmentation, Retention Cohorts, and Demand Forecast.

Suggested measures:

```DAX
Revenue = SUM(FactOrders[order_value])
Orders = DISTINCTCOUNT(FactOrders[order_id])
Customers = DISTINCTCOUNT(FactOrders[customer_id])
AOV = DIVIDE([Revenue], [Orders])
Units = SUM(FactOrders[quantity])
Repeat Customer Rate = DIVIDE(COUNTROWS(FILTER(CustomerFeatures, CustomerFeatures[frequency] > 1)), [Customers])
```

The exported files are generated from the verified demo pipeline. A native `.pbix` file is not included because Power BI Desktop’s window is not currently exposed to the automation bridge; the report can be assembled directly from these ready-to-import files.
