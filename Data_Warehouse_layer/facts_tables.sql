CREATE TABLE orders_fact (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id VARCHAR(10),
    quantity INTEGER
);
