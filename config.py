from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/aug_batch'
app.config['SECRET_KEY']  = "182KSK91023198jsds7878402940954*&*$@"
db = SQLAlchemy(app)

class UserData(db.Model):  # table
    id = db.Column('user_id',db.Integer,primary_key=True)
    fname = db.Column('firstname',db.String(50))
    lname = db.Column('lastname', db.String(50))
    email = db.Column('email',db.String(50))
    gender = db.Column('gender',db.String(50))
    city = db.Column('city',db.String(50))
    username = db.Column('username',db.String(50),unique=True)
    password = db.Column('password',db.String(50))

with app.app_context():
    db.create_all()
    print("Table Created.....")