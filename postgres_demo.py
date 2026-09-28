import psycopg


DATABASE_URL = "postgresql://root:root@localhost:5432/odoo_learning"


def main():
    # The connection closes automatically when this block finishes.
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS partners (
                    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(150) UNIQUE NOT NULL,
                    city VARCHAR(100) NOT NULL
                )
                """
            )

            cursor.executemany(
                """
                INSERT INTO partners (name, email, city)
                VALUES (%s, %s, %s)
                ON CONFLICT (email) DO UPDATE
                SET name = EXCLUDED.name, city = EXCLUDED.city
                """,
                [
                    ("Arshita", "arshita@example.com", "Bengaluru"),
                    ("Jay", "jay@example.com", "Ahmedabad"),
                    ("Rutvi", "rutvi@example.com", "Bengaluru"),
                ],
            )

            cursor.execute(
                "SELECT id, name, email, city FROM partners ORDER BY id"
            )

            print("Connected successfully!\n")
            print("Partners stored in PostgreSQL:")
            for partner_id, name, email, city in cursor.fetchall():
                print(f"{partner_id}: {name} | {email} | {city}")


if __name__ == "__main__":
    main()
