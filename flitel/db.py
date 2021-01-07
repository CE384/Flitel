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
	print(customer)
	try:
		params = config()
		connection = psycopg2.connect(**params)
		with connection.cursor() as cursor:
			insert_user = f"""insert into user_table (type_, username, password) 
			values('customer', '{customer['username']}', '{customer['password']}')
			RETURNING id; """


			print(insert_user)
			cursor.execute(insert_user)
			id_of_new_row = cursor.fetchone()[0]

			print(id_of_new_row)

			insert_customer = f"""insert into customer (id, national_id, name, email, phone, address) 
			values({id_of_new_row}, '{customer['national_id']}', '{customer['name']}', '{customer['email']}',
			 '{customer['phone']}', '{customer['address']}'); """
			
			cursor.execute(insert_customer)

		connection.commit()
	except Exception as e:
		print(e)
		return "User cannot be created"

	return None

def get_user(username):
	pass
