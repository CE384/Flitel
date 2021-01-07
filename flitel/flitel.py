from flask import Flask, session, redirect, url_for, request, render_template

from utils import login_user, register_customer


app = Flask(__name__)
app.secret_key = b'dklsdjf@#423f8_#942;3['


@app.route('/')
def home():
	session_username = session.get('username')

	return render_template('index.html', username=session_username)

@app.errorhandler(404)
def page_not_found(e):
	username = session.get('username')
	return render_template('404.html', username=username), 404


@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('home'))


@app.route('/login', methods=["GET", "POST"])
def login():
	error = None
	session_username = 	session.get('username')

	if session_username is not None:
		error = "please logout first"
	elif request.method == "POST":
		username = request.form.get("username", "")
		password = request.form.get("password", "")

		try:
			login_user(username, password)
			session['username'] = username
			return redirect(url_for('home'))
		except ValueError as err:
			error = err
	
	return render_template('login.html', error=error, username=session_username)


@app.route('/register', methods=["GET", "POST"])
def register():
	error = None
	session_username = session.get('username')

	if session_username is not None:
		error = "please logout first"
	elif request.method == "POST":
		username = request.form.get("username", None)
		password = request.form.get("password", None)
		national_id = request.form.get("national_id", None)
		name = request.form.get("name", None)
		address	= request.form.get("address", None)
		phone = request.form.get("phone", None)
		email = request.form.get("email", None)
		try:
			error = register_customer({
				'username':username,
				'password':password,
				'national_id':national_id,
				'name':name,
				'address':address,
				'phone':phone,
				'email':email
				})

			if not error:
				print(username)
				session['username'] = username
				return redirect(url_for('home'))
		except ValueError as err:
			error = err

	return render_template('register.html', error=error, username=session_username)

