from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html", boolean = 'True')

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email is too short', category='fail')
        elif len(firstName) < 3:
            flash('First name is too short, enter a valid one', category='fail')
        elif password1 != password2:
            flash('Passwords doesnt match', category='fail')
        elif len(password1) < 7:
            flash('Password is too short', category='fail')
        else:
            #add user to db
            flash('User account created successfully', category='success')

    return render_template("sign_up.html")

