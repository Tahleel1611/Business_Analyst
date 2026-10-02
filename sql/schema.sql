CREATE TABLE IF NOT EXISTS fact_orders (order_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL, order_date DATE NOT NULL, product_id TEXT NOT NULL, category TEXT NOT NULL, quantity INTEGER CHECK (quantity > 0), unit_price NUMERIC(12,2) CHECK (unit_price >= 0), region TEXT, order_value NUMERIC(14,2));
CREATE INDEX IF NOT EXISTS idx_fact_orders_date ON fact_orders(order_date);
CREATE INDEX IF NOT EXISTS idx_fact_orders_customer ON fact_orders(customer_id);
