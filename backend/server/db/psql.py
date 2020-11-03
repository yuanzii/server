import psycopg2

con = psycopg2.connect(
        host="127.0.0.1",
        database="car_db",
        user="yuanzi",
        password="yuan7142",
        port=5432
    )

