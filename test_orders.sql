-- order_id, customer_name, drink, size, extras, price,

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    customer_name VARCHAR(20) NOT NULL, 
    drink VARCHAR(20) NOT NULL,
    size VARCHAR(6) NOT NULL,
    extras BOOLEAN NULL,
    price INTEGER NOT NULL 
);

INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('Abiodun', 'hot chocolate', 'medium', false, 2.95);
INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('Beth', 'mocha', 'medium', false, 3.95);
INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('Carl', 'latte', 'small', false, 3.95);
INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('Deyja', 'berrie smoothie', 'large', false, 4.95);
INSERT INTO orders (customer_name, drink, size, extras, price) VALUES ('Edie', 'americano', 'small', false, 2.95);