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

    


if __name__ == "__main__":
    from uuid import uuid4

    email = f"day18-{uuid4().hex}@example.com"

    created = Partner.create(
        "Sharma Traders",
        email,
        "Delhi",
        25000,
    )
    print("Created:", created)

    partner = Partner.browse(created.id)
    print("Browsed:", partner)

    partner.city = "Bengaluru"
    partner.save()

    updated = Partner.browse(created.id)
    print("After save and re-browse:", updated)

    partners = Partner.search("Mumbai")
    print(f"Search found {len(partners)} partners in Mumbai")
