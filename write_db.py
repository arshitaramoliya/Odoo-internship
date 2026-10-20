import psycopg

DATABASE_URL = "postgresql://root:root@localhost:5432/odoo_schema_test"


def update_credit(partner_id, new_limit):
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE partner
                SET credit_limit = %s
                WHERE id = %s
                RETURNING id, name, credit_limit
                """,
                (new_limit, partner_id),
            )

            updated_partner = cursor.fetchone()

    return updated_partner

def delete_partner(partner_id):
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM partner
                WHERE id = %s
                RETURNING id, name
                """,
                (partner_id,),
            )

            deleted_partner = cursor.fetchone()

    return deleted_partner
if __name__ == "__main__":
    partner = delete_partner(184)

    if partner is None:
        print("Partner not found")
    else:
        print("Deleted partner:", partner)


def test_commit():
    connection = psycopg.connect(DATABASE_URL)

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO partner (name, email, city, credit_limit)
                VALUES (%s, %s, %s, %s)
                RETURNING id
                """,
                (
                    "Commit Test",
                    "commit-test@example.com",
                    "Mumbai",
                    1000,
                ),
            )

            print("Generated ID:", cursor.fetchone()[0])

        # connection.commit()

    finally:
        connection.close()


test_commit()


