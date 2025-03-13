import psycopg2
import os 

# Configuración de la conexión a PostgreSQL
DB_CONFIG = {
    "dbname": "GALATEA ",
    "user": "postgres",
    "password": "anlorestrepo",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    """Establece la conexión con la base de datos."""
    return psycopg2.connect('postgres://postgres:anlorestrepo@localhost:5432/GALATEA')

def insert_manuscript(content, has_clue):
    """Guarda el manuscrito en la base de datos."""
    conn = get_connection()
    print('Conexion exitosa')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO manuscripts (content, has_clue) VALUES (%s, %s);",
        (str(content), has_clue)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_stats():
    """Obtiene estadísticas de manuscritos analizados."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FILTER (WHERE has_clue = TRUE) AS count_clue_found, "
        "COUNT(*) FILTER (WHERE has_clue = FALSE) AS count_no_clue, "
        "(COUNT(*) FILTER (WHERE has_clue = TRUE) * 1.0 / NULLIF(COUNT(*), 0)) AS ratio "
        "FROM manuscripts;"
    )
    result = cur.fetchone()
    cur.close()
    conn.close()

    return {
        "count_clue_found": result[0] or 0,
        "count_no_clue": result[1] or 0,
        "ratio": round(result[2] or 0.0, 2)
    }