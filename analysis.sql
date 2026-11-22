
-- 1. Total Revenue
SELECT
    ROUND(SUM(sales)::numeric, 2) AS total_revenue
FROM sales;


-- 2. Total Orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM sales;


-- 3. Top 5 Best-Selling Products
SELECT
    product_name,
    SUM(quantity) AS total_quantity_sold
FROM sales
GROUP BY product_name
ORDER BY total_quantity_sold DESC
LIMIT 5;


-- 4. Revenue by Category
SELECT
    category,
    ROUND(SUM(sales)::numeric, 2) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;


-- 5. Top 5 Customers
SELECT
    customer_id,
    customer_name,
    ROUND(SUM(sales)::numeric, 2) AS total_spent
FROM sales
GROUP BY customer_id, customer_name
ORDER BY total_spent DESC
LIMIT 5;


-- 6. Average Order Value
SELECT
    ROUND(AVG(order_total)::numeric, 2) AS average_order_value
FROM (
    SELECT
        order_id,
        SUM(sales) AS order_total
    FROM sales
    GROUP BY order_id
) AS orders;


-- 7. Monthly Revenue
SELECT
    DATE_TRUNC('month', order_date) AS month,
    ROUND(SUM(sales)::numeric, 2) AS monthly_revenue
FROM sales
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;
