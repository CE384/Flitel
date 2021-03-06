from datetime import date
from flask import Flask, session, redirect, url_for, request, render_template, abort, flash
from functools import wraps

from db import get_flights, get_hotels, get_hotel, get_rooms
import utils

app = Flask(__name__)
app.secret_key = b'dklsdjf@#423f8_#942;3['

### General views ###

@app.route('/')
def home():
	session_username = session.get('username')

	return render_template('index.html', username=session_username)

@app.errorhandler(404)
def page_not_found(e):
	username = session.get('username')
	return render_template('404.html', username=username), 404

@app.after_request
def add_header(r):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also to cache the rendered page for 10 minutes.
	"""
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers['Cache-Control'] = 'public, max-age=0'
	return r

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		session_username = 	session.get('username')
		if session_username is None:
			return redirect(url_for('login', next=request.url))
		return f(*args, **kwargs)
	return decorated_function
	

### Auth views ###

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
		next_url = request.form.get("next")
		try:
			utils.login_user(username, password)
			session['username'] = username
			if next_url:
				return redirect(next_url)
			return redirect(url_for('home'))
		except ValueError as err:
			error = err

	if error:
		flash(error, 'error')
	
	return render_template('login.html', username=session_username)


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
			error = utils.register_customer({
				'username':username,
				'password':password,
				'national_id':national_id,
				'name':name,
				'address':address,
				'phone':phone,
				'email':email
				})

			if not error:
				session['username'] = username
				return redirect(url_for('home'))
		except ValueError as err:
			error = err
	if error:
		flash(error, 'error')

	return render_template('register.html', username=session_username)


### Hotel views ###


@app.route('/hotels', methods=["GET"])
def hotels():
	country_name = request.args.get('country_name', '')
	city_name = request.args.get('city_name', '')
	name = request.args.get('name', '')

	hotels = get_hotels(country=country_name, city=city_name, name=name)
	session_username = session.get('username')

	return render_template('hotels.html', hotels=hotels, username=session_username)

@app.route('/hotels/<int:id>', methods=["GET", "POST"])
def hotel(id):
	session_username = session.get('username')

	booking_id = request.args.get('booking_id', -1)
	rate=False
	if booking_id != -1:
		rate = True
	error = None
	if request.method == "POST":
		rating = request.form.get("rating", None)
		try:
			error = utils.add_rating(
				username=session_username,
				rating=rating,
				hotel_id=id,
				booking_id=booking_id
			)

			if not error:
				flash('Your rating was submitted!', 'success')
		except ValueError as err:
			error = err

		if error:
			flash(error, 'error')


	hotel = get_hotel(id)
	if not hotel:
		abort(404)
	rooms = get_rooms(id)
	return render_template('hotel_info.html', hotel=hotel, rooms=rooms, rate=rate, username=session_username)


@app.route('/hotels/<int:hotel_id>/room/<int:room_number>', methods=["GET", "POST"])
@login_required
def reserve_room(hotel_id, room_number):
	session_username = session.get('username')
	
	error = None
	if request.method == "POST":
		password = request.form.get("password", None)
		from_date = request.form.get("from_date", None)
		to_date = request.form.get("to_date", None)
		try:
			error = utils.reserve_room(
				username=session_username, 
				password=password,
				from_date=from_date,
				to_date=to_date,
				hotel_id=hotel_id,
				room_number=room_number
			)

			if not error:
				flash('Room reserved successfully!', 'success')
				return redirect(url_for('my_bookings'))
		except ValueError as err:
			error = err
		
	if error:
		flash(error, 'error')
	
	return render_template('reserve_room.html', username=session_username)



### Flight views ###

@app.route('/flights', methods=["GET"])
def flights():

	origin_country = request.args.get('origin_country', '')
	destination_city = request.args.get('destination_city', '')
	origin_city = request.args.get('origin_city', '')
	destination_country = request.args.get('destination_country', '')
	departure_date = request.args.get('departure_date', '')

	flights = get_flights(origin_country=origin_country, destination_city=destination_city, origin_city=origin_city,
	 destination_country=destination_country, departure_date=departure_date)
	 
	session_username = session.get('username')

	return render_template('flights.html', flights=flights, username=session_username)


@app.route('/flights/<int:airline_id>/<int:number>', methods=["GET", "POST"])
@login_required
def reserve_flight(airline_id, number):
	session_username = session.get('username')
	
	error = None
	if request.method == "POST":
		password = request.form.get("password", None)
		try:
			error = utils.reserve_flight(
				username=session_username, 
				password=password,
				airline_id=airline_id,
				flight_number=number
			)

			if not error:
				flash('Flight reserved successfully!', 'success')
				return redirect(url_for('my_bookings'))

		except ValueError as err:
			error = err

	if error:
		flash(error, 'error')

	return render_template('reserve_flight.html', username=session_username)


### Booking for users view ###

@app.route('/bookings', methods=['GET'])
@login_required
def my_bookings():
	session_username = session.get('username')

	bookings = utils.get_customer_booking(session_username)

	for booking in bookings:
		if date.today() >= booking['from_date']:
			booking['started'] = True
		if date.today() >= booking['to_date']:
			booking['ended'] = True

	return render_template('bookings.html', bookings=bookings, username=session_username)


@app.route('/payment/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def payment(booking_id):
	session_username = session.get('username')
	booking = utils.get_customer_booking(session_username, booking_id)[0]

	error = None
	if request.method == "POST":
		try:
			password = request.form.get("password", None)
			discount_code = request.form.get("discount", None)
			error = utils.handle_payment(session_username, password, discount_code ,booking)

			if not error:
				flash('Reservation completed succesfully!', 'success')
				return redirect(url_for('my_bookings'))

		except ValueError as err:
			error = err

	if error:
		flash(error, 'error')
	
	return render_template('payment.html', booking=booking, username=session_username)


@app.route('/cancel/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def cancel(booking_id):
	session_username = session.get('username')
	booking = utils.get_customer_booking(session_username, booking_id)[0]

	error = None
	try:
		error = utils.handle_cancel(session_username ,booking)

		if not error:
			flash('Reservation cancelled succesfully!', 'success')
			return redirect(url_for('my_bookings'))

	except ValueError as err:
		error = err

	if error:
		flash(error, 'error')

	return redirect(url_for('my_bookings'))
	
