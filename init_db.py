from flask import render_template
from app import db, Post, Comment, app

post1 = Post(title="What is Open Source and How to Get Started?", content="Content for the first post")
post2 = Post(title="Post the second", content="Content for the second post")
post3 = Post(title="Post the Third", content="Content for the first third")

comment1 = Comment(content="comment for the first post",post=post1)
comment2 = Comment(content="comment for the second post",post=post2)
comment3 = Comment(content="Another comment for the second post",post_id=2)
comment4 = Comment(content="Another comment for the first post", post_id=1)

db.session.add_all([post1, post2, post3])
db.session.add_all([comment1, comment2, comment3, comment4])

db.session.commit()


