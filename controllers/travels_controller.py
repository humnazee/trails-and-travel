from flask import render_template, request, redirect, session
from models import all_travels, get_travel, create_travel, update_travel, delete_travel, like_travel,comment_travel
from services.session_info import current_user

def index():
  travels = all_travels ('travels/index.html', travels=travels, current_user=current_user())

def new():
  return render_template('travels/new.html')

def create():
  name = request.form.get('name')
  tittle = request.form.get('tittle')
  image_url = request.form.get('image_url')
  location = request.form.get('location')
  description = request.form.get('description')
  create_travel(id, name, tittle, image_url, location, description )
  return redirect('/')

def edit(id):
  travel = get_travel(id)
  return render_template('travel/edit.html', travel=travel)

def update(id):
  name = request.form.get('name')
  tittle = request.form.get('tittle')
  image_url = request.form.get('image_url')
  location = request.form.get('location')
  description = request.form.get('description')
  update_travel(id, name, tittle, image_url, location, description )
  return redirect('/')

def delete(id):
  delete_travel(id)
  return redirect('/')

def like(id):
  like_travel(id, session['user_id'])
  return redirect('/')


def comment(id):
  comment_travel(id, session['user_id'])
  return redirect('/')