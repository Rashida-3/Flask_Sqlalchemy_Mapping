from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mapping.sqlite3"
app.config['SQLALCHEMY_TRACK_NOTIFICATION']=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    notes=db.relationship('Notes',backref='user')

    def __repr__(self) -> str:
        return f"<User:{self.name}>"


class Notes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    note=db.Column(db.String(20))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id', ondelete="CASCADE")
    )
 
    def __repr__(self) -> str:
        return f"<Note:{self.note}>"


if __name__=="__main__":
    app.run(debug=True)