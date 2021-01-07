import bcrypt
from db import get_user, add_customer

def get_hashed_password(password):
	return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(plain_password, hashed_password):
	return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def login_user(username, password):
	user = get_user(username)
	if not user or not check_password(password, user['password']):
		raise ValueError('incorrect username or password')

def register_customer(customer):
	customer['password'] = get_hashed_password(customer['password'])
	if get_user(customer['username']):
		raise ValueError('username already exist')
	return add_customer(customer)
