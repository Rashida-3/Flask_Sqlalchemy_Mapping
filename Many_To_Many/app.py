from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)

user_page=db.Table('user_page',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('page_id',db.Integer,db.ForeignKey('page.id')),
)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    following=db.relationship('Page',secondary=user_page,backref='followers')

    def __repr__(self) -> str:
        return f'<User:{self.name}>'

class Page(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))

    def __repr__(self) -> str:
        return f'<page:{self.name}>'

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)