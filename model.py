import psycopg

DATABASE_URL = "postgresql://root:root@localhost:5432/odoo_schema_test"


class Partner:
    def __init__(self, id, name, email, city, credit_limit):
        self.id = id
        self.name = name
        self.email = email
        self.city = city
        self.credit_limit = credit_limit

    def __str__(self):
        return f"{self.name} - {self.city} (id {self.id})"



    @classmethod
    def browse(cls, partner_id):
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, name, email, city, credit_limit
                    FROM partner
                    WHERE id = %s
                    """,
                    (partner_id,),
                )

                row = cursor.fetchone()

        if row is None:
            return None

        return cls(*row)

    @classmethod
    def search(cls, city=None):
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                if city is None:
                    cursor.execute("""
                        SELECT id, name, email, city, credit_limit
                        FROM partner
                        ORDER BY id
                    """)
                else:
                    cursor.execute(
                        """
                        SELECT id, name, email, city, credit_limit
                        FROM partner
                        WHERE city = %s
                        ORDER BY id
                        """,
                        (city,),
                    )

                rows = cursor.fetchall()

        return [cls(*row) for row in rows]


    def save(self):
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE partner
                    SET name = %s,
                        email = %s,
                        city = %s,
                        credit_limit = %s
                    WHERE id = %s
                    """,
                    (
                        self.name,
                        self.email,
                        self.city,
                        self.credit_limit,
                        self.id,
                    ),
                )



    @classmethod
    def create(cls, name, email, city, credit_limit):
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO partner
                        (name, email, city, credit_limit)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id, name, email, city, credit_limit
                    """,
                    (name, email, city, credit_limit),
                )

                row = cursor.fetchone()

        return cls(*row)

    
    def orders(self):
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, reference, order_date, partner_id
                    FROM sale_order
                    WHERE partner_id = %s
                    ORDER BY id
                    """,
                    (self.id,),
                )

                rows = cursor.fetchall()

        return [SaleOrder(*row) for row in rows]


class SaleOrder:
    def __init__(self, id, reference, order_date, partner_id):
        self.id = id
        self.reference = reference
        self.order_date = order_date
        self.partner_id = partner_id

    def __str__(self):
        return f"{self.reference} - {self.order_date}"

    def partner(self):
        return Partner.browse(self.partner_id)

    def total(self):
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT COALESCE(
                        SUM(quantity * unit_price), 0
                    )
                    FROM sale_order_line
                    WHERE order_id = %s
                    """,
                    (self.id,),
                )

                return cursor.fetchone()[0]

    @classmethod
    def browse(cls, order_id):
        with psycopg.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, reference, order_date, partner_id
                    FROM sale_order
                    WHERE id = %s
                    """,
                    (order_id,),
                )

                row = cursor.fetchone()

        if row is None:
            return None

        return cls(*row)

    
if __name__ == "__main__":
    partners = Partner.search()

    for partner in partners:
        orders = partner.orders()

        print(
            f"{partner.name} ({partner.city})"
            f" - {len(orders)} orders"
        )

        partner_total = 0

        for order in orders:
            amount = order.total()
            partner_total += amount

            print(
                f"    {order.reference} "
                f"{order.order_date} "
                f"{amount:,.2f}"
            )

        print(f"    Total: {partner_total:,.2f}")
        print()


    
