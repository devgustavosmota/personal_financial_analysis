from app.forms import SignIn
from flask import render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash
from database import get_user_by_email
from . import auth

@auth.route('/signin', methods=['GET', 'POST'])
def signin():

    form = SignIn()

    if form.validate_on_submit():

        email = form.email.data
        user = get_user_by_email(email)

        if user:
            password = form.password.data
            password_hash = user[2]

            if check_password_hash(password_hash, password):
                flash('Logged in!', 'success')
                return redirect(url_for('homepage.dashboard'))
            
            else:
                flash('Incorrect password.', 'error')
                return redirect(url_for('auth.signin'))

        else:
            flash('Unregistered user.')
            return redirect(url_for('auth.signup', email=email))

    return render_template('auth/signin.html', form=form)
