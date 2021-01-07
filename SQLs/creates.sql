create table country(
	code 			integer,
	name 			varchar(50) not null unique,
	
	primary key (code)
);

create table city(
	country_code 	integer,
	code 			integer,
	name 			varchar(50) not null,
	
	foreign key (country_code) references country(code),
	primary key (country_code, code)
);

create table user_table (
	id 				serial,
	type 			varchar(8) not null check (
		type in ('customer', 'airline', 'hotel')
	),
	username 		varchar(20) not null unique,
	password 		varchar(64) not null,
	
	primary key (id)
);

create table costumer (
	id 				integer,
	national_id 	varchar(20) not null unique check (national_id ~ '^[0-9]+$'),
	first_name		varchar(30) not null,
	last_name 		varchar(30) not null,
	address 		varchar(150),
	phone 			varchar(20) check (phone ~ '^[0-9]+$'),
	email 			varchar(100) check (
		email ~ '^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'
	),

	foreign key (id) references user_table(id),
	primary key (id)
);

create table airline (
	id 				integer,
	name 			varchar(30) not null unique,
	description 	text,

	foreign key (id) references user_table(id),
	primary key (id)
);

create table hotel (
	id 				integer,
	name 			varchar(30) not null unique,
	description 	text,
	phone 			varchar(20) check (phone ~ '^[0-9]+$'),
	facilities 		text,
	address 		varchar(150),
	website 		varchar(100),
	stars_count 	integer check (
		stars_count >= 1 and stars_count <= 5
	),
	country_code 	integer not null,
	city_code 		integer not null,
	location 		point,

	foreign key (id) references user_table(id),
	foreign key (country_code, city_code) references city(country_code, code),
	primary key (id)
);
create table room(
	hotel_id 		integer,
	number 			integer not null,
	type 			varchar(5) check (type in ('1 bed', '2 beds', 'suite')),
	capacity 		integer check (capacity >= 0),
	price 			integer check (price >= 0),
	
	foreign key (hotel_id) references hotel(id),
	primary key (hotel_id, number)
);
create table flight (
	airline_id 					integer,
	number 						integer not null,
	type 						varchar(11) check (type in ('buisiness', 'economy', 'first class')),
	capacity 					integer check (capacity >= 0),
	price 						integer check (price >= 0),
	origin_country_code 		integer,
	origin_city_code 			integer,
	destination_country_code 	integer,
	destination_city_code 		integer,
	departure_date 				date,
	departure_time 				time,

	foreign key (airline_id) references airline(id),
	foreign key (origin_country_code, origin_city_code) references city(country_code, code),
	foreign key (destination_country_code, destination_city_code) references city(country_code, code),
	primary key (airline_id, number)
);

create table discount(
	id 		varchar(10),
	percent	integer not null check (
		percent >= 0 and percent <= 100
	),

	primary key (id)
);

create table booking(
	id 					serial,
	submission_date 	date,
	transaction_date 	date,
	status 				varchar(20) check (
		status in ('completed', 'cancelled', 'waiting for payment')
	),
	transaction_amount 	integer,
	costumer_id 		integer not null,
	
	foreign key (costumer_id) references costumer(id),
	primary key (id)
);

create table book_discount(
	booking_id 		integer,
	discount_id 	varchar(10),

	foreign key (booking_id) references booking(id),
	foreign key (discount_id) references discount(id),
	primary key (booking_id, discount_id)
);

create table flight_booking(
	id 				integer,
	airline_id 		integer,
	flight_number 	integer,

	foreign key (airline_id, flight_number) references flight(airline_id, number),
	foreign key (id) references booking(id),
	primary key (id)
);

create table room_booking(
	id 				integer,
	hotel_id		integer,
	room_number 	integer,
	from_date 		date,
	to_date 		date,
	customer_rating integer check (
		customer_rating >= 1 and customer_rating <= 5
	),

	foreign key (hotel_id, room_number) references room(hotel_id, number),
	foreign key (id) references booking(id),
	primary key (id)
);
