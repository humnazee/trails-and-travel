from flask import render_template, request, redirect, session
from models.iconic import all_iconics, get_iconic, create_iconic, update_iconic, delete_iconic, like_iconic, comment_iconic
from services.session_info import current_user

def index():
  iconics = all_iconics () 
  return render_template('iconics/index.html', iconics=iconics, current_user=current_user())

def new():
  return render_template('iconics/new.html')

def create():
  name = request.form.get('name')
  title = request.form.get('title')
  image_url = request.form.get('image_url')
  location = request.form.get('location')
  description = request.form.get('description')
  create_iconic(name, title, image_url, location, description)
  return redirect('/iconics')

def edit(id):
  iconic = get_iconic(id)
  return render_template('iconics/edit.html', iconic=iconic)

def update(id):
  name = request.form.get('name')
  title = request.form.get('title')
  image_url = request.form.get('image_url')
  location = request.form.get('location')
  description = request.form.get('description')
  update_iconic(id, name, title, image_url, location, description)
  return redirect('/iconics')

def delete(id):
  delete_iconic(id)
  return redirect('/iconics')

def like(id):
  like_iconic(id, session['user_id'])
  return redirect('/iconics')


def comment(id):
  comment_iconic(id, session['user_id'])
  return redirect('/iconics')