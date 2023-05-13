from db.db import sql


def all_travels():
  return sql('SELECT * FROM travels ORDER BY id')

def get_travel(id):
  travels = sql("SELECT * FROM travels WHERE id = %s", [id])
  return travels[0]

def create_travel(name, title, image_url, location, description):
  sql('INSERT INTO travels(name, title, image_url, location, description) VALUES(%s, %s, %s, %s, %s) RETURNING *', [name, title, image_url, location, description])

def update_travel(id, name, title, image_url, location, description):
  sql('UPDATE travels SET name=%s, title=%s, image_url=%s, location=%s, description=%s WHERE id=%s RETURNING *', [name, title, image_url, location, description, id])

def delete_travel(id):
  sql('DELETE FROM travels WHERE id=%s RETURNING *', [id])

def like_travel(travel_id, user_id):
  sql("INSERT INTO likes(user_id, travel_id) VALUES(%s, %s) RETURNING *", [user_id, travel_id])

def comment_travel(travel_id, user_id):
  sql("INSERT INTO comments(user_id, travel_id) VALUES(%s, %s) RETURNING *", [user_id, travel_id])