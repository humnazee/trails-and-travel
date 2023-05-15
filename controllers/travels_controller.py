from flask import render_template, request, redirect, session
from models.travel import all_travels, get_travel, create_travel, update_travel, delete_travel, like_travel, comment_travel
from services.session_info import current_user

def index():
  travels = all_travels () 
  return render_template('travels/index.html', travels=travels, current_user=current_user())

def new():
  return render_template('travels/new.html')

def create():
  name = request.form.get('name')
  title = request.form.get('title')
  image_url = request.form.get('image_url')
  location = request.form.get('location')
  description = request.form.get('description')
  create_travel(name, title, image_url, location, description)
  return redirect('/travels')

def edit(id):
  travel = get_travel(id)
  return render_template('travels/edit.html', travel=travel)

def update(id):
  name = request.form.get('name')
  title = request.form.get('title')
  image_url = request.form.get('image_url')
  location = request.form.get('location')
  description = request.form.get('description')
  update_travel(id, name, title, image_url, location, description)
  return redirect('/travels')

def delete(id):
  delete_travel(id)
  return redirect('/travels')

def like(id):
  like_travel(id, session['user_id'])
  return redirect('/travels')


def comment(id):
  comment_travel(id, session['user_id'])
  return redirect('/travels')