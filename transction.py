from datetime import date
from uuid import uuid4

import psycopg

DATABASE_URL = "postgresql://root:root@localhost:5432/odoo_schema_test"


def create_order(partner_id, lines):
    connection = psycopg.connect(DATABASE_URL)

    try:
        with connection.cursor() as cursor:
            reference = f"TEST-{uuid4().hex[:12]}"

            cursor.execute(
                """
                INSERT INTO sale_order
                    (reference, order_date, partner_id)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (reference, date.today(), partner_id),
            )

            order_id = cursor.fetchone()[0]

            for line in lines:
                cursor.execute(
                    """
                    INSERT INTO sale_order_line
                        (order_id, product_id, quantity, unit_price)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        order_id,
                        line["product_id"],
                        line["quantity"],
                        line["unit_price"],
                    ),
                )

        connection.commit()
        return order_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    lines = [
        {"product_id": 1, "quantity": 1, "unit_price": 65000},
        {"product_id": 2, "quantity": 2, "unit_price": 800},
        {"product_id": 3, "quantity": 1, "unit_price": 1500},
    ]

    order_id = create_order(1, lines)
    print(f"Order {order_id} created with {len(lines)} lines.")