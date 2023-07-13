"""
    Conexión a PostgreSQL con Python
    Ejemplo de CRUD evitando inyecciones SQL

    @author parzibyte
    Más tutoriales en:
                        parzibyte.me/blog
"""

import psycopg2

# Recomendado: https://parzibyte.me/blog/2018/12/20/args-kwargs-python/
try:
    credenciales = {
        "dbname": "db_school",
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",
        "port": 5432
    }
    conexion = psycopg2.connect(**credenciales)
    if conexion:
        print("Te has conectado")
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)
