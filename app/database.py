import psycopg2
import os
import json

DB_URL = os.getenv("DATABASE_URL", "postgres://postgres:anlorestrepo@localhost:5432/GALATEA")

def get_connection():
    try:
        conn = psycopg2.connect(DB_URL)
        return conn
    except psycopg2.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

def insert_manuscript(content, has_clue):
    conn = get_connection()
    if not conn:
        return

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO manuscripts (content, has_clue) VALUES (%s, %s);",
                    (json.dumps(content), has_clue) 
                )
    except psycopg2.Error as e:
        print(f"Error al insertar en la base de datos: {e}")
    finally:
        conn.close()

def get_stats():
    conn = get_connection()
    if not conn:
        return {"count_clue_found": 0, "count_no_clue": 0, "ratio": 0.0}

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COUNT(*) FILTER (WHERE has_clue = TRUE) AS count_clue_found, "
                    "COUNT(*) FILTER (WHERE has_clue = FALSE) AS count_no_clue, "
                    "(COUNT(*) FILTER (WHERE has_clue = TRUE) * 1.0 / NULLIF(COUNT(*), 0)) AS ratio "
                    "FROM manuscripts;"
                )
                result = cur.fetchone()
                return {
                    "count_clue_found": result[0] or 0,
                    "count_no_clue": result[1] or 0,
                    "ratio": round(result[2] or 0.0, 2)
                }
    except psycopg2.Error as e:
        print(f"Error al obtener estadísticas: {e}")
        return {"count_clue_found": 0, "count_no_clue": 0, "ratio": 0.0}
    finally:
        conn.close()