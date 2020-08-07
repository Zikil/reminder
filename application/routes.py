from flask import render_template, flash, redirect, url_for
from application import application
from application.forms import LoginForm

@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'Ilya'}
    return render_template('main.html', title='home', user=user)

@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)