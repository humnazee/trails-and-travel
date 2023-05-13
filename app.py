from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, redirect
from routes.travels_routes import travels_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "key")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(travels_routes, url_prefix='/travels')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
  return redirect('/travels')