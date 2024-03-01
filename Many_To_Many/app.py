from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)

user_channel=db.Table('user_channel',
    db.Column('userid', db.Integer, db.ForeignKey('user.id')),
    db.Column('channelid', db.Integer, db.ForeignKey('channel.id'))
 )

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    following=db.relationship('Channel', secondary=user_channel,backref='followers')

    def __repr__(self):
        return f'User: {self.name}'

class Channel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))

    def __repr__(self):
        return f'Channel: {self.name}'




if __name__=="__main__":
    app.run(debug=True)


# >>> from app import db,User,Channel
# >>> db.create_all()
# >>> object=User(name="Rashida")
# >>> ans=User(name="Ansari")
# >>> pretty=Channel(name="Pretty Printed")
# >>> zo=Channel(name="Zobia Ansari")
# >>> db.session.add_all([object,ans,pretty,zo])
# >>> db.session.commit()
# >>> object.following.append(pretty)
# >>> db.session.commit()
# >>> object.following.append(zo)
# >>> db.session.commit()
# >>> object.following
# [Channel: Pretty Printed, Channel: Zobia Ansari]
# >>> ans.followers
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'User' object has no attribute 'followers'. Did you mean: 'following'?
# >>> pretty.followers 
# [User: Rashida]
# >>> zo.followers
# [User: Rashida]
# >>> ans.following.append(pretty)
# >>> db.session.commit()
# >>> pretty.followers
# [User: Rashida, User: Ansari]
# >>> for followers in pretty.followers:
# ... print(followers.name)






