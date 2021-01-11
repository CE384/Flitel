import bcrypt
import db

def get_hashed_password(password):
	return password
	# return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(plain_password, hashed_password):
	return plain_password == hashed_password
	# return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def login_user(username, password):
	user = db.get_user(username)
	if not user or not check_password(password, user['password']):
		raise ValueError('incorrect username or password')

def register_customer(customer):
	customer['password'] = get_hashed_password(customer['password'])
	if db.get_user(customer['username']):
		raise ValueError('username already exist')
	return db.add_customer(customer)


def reserve_room(username, from_date, to_date, password, hotel_id, room_number):
	user = db.get_user(username)
	if not user or not check_password(password, user['password']):
		raise ValueError('incorrect password')
	if not user['type'] != 'customer':
		raise ValueError('You cannot reserve room')

	error = db.add_room_booking(hotel_id, room_number, user['id'], from_date, to_date)
	return error
