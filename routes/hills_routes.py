from flask import Blueprint
from controllers.hills_controller import index, new, create, edit, update, delete, like, comment

hills_routes = Blueprint('hills_routes', __name__)

hills_routes.route('')(index)
hills_routes.route('/new')(new)
hills_routes.route('', methods=['POST'])(create)
hills_routes.route('/<id>/edit')(edit)
hills_routes.route('/<id>', methods=["POST"])(update)
hills_routes.route('/<id>/delete', methods=["POST"])(delete)
hills_routes.route('/<id>/likes', methods=["POST"])(like)
hills_routes.route('/<id>/comments', methods=["POST"])(comment)