from config import *

@app.route("/")
def welcome_page():
    return render_template('index.html')

#routing

@app.route('/app/login',methods=['POST'])
def user_login():
    message = ''
    if request.method=="POST":
        formdata = request.form
        username = formdata.get('username')
        password = formdata.get('password')
        if username and password:
            if username=='python' and password=='abc':
                return render_template('home.html', msg=username)
            else:
                message='Invalid'
                return render_template('index.html',msg=message)
        else:
            message="username and passwod cannot empty"
    return render_template('index.html',msg=message)

@app.route('/app/sign_up',methods=['GET','POST'])
def user_signup():
    message=""
    if request.method == 'POST':
        formdata = request.form  # whatever data we have submitted it inside form
        fname =formdata.get('firstname')
        lname =formdata.get('lastname')
        email=formdata.get('email')
        gender = formdata.get('gender')
        city =formdata.get('city')
        username =formdata.get('username'),
        password =formdata.get('password')
        user1 = UserData(fname=fname,
                         lname=lname,
                         email=email,
                         gender=gender,
                         city=city,
                         username=username,
                         password=password)
        db.session.add(user1)
        db.session.commit()
        message = "User Successfully Registered {}".format(user1.id)
    return render_template('register.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)