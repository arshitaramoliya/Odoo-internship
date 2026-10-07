ALTER TABLE partner
ALTER COLUMN name SET NOT NULL;

BEGIN;

INSERT INTO partner (name, email, city, credit_limit)
SELECT
    'Duplicate Test',
    arshitapatel077@gmail.com,
    'Test City',
    1000
FROM partner
ORDER BY id
LIMIT 1;

ROLLBACK;