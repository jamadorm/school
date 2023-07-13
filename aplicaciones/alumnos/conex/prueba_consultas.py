"""
    Conexión a PostgreSQL con Python
    Ejemplo de CRUD evitando inyecciones SQL

    @author parzibyte
    Más tutoriales en:
                        parzibyte.me/blog
"""
import psycopg2
from conex import conexion

try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT id, nombre, apellido_paterno, apellido_materno FROM alumnos_alumno;")

        # Con fetchall traemos todas las filas
        alumnos = cursor.fetchall()

        # Recorrer e imprimir
        for alumno in alumnos:
            print(alumno)
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()