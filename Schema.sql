CREATE TABLE if not exists partner (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    city VARCHAR(100) DEFAULT 'Unknown',
    credit_limit NUMERIC(12, 2) DEFAULT 0,
    CONSTRAINT partner_credit_limit_check
        CHECK (credit_limit >= 0)
);

CREATE TABLE if not exists product (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    list_price NUMERIC(12, 2) NOT NULL
);

CREATE TABLE if not exists product_tag (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE if not exists sale_order (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    reference VARCHAR(20) UNIQUE NOT NULL,
    order_date DATE NOT NULL,
    partner_id INTEGER NOT NULL
        REFERENCES partner(id)
);

CREATE TABLE if not exists sale_order_line (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id INTEGER NOT NULL
        REFERENCES sale_order(id)
        ON DELETE CASCADE,
    product_id INTEGER NOT NULL
        REFERENCES product(id),
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(12, 2) NOT NULL
);

CREATE TABLE if not exists product_tag_rel (
    product_id INTEGER NOT NULL
        REFERENCES product(id),
    product_tag_id INTEGER NOT NULL
        REFERENCES product_tag(id),
    PRIMARY KEY (product_id, product_tag_id)
);



INSERT INTO product_tag_rel (product_id, product_tag_id)
VALUES
    -- Laptop
    (1, 1),
    (1, 2),
    (1, 5),

    -- Mouse
    (2, 1),
    (2, 4),

    -- Keyboard
    (3, 1),
    (3, 3),
    (3, 4),

    -- Monitor
    (4, 1),
    (4, 2),
    (4, 3),

    -- Printer
    (5, 1),
    (5, 3),

    -- Headphones
    (6, 1),
    (6, 4),

    -- Webcam
    (7, 1),
    (7, 5),

    -- USB Drive
    (8, 4)
ON CONFLICT (product_id, product_tag_id) DO NOTHING;


INSERT INTO product_tag (name)
VALUES
    ('Electronics'),
    ('Featured'),
    ('Office'),
    ('Accessory'),
    ('New')
ON CONFLICT (name) DO NOTHING;

INSERT INTO product_tag_rel (product_id, product_tag_id)
VALUES
    (1, 1), (1, 2), (1, 5),
    (2, 1), (2, 4),
    (3, 1), (3, 3), (3, 4),
    (4, 1), (4, 2), (4, 3),
    (5, 1), (5, 3),
    (6, 1), (6, 4),
    (7, 1), (7, 5),
    (8, 4)
ON CONFLICT (product_id, product_tag_id) DO NOTHING;

SELECT * FROM product_tag ORDER BY id;

SELECT COUNT(*) AS total_relations
FROM product_tag_rel;