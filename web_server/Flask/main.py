from flask import Flask, request, make_response, \
    redirect, render_template, abort, session, url_for, \
    flash
from flask_bootstrap import Bootstrap

import unittest
from app import create_app
from app.form import LoginForm

from flask_login import login_required, current_user

app = create_app()


todos = ['hola', 'no']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404) 
def not_found(error): 
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

    
@app.route('/index')
def index():
    response = make_response(redirect('/first_template'))
    # response.set_cookie('user_ip', request.remote_addr)
    session['user_ip'] = request.remote_addr
    return response
    

@app.route('/my_ip')
def example_request():
    return "Tu ip es {}".format(request.remote_addr)


@app.route('/hello')
def hello():
    return "Hola amigito"


@app.route('/first_template', methods= ['GET'])
@login_required
def first_template():
    login_form = LoginForm()
    context = {
        #'user_ip' : request.cookies.get('user_ip'),
        'user_ip' : session.get('user_ip'),
        'todos' : todos,
        'login_form' : login_form,
        'username' : session.get('username')
    }
    
    return render_template('hello.html', **context)

@app.route('/error_500')
def error_500():
    abort(500)