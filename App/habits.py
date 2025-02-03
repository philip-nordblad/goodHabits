from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import current_user, login_required
from .forms import HabitForm
from .models import Habit
from . import db



bp = Blueprint('home',__name__,url_prefix='/home')

@bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    form = HabitForm()

    if form.validate_on_submit() and current_user.is_authenticated:
        title = form.title.data
        category = form.category.data

        new_habit = Habit(title=title, category=category, count=0, user_id=current_user.get_id())
        db.session.add(new_habit)
        db.session.commit()

        flash('Habit created successfully!', 'success')
        return redirect(url_for('home.home'))  # Redirect to the home page to display the updated list of habits

    # Query habits associated with the current user
    habits = Habit.query.filter_by(user_id=current_user.get_id()).all()
    return render_template('home.html', form=form, habits=habits)




@bp.route('/deleteHabit/<int:habit_id>', methods = ["POST"])
def deleteHabit(habit_id):
    habit = Habit.query.get_or_404(habit_id)

    if (int(habit.user_id) != int(current_user.get_id())):
        flash('You do not have permission to delete this habit')
        redirect(url_for('home.home'))

    db.session.delete(habit)
    db.session.commit()
    flash('Habit deleted successfully')
    return redirect(url_for('home.home'))


@bp.route('/addCount/<int:habit_id>', methods = ['POST'])
def addCount(habit_id):

    habit = Habit.query.get_or_404(habit_id)
    habit.count += 1

    db.session.commit()

    return redirect(url_for('home.home'))

    