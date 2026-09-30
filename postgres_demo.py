import psycopg

DATABASE_URL = "postgresql://root:root@localhost:5432/odoo_learning"


def dbconnection():

    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:

            # Create simple table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER,
                    name VARCHAR(100),
                    city VARCHAR(100)
                )
            """)


#ae likhne se purana run kiya hua next time run karte time new aayega 
#cursor Python aur PostgreSQL ke beech messenger ka kaam karta hai.
#execute() PostgreSQL ko SQL command bhejta hai.TRUNCATE: table ka saara data remove karta hai.
#TABLE: batata hai ki operation table par ho raha hai.
            cursor.execute("truncate table students")

            # Insert data
            cursor.executemany("""
                INSERT INTO students (id, name, city)
                VALUES (%s, %s, %s)
            """, [
                (1, "Arshita", "Bengaluru"),
                (2, "Jay", "Ahmedabad"),
                (3, "Rutvi", "Bengaluru")
            ])

            # Get data
            cursor.execute("""
                SELECT id, name, city
                FROM students
                ORDER BY id
            """)

            # Print data
            print("Connected successfully!")
            print("Students:")

            for student_id, name, city in cursor.fetchall():
                print(f"{student_id}: {name} | {city}")


            print("city=Bengaluru")
            cursor.execute("select id,name,city from students where city = %s",("Bengaluru",))

            for student_id,name,city in cursor.fetchall():
                print(f"{student_id}:{name}|{city}")

            print("FIRST TWO STUDENS IN ALPHABETICAL ORDER")

            cursor.execute(""" select id,name,city from students order by name asc limit 2 """)

            for student_id,name,city in cursor.fetchall():
                print(f"{student_id}:{name}|{city}")

            print("student whose name starts with J")
            cursor.execute(""" select id,name ,city from students where name like %s""",("A%",))
            for students_id,name,city in cursor.fetchall():
                print(f"{student_id}:{name}|{city}")

            print("and condition return ho rhi he")
            cursor.execute("""select id,name,city from students where name Ilike %s and city=%s""",("a%","Bengaluru"))
#ilike upercase/lowercase ignore krta he
            for student_id,name,city in cursor.fetchall():
                print(f"{student_id}:{name}|{city}")

            print("or condition retun")
            cursor.execute(""" select id,name,city from students where city =%s or city=%s order by id""",("Bengaluru","Ahmedabad"))

            for student_id,name,city in cursor.fetchall():
                print(f"{student_id}:{name}|{city}")

            #same or ko me in se use kar rhi hu
            print("in condition return hogi")
            cursor.execute(""" select id,name,city from students where city in(%s,%s)""",("Bengaluru","Ahmedabad"))

            for student_id,name,city in cursor.fetchall():
                print(f"{student_id}:{name}|{city}")

            print("UPDATE condition return krna he")
            cursor.execute("""update students set city=%s where name=%s """,("Mumbai","Jay"))

            cursor.execute("""
            SELECT id, name, city
            FROM students
            WHERE name = %s
            """, ("Jay",))

            students = cursor.fetchone()
            print("Updated student:", students)

            print("IS null return krna he")
            cursor.execute("""
            INSERT INTO students (id, name, city)
            VALUES (%s, %s, %s)
            """, (4, "Rahul", None))

            print("\nStudents without a city:")

            cursor.execute("""
                SELECT id, name, city
                FROM students
                WHERE city IS NULL
            """)

            for student_id, name, city in cursor.fetchall():
                print(f"{student_id}: {name} | {city}")


            print("delet the specific record")
            cursor.execute("""
            DELETE FROM students
             WHERE name = %s
            """, ("Rahul",))
            cursor.execute("SELECT COUNT(*) FROM students")

            total = cursor.fetchone()[0]
            print(f"Total students: {total}")


            print("\nStudents count by city:")

            cursor.execute("""
                SELECT city, COUNT(*)
                FROM students
                GROUP BY city
                ORDER BY city
            """)

            for city, total in cursor.fetchall():
                print(f"{city}: {total} students")
                                    

dbconnection()
