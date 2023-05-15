from flask import Blueprint
from controllers.destinations_controller import index, new, create, edit, update, delete

destinations_routes = Blueprint('destinations_routes', __name__)

destinations_routes.route('')(index)
destinations_routes.route('/new')(new)
destinations_routes.route('', methods=['POST'])(create)
destinations_routes.route('/<id>/edit')(edit)
destinations_routes.route('/<id>', methods=["POST"])(update)
destinations_routes.route('/<id>/delete', methods=["POST"])(delete)