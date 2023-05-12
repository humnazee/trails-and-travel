from flask import Blueprint
from controllers.travels_controller import index, new, create, edit, update, delete, like, comment

travels_routes = Blueprint('travels_routes', __name__)

travels_routes.route('')(index)
travels_routes.route('/new')(new)
travels_routes.route('', methods=['POST'])(create)
travels_routes.route('/<id>/edit')(edit)
travels_routes.route('/<id>', methods=["POST"])(update)
travels_routes.route('/<id>/delete', methods=["POST"])(delete)
travels_routes.route('/<id>/likes', methods=["POST"])(like)
travels_routes.route('/<id>/comments', methods=["POST"])(comment)
