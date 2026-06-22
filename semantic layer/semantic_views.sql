CREATE VIEW vw_customer_sales AS
SELECT
    c.customer_name,
    SUM(o.quantity) AS total_quantity
FROM orders_fact o
JOIN customers_dim c
ON o.customer_id = c.customer_id
GROUP BY c.customer_name;

CREATE VIEW vw_product_sales AS
SELECT
    p.product_name,
    SUM(o.quantity) AS total_quantity
FROM orders_fact o
JOIN products_dim p
ON o.product_id = p.product_id
GROUP BY p.product_name;
