from datetime import datetime
from flask import current_app, g
from app.utils.db import get_db

class Post:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        self.fecha_creacion = datetime.utcnow()

    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO posts (autor, contenido, fecha_creacion) VALUES (%s, %s, %s) RETURNING id",
            (self.autor, self.contenido, self.fecha_creacion)
        )
        post_id = cursor.fetchone()[0]
        db.commit()
        cursor.close()
        return post_id

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT autor, contenido, fecha_creacion FROM posts")
        posts = cursor.fetchall()
        cursor.close()
        return [{'autor': row[0], 'contenido': row[1], 'fecha_creacion': row[2]} for row in posts]

