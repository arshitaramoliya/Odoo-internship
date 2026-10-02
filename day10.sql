
             CREATE TABLE if not exists partner (
                id INTEGER generated always as identity primary key,
                name VARCHAR(100) not null,
                email varchar(150) unique not null,
                city varchar(100)
            );

            INSERT INTO partner (name, email, city)
VALUES
    ('Acme Corp', 'sales@acme.com', 'Mumbai'),
    ('Blue Ridge Ltd', 'hello@blueridge.com', 'Pune'),
    ('Sunrise Tech', 'info@sunrise.in', 'Delhi'),
    ('Green Foods', 'contact@greenfoods.in', 'Mumbai'),
    ('Orbit Systems', 'team@orbit.com', 'Ahmedabad'),
    ('Silver Line', 'office@silverline.in', 'Pune'),
    ('Royal Traders', 'sales@royal.com', 'Delhi'),
    ('Nova Labs', 'hello@novalabs.com', 'Bengaluru'),
    ('Bright Works', 'info@brightworks.in', 'Mumbai'),
    ('Prime Services', 'contact@prime.com', 'Ahmedabad')
ON CONFLICT (email) DO NOTHING;
                        

            CREATE TABLE if not exists sale_order (
                id INTEGER generated always as identity PRIMARY KEY,
                reference VARCHAR(20) unique not null,
                order_date DATE not null,
                partner_id INTEGER REFERENCES partner(id)
            );

            INSERT INTO sale_order (reference, order_date, partner_id)
VALUES
    ('SO001', '2026-09-01', 1),
    ('SO002', '2026-09-02', 2),
    ('SO003', '2026-09-03', 1),
    ('SO004', '2026-09-04', 3),
    ('SO005', '2026-09-05', 4),
    ('SO006', '2026-09-06', 2),
    ('SO007', '2026-09-07', 5),
    ('SO008', '2026-09-08', 1),
    ('SO009', '2026-09-09', 6),
    ('SO010', '2026-09-10', 3),
    ('SO011', '2026-09-11', 7),
    ('SO012', '2026-09-12', 4),
    ('SO013', '2026-09-13', 5),
    ('SO014', '2026-09-14', 2),
    ('SO015', '2026-09-15', 7)
ON CONFLICT (reference) DO NOTHING;

SELECT
    sale_order.reference,
    sale_order.order_date,
    partner.name
FROM sale_order
INNER JOIN partner
    ON sale_order.partner_id = partner.id
ORDER BY sale_order.id;

--INSERT INTO sale_order (reference, order_date, partner_id)
--VALUES ('SO999', '2026-09-30', 999);



-- Day 10 Foreign Key Error I tried to insert a sale order with partner_id 999.
--PostgreSQL rejected it because partner ID 999 does not exist in the
--partner table.
--A foreign key prevents an order from referring to a nonexistent partner.

select partner.name,sale_order.reference,sale_order.order_date from partner left join sale_order on partner.id = sale_order.partner_id order by partner.id,sale_order.id;
