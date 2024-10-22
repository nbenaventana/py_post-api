import logging
from flask import Blueprint, request, jsonify
from app.models.post import Post

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/create', methods=['POST'])
def crear_post():
    try:
        # Get post data from the request
        autor = request.json['autor']
        contenido = request.json['contenido']

        # Create a new Post object
        post = Post(autor, contenido)

        # Save the post to the database
        post_id = post.save()

        # Return a successful response
        return jsonify({'mensaje': 'Post creado exitosamente', 'post_id': str(post_id)}), 201
    except KeyError as e:
        # Handle error if any field is missing in the request
        return jsonify({'error': f'Falta el campo {e}'}), 400
    except Exception as e:
        # Handle any other error
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