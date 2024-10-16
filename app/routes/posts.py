import logging
from flask import Blueprint, request, jsonify
from app.models.post import Post

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/create', methods=['POST'])
def crear_post():
    try:
        # Obtenemos los datos del post desde la solicitud
        autor = request.json['autor']
        contenido = request.json['contenido']

        # Creamos un nuevo objeto Post
        post = Post(autor, contenido)

        # Guardamos el post en la base de datos
        post_id = post.save()

        # Retornamos una respuesta exitosa
        return jsonify({'mensaje': 'Post creado exitosamente', 'post_id': str(post_id)}), 201
    except KeyError as e:
        # Manejamos el error si falta algún campo en la solicitud
        return jsonify({'error': f'Falta el campo {e}'}), 400
    except Exception as e:
        # Manejamos cualquier otro error
        logging.error('Error al crear post.', exc_info=True)
        return jsonify({'error': 'Error al crear el post'}), 500

@bp.route('/list', methods=['GET'])
def listar_posts():
    try:
        # Obtenemos todos los posts de la base de datos
        posts = Post.get_all()

        # Convertimos los posts a un formato JSON
        posts_json = [{'autor': post['autor'], 'contenido': post['contenido'], 'fecha_creacion': post['fecha_creacion']} for post in posts]

        # Retornamos la lista de posts
        return jsonify(posts_json), 200
    except Exception as e:
        # Manejamos cualquier error
        logging.error('Error al listar posts.', exc_info=True)
        return jsonify({'error': 'Error al listar posts'}), 500