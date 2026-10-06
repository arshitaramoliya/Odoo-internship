CREATE TABLE IF NOT EXISTS product (
    id INTEGER  PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    list_price NUMERIC(12, 2) NOT NULL
);

INSERT INTO product (name, list_price)
VALUES
    ('Laptop', 65000),
    ('Mouse', 800),
    ('Keyboard', 1500),
    ('Monitor', 18000),
    ('Printer', 12000),
    ('Headphones', 2500),
    ('Webcam', 3200),
    ('USB Drive', 700);

SELECT * FROM product ORDER BY id;

 DROP TABLE IF EXISTS sale_order_line;

CREATE TABLE sale_order_line (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES sale_order(id),
    product_id INTEGER NOT NULL REFERENCES product(id),
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(12, 2) NOT NULL
);
    INSERT INTO sale_order_line
    (order_id, product_id, quantity, unit_price)
VALUES
    (1, 1, 1, 65000),
    (1, 2, 2, 800),
    (1, 3, 1, 1500),

    (2, 4, 2, 18000),
    (2, 5, 1, 12000),
    (2, 6, 3, 2500),

    (3, 1, 1, 65000),
    (3, 7, 2, 3200),
    (3, 8, 5, 700);

    select * from sale_order_line order by id