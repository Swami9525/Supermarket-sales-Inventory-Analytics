CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(150),
    category VARCHAR(100),
    selling_price NUMERIC(10,2),
    cost_price NUMERIC(10,2),
    supplier VARCHAR(150),
    reorder_level INTEGER
);

CREATE TABLE IF NOT EXISTS sales (
    sales_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bill_number VARCHAR(30),
    sale_date DATE,
    product_id VARCHAR(20) REFERENCES products(product_id),
    quantity INTEGER,
    discount NUMERIC(10,2),
    payment_method VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS inventory (
    inventory_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    inventory_date DATE,
    product_id VARCHAR(20) REFERENCES products(product_id),
    opening_stock INTEGER,
    stock_received INTEGER,
    damaged_units INTEGER,
    stock_count INTEGER,
    closing_stock INTEGER
);


select * from sales

------What is the total revenue, cost, and profit?
SELECT datname, length(datname)
FROM pg_database
WHERE datname LIKE 'supermarket_analytics%';


    ROUND(SUM(net_sales)::NUMERIC, 2) AS total_revenue,
    ROUND(SUM(total_cost)::NUMERIC, 2) AS total_cost,
    ROUND(SUM(profit)::NUMERIC, 2) AS total_profit
FROM vw_sales_analysis;


SELECT quote_ident(datname), length(datname)
FROM pg_database
WHERE datname LIKE 'supermarket_analytics%';


ALTER DATABASE "supermarket_analytics " RENAME TO supermarket_analytics;
