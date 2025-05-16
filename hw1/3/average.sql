SELECT AVG(amount) AS average_order_value
FROM orders
WHERE order_date >= '2024-01-01' AND order_date < '2024-04-01';
