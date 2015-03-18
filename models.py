  from datetime import datetime
from pony.orm import *

db = Database("sqlite", "data.sqlite", create_db=True)

class User(db.Entity):
    username = Required(str, unique=True, lazy=False)
    password = Required(str)
    email = Required(str, unique=True)
    dt = Optional(datetime, default=datetime.now)
    photos = Set("Photo")
    likes = Set("Like")
    comments = Set("Comment", reverse="user")
    mentioned = Set("Comment", reverse="mentioned")


class Photo(db.Entity):
    picture = Required(str)
   # dt = Required(datetime, default=datetime.now)
    tags = Set("Tag")
    user = Optional(User)
    liked = Set("Like")
    comments = Set("Comment")


class Tag(db.Entity):
    name = PrimaryKey(unicode)
    photos = Set(Photo)


class Comment(db.Entity):
    photo = Required(Photo)
    user = Required(User, reverse="comments")
    dt = Required(datetime, default=datetime.now)
    text = Required(unicode)
    mentioned = Set(User, reverse="mentioned")



class Like(db.Entity):
    user = Required(User)
    photo = Required(Photo)
    dt = Required(datetime, default=datetime.now)
    PrimaryKey(user, photo)


sql_debug(True)

db.generate_mapping(create_tables=True)