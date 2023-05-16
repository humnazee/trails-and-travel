from flask import render_template, request, redirect, session
from models.hill import all_hills, get_hill, create_hill, update_hill, delete_hill, like_hill, comment_hill
from services.session_info import current_user

def index():
  hills = all_hills () 
  return render_template('hills/index.html', hills=hills, current_user=current_user())

def new():
  return render_template('hills/new.html')

def create():
  name = request.form.get('name')
  title = request.form.get('title')
  image_url = request.form.get('image_url')
  location = request.form.get('location')
  description = request.form.get('description')
  create_hill(name, title, image_url, location, description)
  return redirect('/hills')

def edit(id):
  hill = get_hill(id)
  return render_template('hills/edit.html', hill=hill)

def update(id):
  name = request.form.get('name')
  title = request.form.get('title')
  image_url = request.form.get('image_url')
  location = request.form.get('location')
  description = request.form.get('description')
  update_hill(id, name, title, image_url, location, description)
  return redirect('/hills')

def delete(id):
  delete_hill(id)
  return redirect('/hills')

def like(id):
  like_hill(id, session['user_id'])
  return redirect('/hills')


def comment(id):
  comment_hill(id, session['user_id'])
  return redirect('/hills')