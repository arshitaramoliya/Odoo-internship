import psycopg

DATABASE_URL = "postgresql://root:root@localhost:5432/odoo_schema_test"

with psycopg.connect(DATABASE_URL) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, name, city
            FROM partner
            ORDER BY id
        """)

        partners = cursor.fetchall()

        for partner in partners:
            print(partner)

def get_partners(city):
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, name, city
                FROM partner
                WHERE city = %s
                ORDER BY id
                """,
                (city,),
            )

            return cursor.fetchall()


def print_report():
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT DISTINCT city
                FROM partner
                WHERE city IS NOT NULL
                ORDER BY city
            """)

            cities = cursor.fetchall()

    for (city,) in cities:
        print(city)

        for partner_id, name, partner_city in get_partners(city):
            print(f"    {name}")


print_report







