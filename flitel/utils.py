from datetime import datetime
import bcrypt
from werkzeug.exceptions import NotFound
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
	if not user['type'] == 'customer':
		raise ValueError('You cannot reserve room.')

	error = db.add_room_booking(hotel_id, room_number, user['id'], from_date, to_date)
	return error

def reserve_flight(username, password, airline_id, flight_number):
	user = db.get_user(username)
	if not user or not check_password(password, user['password']):
		raise ValueError('incorrect password')
	if not user['type'] == 'customer':
		raise ValueError('You cannot reserve flight.')

	error = db.add_flight_booking(airline_id, flight_number, user['id'])
	return error

def get_customer_booking(username, booking_id=None):
	user = db.get_user(username)
	if not user['type'] == 'customer':
		raise NotFound()

	return db.get_bookings(user['id'], booking_id)


def handle_payment(username, password, discount_code, booking):
	user = db.get_user(username)
	
	if not user or not check_password(password, user['password']):
		raise ValueError('incorrect password')

	if not user['type'] == 'customer':
		raise NotFound()

	discount = None
	if discount_code:
		discount = db.get_discount(discount_code)
		if not discount:
			raise ValueError('Discount code is invalid.')
		
		
	amount = booking['price']
	if discount:
		amount = amount * (100 - discount['percent']) / 100

	return db.complete_booking(booking['id'], amount, discount_code)

