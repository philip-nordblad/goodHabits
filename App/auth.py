from flask_login import login_required, login_user
from flask import (Blueprint, flash, g, redirect, render_template,request,session,url_for)
from . import db, login_manager
from .forms import LoginForm, RegistrationForm

bp = Blueprint('auth', __name__,url_prefix='/auth')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route('/register', methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        error = None

        if User.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registerd."

        if error is None:
            #set up new user

            new_user = User(username=username,password=generate_password_hash(password,method='pbkdf2:sha256')) 
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html', form=form)

@bp.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        
        username = form.username.data
        password = form.password.data

        error = None
        
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password,password):
            error = "Incorrect password."
        
        if error is None:
            #set up new user
            login_user(user)
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html', form=form)


    @bp.route('/logout')
    @login_required
    def logout():
        logout_user()
        redirect(url_for('index'))