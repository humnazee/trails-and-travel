from flask import Blueprint
from controllers.iconics_controller import index, new, create, edit, update, delete, like, comment

iconics_routes = Blueprint('iconics_routes', __name__)

iconics_routes.route('')(index)
iconics_routes.route('/new')(new)
iconics_routes.route('', methods=['POST'])(create)
iconics_routes.route('/<id>/edit')(edit)
iconics_routes.route('/<id>', methods=["POST"])(update)
iconics_routes.route('/<id>/delete', methods=["POST"])(delete)
iconics_routes.route('/<id>/likes', methods=["POST"])(like)
iconics_routes.route('/<id>/comments', methods=["POST"])(comment)