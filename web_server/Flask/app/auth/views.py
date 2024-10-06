from flask import render_template, session, flash, redirect, url_for
from app.form import LoginForm
from . import auth
from models import UserData, UserModel
from flask_login import login_user, login_required, logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        #session['username'] = username
        
        print(password)
        print(username*2)
        if password == username*2:
            user_data = UserData(username=username, password=password)
            user_model = UserModel(user_data=user_data)
            login_user(user_model)

            flash('Bienvenido de nuevo')
            return redirect(url_for('first_template'))
        else:
            flash('nono no podes pasar')
            
        flash('Nombre de usuario registrado con exito')
        return redirect(url_for('index'))
    
    return render_template('login.html', **context)


@auth.route('signut', methods = ['GET', 'POST'])
def singout():
    signut_form = LoginForm()
    context = {
        'signut_form' : signut_form
    }

    if signut_form.validate_on_submit():
        username = signut_form.username.data
        password = signut_form.password.data
        user_data = UserData(username=username, password=password)
        user = UserModel(user_data)

        login_user(user=user)
        flash('bienvenido')
        return redirect(url_for('index'))
    return render_template('signut.html', **context)


@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('regresa pronto')
    return redirect(url_for('auth.login'))