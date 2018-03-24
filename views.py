from app import app
from flask import render_template,redirect,url_for
from werkzeug.security  import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user
from model import *
from database import *


login_manager=LoginManager(app)
login_manager.login_view='login'

#used to connect usermixin woth the database
@login_manager.user_loader
def load_user(user_id):
	return(user.query.get(int(user_id)))
@app.route('/')
def index():
    return(render_template('index.html'))


@app.route('/login',methods=['GET','POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        log_user=user.query.filter_by(name=form.username.data).first()
        if log_user:
            if check_password_hash(log_user.password,form.password.data):
            	login_user(log_user,remember=form.remember.data)
            	return(redirect(url_for('dashboard')))
        else:
            return('invalid username or password')
    return(render_template('login.html',form=form))


@app.route('/signup',methods=['GET','POST'])
def signup():
    form=register_form()
    if form.validate_on_submit():
    	hashed_password=generate_password_hash(form.password.data,method='sha256')
        new_user=user(form.username.data,form.email.data,hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return('new user created')
    	#return('<h1>'+form.username.data+' '+form.password.data+' '+form.email.data+'</h1>')
    return(render_template('signup.html',form=form))


@app.route('/dashboard')
@login_required
def dashboard():
    return(render_template('dashboard.html',name=current_user.name))
@app.route('/logout')
def logout():
	logout_user()
	return (redirect(url_for('index')))