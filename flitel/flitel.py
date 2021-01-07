from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = b'dklsdjf@#423f8_#942;3['

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register')
def register():
    return 'register'


@app.route('/login')
def login():
    return 'login'


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
