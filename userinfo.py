from config import db,app

class userdata(db.Model):
    id         = db.Column('stud_id', db.Integer(), primary_key=True, autoincrement=True)
    name       = db.Column('stud_name', db.String(50))
    gender     = db.Column('stud_gender', db.String(50))
    birth_date = db.Column('stud_birthday_date', db.Date())
    blood_group= db.Column('stud_blood_group', db.String(50))
    fname      = db.Column('stud_father_name', db.String(50))
    mobileno   = db.Column('stud_mobile_no', db.BigInteger())
    occupation = db.Column('stud_father_occupation', db.String(50))
    email_id   = db.Column('stud_email_id', db.String(50))
    address    = db.Column('stud_address', db.String(50))
    username   = db.Column('stud_username', db.String(50))
    password   = db.Column('stud_password', db.String(50))

with app.app_context():
    db.create_all()
    print("Table Created.....")