from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_NOTIFICATION']=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    profile=db.relationship('Profile',backref='user', uselist=False)

    def __repr__(self) -> str:
        return f"<User:{self.name}>"


class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id', ondelete="CASCADE"), unique=True)
 
    def __repr__(self) -> str:
        return f"<Profie:{self.username}>"


if __name__=="__main__":
    # with app.app_context():
    #     db.create_all()
        app.run(debug=True)