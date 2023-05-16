from db.db import sql


def all_destinations():
  return sql('SELECT * FROM destinations ORDER BY id')

def get_destination(id):
  destinations = sql("SELECT * FROM destinations WHERE id = %s", [id])
  return destinations[0]

def create_destination(name, image_url):
  sql('INSERT INTO destinations(name, image_url) VALUES(%s, %s) RETURNING *', [name, image_url])

def update_destination(id, name, image_url):
  sql('UPDATE destinations SET name=%s, image_url=%s WHERE id=%s RETURNING *', [name, image_url, id])

def delete_destination(id):
  sql('DELETE FROM destinations WHERE id=%s RETURNING *', [id])
