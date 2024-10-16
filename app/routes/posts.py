import logging
from flask import Blueprint, request, jsonify
from app.models.post import Post

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/', methods=['POST'])
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