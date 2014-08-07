from flask import render_template,Flask,session,redirect,url_for
from app import app
from forms import LoginForm
import sys
import imaplib
host='webmail.nitt.edu'
port=143
session={}
@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
	if 'user' in session:
		return render_template('user_home.html',session=session)
	form=LoginForm()
	if form.validate_on_submit():
		username=form.gmail.data
		password=form.password.data
		conn=imaplib.IMAP4_SSL(host,port)
		try:
			conn.login(username,password)
			session['user']=username
			print 'logged in '+username
			return render_template('user_home.html',session=session) 
		except conn.error:
			print 'login unsuccesful'	
	return render_template('index.html',form=form)

@app.route('/user_home',methods=['GET','POST'])
def user_home():
	if 'user' in session:
		return render_template('user_home.html',session=session)

	return redirect(url_for('index'))
@app.route('/admin',methods=['GET','POST'])
@app.route('/logout')
def logout():
	session.pop('user',None)
	return redirect(url_for('index'))
