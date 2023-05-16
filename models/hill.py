from db.db import sql


def all_hills():
  return sql('SELECT * FROM hills ORDER BY id')

def get_hill(id):
  hills = sql("SELECT * FROM hills WHERE id = %s", [id])
  return hills[0]

def create_hill(name, title, image_url, location, description):
  sql('INSERT INTO hills(name, title, image_url, location, description) VALUES(%s, %s, %s, %s, %s) RETURNING *', [name, title, image_url, location, description])

def update_hill(id, name, title, image_url, location, description):
  sql('UPDATE hills SET name=%s, title=%s, image_url=%s, location=%s, description=%s WHERE id=%s RETURNING *', [name, title, image_url, location, description, id])

def delete_hill(id):
  sql('DELETE FROM hills WHERE id=%s RETURNING *', [id])

def like_hill(hill_id, user_id):
  sql("INSERT INTO likes(user_id, hill_id) VALUES(%s, %s) RETURNING *", [user_id, hill_id])

def comment_hill(hill_id, user_id):
  sql("INSERT INTO comments(user_id, hill_id) VALUES(%s, %s) RETURNING *", [user_id, hill_id])