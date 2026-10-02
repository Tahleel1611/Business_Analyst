-- CTE, CASE, window function, rolling revenue, and ranking
WITH monthly AS (SELECT date_trunc('month', order_date) month, SUM(order_value) revenue FROM fact_orders GROUP BY 1), ranked AS (SELECT *, revenue - LAG(revenue) OVER (ORDER BY month) growth, SUM(revenue) OVER (ORDER BY month) running_revenue, RANK() OVER (ORDER BY revenue DESC) revenue_rank FROM monthly)
SELECT month, revenue, growth, running_revenue, CASE WHEN revenue > 0 THEN growth / revenue END growth_rate, revenue_rank FROM ranked ORDER BY month;
