insert into country values (1, 'Iran');
insert into country values (2, 'Turkey');
insert into country values (3, 'USA');
insert into country values (4, 'Canada');
insert into country values (5, 'England');

insert into city values (1, 1, 'Tehran');
insert into city values (1, 2, 'Mashhad');
insert into city values (2, 1, 'Istanbul');
insert into city values (2, 2, 'Ankara');
insert into city values (3, 1, 'Washington');
insert into city values (3, 2, 'New York');
insert into city values (4, 1, 'Toronto');
insert into city values (4, 2, 'Vancouver');
insert into city values (5, 1, 'London');
insert into city values (5, 2, 'Manchester');

insert into user_table values (1, 'customer', 'saba', '123');
insert into user_table values (2, 'customer', 'kimia', '123');
insert into user_table values (3, 'hotel', 'hotel_1', '123');
insert into user_table values (4, 'hotel', 'hotel_2', '123');
insert into user_table values (5, 'hotel', 'hotel_3', '123');
insert into user_table values (6, 'hotel', 'hotel_4', '123');
insert into user_table values (7, 'hotel', 'hotel_5', '123');
insert into user_table values (8, 'hotel', 'hotel_6', '123');
insert into user_table values (9, 'hotel', 'hotel_7', '123');
insert into user_table values (10, 'hotel', 'hotel_8', '123');
insert into user_table values (13, 'airline', 'airline_1', '123');
insert into user_table values (14, 'airline', 'airline_2', '123');
insert into user_table values (15, 'airline', 'airline_3', '123');
insert into user_table values (16, 'airline', 'airline_4', '123');

insert into customer values (1, '1', 'saba hashemi', 'tehran', '123456789', 'savaw97@gmail.com');
insert into customer values (2, '2', 'kimia noorbakhsh', 'tehran', '123456789', 'kimianoorbakhsh@gmail.com');

insert into airline values (13, 'mahan air', 'Mahan Airlines, operating under the name Mahan Air is a privately owned Iranian airline based in Tehran, Iran.');
insert into airline values (14, 'turkish airlines', 'Turkish Airlines is the national flag carrier airline of Turkey.');
insert into airline values (15, 'united airlines', 'United Airlines, Inc. is a major American airline headquartered at Willis Tower in Chicago, Illinois.');
insert into airline values (16, 'british airways', 'British Airways is the flag carrier airline of the United Kingdom.');


insert into hotel (id, name, description, phone, facilities, address, website, stars_count, country_code, city_code) values 
						(3,
						  'espinas palace',
						  'The 5-Star Epinas Palace Hotel located in the best residential and commercial part of Tehran, Iran.',
						 '982175675000', 
						 'Espinas Palace Hotel is a hotel with a flair for services. A stay in the Palace is always a special time for our guests. The Palace features all the amenities and services of a luxury five-star hotel coupled with attraction and a unique feel-at-home atmosphere',
						 'Tehran, Iran', 'https://espinashotels.com/', 5, 1, 1);
insert into hotel (id, name, description, phone, facilities, address, website, stars_count, country_code, city_code) values 
						(4,
						  'almas',
						  'The 4-Star Almas Hotel in Mashhad-Iran incorporating luxury and elegance Opened in March 2017.',
						 '985131414000', 
						 ' Lobby, Lobby lounge, Coffee Shop Firoozeh Restaurant, Panorama Revolving Rooftop Restaurant Roof Garden Restaurant & Café.',
						 'Mashhad, Iran', '', 4, 1, 2);						 
insert into hotel (id, name, description, phone, facilities, address, website, stars_count, country_code, city_code) values 
						 (5,
						  'marmara deluxe hotel',
						  'Hotel Istanbul is in the middle of the historical Sultanahmet area.',
						 '902125202777', 
						 'Marmara Deluxe Hotel has a very special location, in the middle of the historical peninsula (half-island) that makes the cultures & religions meet, where the Asia and Europe greet each other and also a location that available to go by foot to the most important places that visitors of Istanbul have to visit firstly.',
						 'Istanbul, Turkey', 'http://www.marmarahoteldeluxe.com/', 3, 2, 1);					 
insert into hotel (id, name, description, phone, facilities, address, website, stars_count, country_code, city_code) values 
				(6,
						  'Metropolitan Hotel Ankara',
						  '5 HRS Stars Metropolitan Hotels Ankara in Ankara (Ankara)',
						 '903122954545', 
						 'Located in the city center of Ankara, Metropolitan Hotels Ankara offers modern rooms with luxury design, soundproofing, and air conditioning. The hotel has free private parking on site.',
						 'Ankara, Turkey', '', 5, 2, 2);						 
insert into hotel (id, name, description, phone, facilities, address, website, stars_count, country_code, city_code) values 
						(7,
						  'Grand Hyatt Washington',
						  'Grand Hyatt Washington places you in the heart of Washington, D.C.',
						 '12025821234', 
						 'The WMATA Metro Center train station is directly connected to our lobby, so you can board the red, orange, silver, or blue line and easily navigate the city.',
						 'Washington, USA', 'https://www.hyatt.com/', 4, 3, 1);						 
insert into hotel (id, name, description, phone, facilities, address, website, stars_count, country_code, city_code) values 
					 (8,
						  'The Langham',
						  'Chic contemporary style that inspires. Ultimate location on Fifth Avenue. Personalised service that is genuine. Culinary delights that captivate. A stay at The Langham, New York, Fifth Avenue is unlike any other.',
						 '12126954005', 
						 'Contemporary luxury. Urban sophistication. 234 residentially-styled guest rooms and suites designed to relax, inspire, and surprise. Each furnished with indulgent amenities such as Swedish Duxiana beds and large marble-clad bathrooms with rainfall showers. Many  highlighted by views of the iconic Manhattan skyline that is framed by the oversized glass windows.',
						 'New York, USA', 'https://www.langhamhotels.com/', 5, 3, 2);					 
insert into hotel (id, name, description, phone, facilities, address, website, stars_count, country_code, city_code) values 
					(9,
						  'Bond Place Hotel Toronto',
						  'At the foot of Yonge and Dundas square, stationed in the center of Toronto’s playground.',
						 '14163626061', 
						 'ount sheep in our beautifully curated rooms. Plot your next adventure from our bright and social lobby. Submerse yourself in Toronto life from our convenient location.',
						 'Toronto, Canada', 'https://www.bondplace.ca/the-hotel/', 3, 4, 1);				 
insert into hotel (id, name, description, phone, facilities, address, website, stars_count, country_code, city_code) values 
						(10,
						  'Blakemore Hyde Park Hotel',
						  'The Blakemore Hyde Park, A cosmopolitan four-star London hotel',
						 '14163626061', 
						 'A warm welcome to our stylish, vibrant hotel, just a short stroll from Paddington Station and a few minutes from the relaxing calm of Hyde Park. Located on a quiet, residential street but within walking distance of key transport links, our hotel is the perfect London base, for both business and leisure guests.',
						 'London, England', 'https://www.blakemorehydepark.com/', 4, 5, 1);
						 
insert into room values (3, 1, '1 bed', '1', '100');
insert into room values (3, 2, '1 bed', '1', '100');
insert into room values (3, 3, '2 beds', '3', '200');
insert into room values (3, 4, '2 beds', '3', '200');
insert into room values (3, 5, 'suite', '5', '400');
insert into room values (3, 6, 'suite', '5', '400');
insert into room values (4, 1, '1 bed', '1', '100');
insert into room values (4, 2, '1 bed', '1', '100');
insert into room values (4, 3, '2 beds', '3', '200');
insert into room values (4, 4, '2 beds', '3', '200');
insert into room values (4, 5, 'suite', '5', '400');
insert into room values (4, 6, 'suite', '5', '400');
insert into room values (5, 1, '1 bed', '1', '100');
insert into room values (5, 2, '1 bed', '1', '100');
insert into room values (5, 3, '2 beds', '3', '200');
insert into room values (5, 4, '2 beds', '3', '200');
insert into room values (5, 5, 'suite', '5', '400');
insert into room values (5, 6, 'suite', '5', '400');
insert into room values (6, 1, '1 bed', '1', '100');
insert into room values (6, 2, '1 bed', '1', '100');
insert into room values (6, 3, '2 beds', '3', '200');
insert into room values (6, 4, '2 beds', '3', '200');
insert into room values (6, 5, 'suite', '5', '400');
insert into room values (6, 6, 'suite', '5', '400');
insert into room values (7, 1, '1 bed', '1', '100');
insert into room values (7, 2, '1 bed', '1', '100');
insert into room values (7, 3, '2 beds', '3', '200');
insert into room values (7, 4, '2 beds', '3', '200');
insert into room values (7, 5, 'suite', '5', '400');
insert into room values (7, 6, 'suite', '5', '400');
insert into room values (8, 1, '1 bed', '1', '100');
insert into room values (8, 2, '1 bed', '1', '100');
insert into room values (8, 3, '2 beds', '3', '200');
insert into room values (8, 4, '2 beds', '3', '200');
insert into room values (8, 5, 'suite', '5', '400');
insert into room values (8, 6, 'suite', '5', '400');
insert into room values (9, 1, '1 bed', '1', '100');
insert into room values (9, 2, '1 bed', '1', '100');
insert into room values (9, 3, '2 beds', '3', '200');
insert into room values (9, 4, '2 beds', '3', '200');
insert into room values (9, 5, 'suite', '5', '400');
insert into room values (9, 6, 'suite', '5', '400');
insert into room values (10, 1, '1 bed', '1', '100');
insert into room values (10, 2, '1 bed', '1', '100');
insert into room values (10, 3, '2 beds', '3', '200');
insert into room values (10, 4, '2 beds', '3', '200');
insert into room values (10, 5, 'suite', '5', '400');
insert into room values (10, 6, 'suite', '5', '400');

insert into flight values (13, 3, 'economy', 100, 200, 1, 1, 5, 1, '2021-02-25', '12:00:00'); -- tehran-london
insert into flight values (15, 3, 'economy', 100, 200, 3, 1, 5, 2, '2021-02-24', '13:00:00'); -- washington-manchester
insert into flight values (16, 3, 'economy', 100, 200, 5, 1, 5, 2, '2021-02-25', '15:00:00'); -- london- manchester

insert into flight values (13, 1, 'economy', 100, 100, 1, 1, 1, 2, '2021-01-08', '14:00:00'); -- tehran-mashhad
insert into flight values (13, 2, 'economy', 100, 200, 1, 1, 5, 1, '2021-01-09', '15:00:00'); -- tehran-london
insert into flight values (14, 1, 'economy', 100, 100, 2, 1, 1, 1, '2021-01-08', '14:00:00'); -- istabbul-tehran
insert into flight values (14, 2, 'economy', 100, 200, 2, 1, 3, 2, '2021-01-09', '15:00:00'); --istanbul-new york
insert into flight values (15, 1, 'economy', 100, 100, 3, 1, 3, 2, '2021-01-08', '14:00:00'); --washington-newyork
insert into flight values (15, 2, 'economy', 100, 200, 3, 1, 5, 2, '2021-01-09', '15:00:00'); -- washington-manchester
insert into flight values (16, 1, 'economy', 100, 100, 3, 1, 5, 1, '2021-01-08', '14:00:00'); -- washington-london
insert into flight values (16, 2, 'economy', 100, 200, 5, 1, 5, 2, '2021-01-09', '15:00:00'); -- london- manchester


insert into discount values('dis1', 10);
insert into discount values('dis2', 50);
insert into discount values('dis3', 20);
insert into discount values('dis4', 60);
