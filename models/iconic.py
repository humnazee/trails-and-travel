from db.db import sql


def all_iconics():
  return sql('SELECT * FROM iconics ORDER BY id')

def get_iconic(id):
  iconics = sql("SELECT * FROM iconics WHERE id = %s", [id])
  return iconics[0]

def create_iconic(name, title, image_url, location, description):
  sql('INSERT INTO iconics(name, title, image_url, location, description) VALUES(%s, %s, %s, %s, %s) RETURNING *', [name, title, image_url, location, description])

def update_iconic(id, name, title, image_url, location, description):
  sql('UPDATE iconics SET name=%s, title=%s, image_url=%s, location=%s, description=%s WHERE id=%s RETURNING *', [name, title, image_url, location, description, id])

def delete_iconic(id):
  sql('DELETE FROM iconics WHERE id=%s RETURNING *', [id])

def like_iconic(iconi_id, user_id):
  sql("INSERT INTO likes(user_id, iconic_id) VALUES(%s, %s) RETURNING *", [user_id,iconi_id])

def comment_iconic(iconi_id, user_id):
  sql("INSERT INTO comments(user_id, iconic_id) VALUES(%s, %s) RETURNING *", [user_id, iconi_id])