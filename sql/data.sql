INSERT INTO customers (name, email) VALUES
('Juan Perez', 'juan@gmail.com'),
('Ana Gomez', 'ana@gmail.com');

INSERT INTO products (name, price, stock) VALUES
('Camiseta Urbana', 25.99, 100),
('Gorra Street', 15.50, 50);

INSERT INTO orders (customer_id) VALUES (1), (2);

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1,1,2),
(2,2,1);

