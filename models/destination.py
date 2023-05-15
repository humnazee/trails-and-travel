from db.db import sql


def all_destinations():
  return sql('SELECT * FROM destinations ORDER BY id')

def get_destination(id):
  destinations = sql("SELECT * FROM destinations WHERE id = %s", [id])
  return destinations[0]

def create_destination(type, image_url):
  sql('INSERT INTO destinations(type, image_url) VALUES(%s, %s) RETURNING *', [type, image_url])

def update_destination(id, type, image_url):
  sql('UPDATE destinations SET type=%s, image_url=%s WHERE id=%s RETURNING *', [type, image_url, id])

def delete_destination(id):
  sql('DELETE FROM destinations WHERE id=%s RETURNING *', [id])
