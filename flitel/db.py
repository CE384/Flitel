import psycopg2
from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
	parser = ConfigParser()
	parser.read(filename)

	db_params = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db_params[param[0]] = param[1]
	else:
		raise Exception("section {} not found".format(section))
	return db_params

def add_customer(customer):
	try:
		params = config()
		connection = psycopg2.connect(**params)
		with connection.cursor() as cursor:
			insert_user = f"""insert into user_table (type_, username, password) 
			values('customer', '{customer['username']}', '{customer['password']}')
			RETURNING id; """

			cursor.execute(insert_user)
			id_of_new_row = cursor.fetchone()[0]

			insert_customer = f"""insert into customer (id, national_id, name, email, phone, address) 
			values({id_of_new_row}, '{customer['national_id']}', '{customer['name']}', '{customer['email']}',
			 '{customer['phone']}', '{customer['address']}'); """
			
			cursor.execute(insert_customer)

		connection.commit()
	except Exception as e:
		print(e)
		return e

	return None

def get_user(username):
	user = None
	try:
		params = config()
		connection = psycopg2.connect(**params)
		with connection.cursor() as cursor:
			query = f"""select * from user_table where username='{username}'"""
			
			cursor.execute(query)
			result = cursor.fetchall()
			if result:
				user = {'username': username, 'type': result[0][1], 'password' : result[0][3]}
			print(user)
	except Exception as e:
		print(e)
		return e

	return user


def get_hotels():
	hotels = []
	try:
		params = config()
		connection = psycopg2.connect(**params)
		with connection.cursor() as cursor:
			query = f"""select name, id, city_name, country_name, stars_count from hotels_info;"""
			
			cursor.execute(query)
			results = cursor.fetchall()
			for r in results:
				hotel = {
					'name': r[0],
					'id': r[1],
					'city_name': r[2],
					'country_name': r[3],
					'stars_count': r[4]
				}
				hotels.append(hotel)
	except Exception as e:
		print(e)
		return e

	return hotels

def get_hotel(hotel_id):
	hotel = None
	try:
		params = config()
		connection = psycopg2.connect(**params)
		with connection.cursor() as cursor:

			query = f"""select name, description, phone, website, address, facilities, stars_count, country_name, city_name, id
			from hotels_info natural join hotel where id = {hotel_id};"""
			
			cursor.execute(query)
			r = cursor.fetchone()
			if r:
				hotel = {
					'name': r[0],
					'description': r[1],
					'phone': r[2],
					'website': r[3],
					'address': r[4],
					'facilities': r[5],
					'stars_count': r[6],
					'country_name': r[7],
					'city_name': r[8],
					'id': r[9]
				}

	except Exception as e:
		print(e)
		return e

	return hotel

def get_rooms(hotel_id):
	rooms = []
	try:
		params = config()
		connection = psycopg2.connect(**params)
		with connection.cursor() as cursor:
			query = f"""select number, type_, capacity, price from hotels_rooms
			where id = {hotel_id};"""
			
			cursor.execute(query)
			results = cursor.fetchall()
			for r in results:
				room = {
					'number': r[0],
					'type': r[1],
					'capacity': r[2],
					'price': r[3]
				}
				rooms.append(room)
	except Exception as e:
		print(e)
		return e
	print(rooms)
	return rooms

def get_flights():
	flights = []
	try:
		params = config()
		connection = psycopg2.connect(**params)
		with connection.cursor() as cursor:
			query = f"""select airline_name, airline_id, number, price, departure_date,
			origin_city_name, origin_country_name, destination_city_name, destination_country_name from flight_info;"""
			
			cursor.execute(query)
			results = cursor.fetchall()
			for r in results:
				flight = {
					'airline_name': r[0],
					'airline_id': r[1],
					'number': r[2],
					'price': r[3],
					'departure_date': r[4],
					'origin_city_name': r[5],
					'origin_country_name': r[6],
					'destination_city_name': r[7],
					'destination_country_name': r[8]
				}
				flights.append(flight)
	except Exception as e:
		print(e)
		return e

	return flights
