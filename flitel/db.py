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


def example():
	query = '''SELECT * FROM discount'''

	connection = None
	try:
		params = config()
		connection = psycopg2.connect(**params)
		with connection.cursor() as cursor:
			cursor.execute(query)
			discounts = cursor.fetchall()
			print(discounts)

		# if performing changes this line is needed:
		# connection.commit()
	finally:
		if connection is not None:
			connection.close()
