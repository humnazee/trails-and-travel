from flask import render_template, request, redirect
from models.destination import all_destinations, get_destination, create_destination, update_destination, delete_destination
from services.session_info import current_user

def index():
  destinations = all_destinations () 
  return render_template('destinations/index.html', destinations=destinations, current_user=current_user())

def new():
  return render_template('destinations/new.html')

def create():
  type = request.form.get('type')
  image_url = request.form.get('image_url')
  create_destination(type, image_url)
  return redirect('/')

def edit(id):
  destination = get_destination(id)
  return render_template('destinations/edit.html', destination=destination)

def update(id):
  type = request.form.get('type')
  image_url = request.form.get('image_url')
  update_destination(type, image_url, id)
  return redirect('/')

def delete(id):
  delete_destination(id)
  return redirect('/')
