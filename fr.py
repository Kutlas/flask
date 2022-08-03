from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flaskblog.models import User, Post
from flaskblog import db, app

db = SQLAlchemy(app)

# import json
#
# posts = []
# with open('posts.json', 'r') as f:
#     i = 0
#     file = f.read()
#     print(file[0])
#     posts = json.loads(file)
    # for i, lin in enumerate(posts):
    #     post = Post(title=lin.get('title'), content=lin.get('content'), user_id=lin.get('user_id'))
    #     db.session.add(post)
    #     db.session.commit()
    # print(posts[0])
