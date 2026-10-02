-- WEEK 2: SQL FOR DATA ANALYSIS

-- 1. Query top 10 customers by total spend
SELECT 
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 10;

-- 2. Query Average Order Value (AOV) per customer
SELECT 
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders,
    ROUND(AVG(o.total_amount), 2) AS average_order_value
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 1
ORDER BY average_order_value DESC;

-- 3. Customer Segmentation using CASE statement
SELECT 
    customer_id,
    customer_name,
    total_spent,
    CASE 
        WHEN total_spent >= 5000 THEN 'VIP / High Value'
        WHEN total_spent BETWEEN 1500 AND 4999 THEN 'Mid Tier'
        ELSE 'Standard'
    END AS customer_tier
FROM (
    SELECT 
        c.customer_id,
        c.customer_name,
        SUM(o.total_amount) AS total_spent
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name
) customer_summary
ORDER BY total_spent DESC;