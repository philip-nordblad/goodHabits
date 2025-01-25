from flask_login import login_required, login_user
from flask import (Blueprint, flash, g, redirect, render_template,request,session,url_for)
from . import db, login_manager

bp = Blueprint('auth', __name__,url_prefix='/auth')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route('/register', methods=['GET','POST'])
def register():

    form = LoginForm()