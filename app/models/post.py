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
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        print(posts)
        cursor.close()
        return posts
        #return [{'autor': row[1], 'contenido': row[2], 'fecha_creacion': row[3]} for row in posts]

