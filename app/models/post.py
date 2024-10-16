from datetime import datetime

from app.utils.db import mongo

class Post:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        self.fecha_creacion = datetime.utcnow()

    def save(self):
        post_dict = {
            'autor': self.autor,
            'contenido': self.contenido,
            'fecha_creacion': self.fecha_creacion
        }
        result = mongo.db.posts.insert_one(post_dict)
        return result.inserted_id
