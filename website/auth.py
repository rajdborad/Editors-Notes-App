from xmlrpc.client import boolean
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    
    data = request.form
    print(data)
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(email) < 4:
            flash('Email must be 4 character long', category='error')
        elif len(first_name) < 2:
            flash('First Name must be 2 character long', category='error')
        elif password1 != password2:
            flash('Both password must be same', category='error')
        elif len(password1) < 8:
            flash('Password must be 8 character long', category='error')
        else:
            flash('Account Created Successfully!...', category='success')

    return render_template("sign_up.html")
