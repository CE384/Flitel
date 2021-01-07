create view city_country (city_code, country_code, city_name, country_name)
    as select city.code, country_code, city.name, country.name
    from city join country on city.country_code = country.code;

create view hotels_info 
    as select hotel.name, hotel.id, city_name, country_name, stars_count
    from (hotel join city_country as CC
    on hotel.city_code= CC.city_code and hotel.country_code = CC.country_code);


create view hotels_rooms 
    as select hotel.name as hotel_name, hotel.id, room.number, type, capacity, price
    from hotel join room on hotel.id = room.hotel_id;


create view flight_info
    as select airline.name as airline_name, airline.id as airline_id, flight.number, price, departure_date, departure_time,
    CC1.city_name as origin_city_name, CC1.country_name as origin_country_name,
    CC2.city_name as destination_city_name, CC2.country_name as destination_country_name
    from (airline join flight on airline.id = flight.airline_id)
    join city_country as CC1
    on flight.origin_city_code=CC1.city_code and flight.origin_country_code = CC1.country_code
    join city_country as CC2
    on flight.destination_city_code=CC2.city_code and flight.destination_country_code = CC2.country_code;


create view airline_bookings_status
    as select costumer.name, FI.number, FI.origin_city_name, FI.origin_country_name,
    FI.destination_city_name, FI.destination_country_name, FI.departure_date,
    FI.departure_time, status, transaction_date, transaction_amount
    from booking join costumer on booking.costumer_id = costumer.id
    join (flight_booking as FB join flight_info as FI
        on FB.airline_id = FI.airline_id and FB.flight_number = FI.number)
        on booking.id = FB.id ;


create view hotel_bookings_status
    as select costumer.name, RB.hotel_id, RB.room_number, RB.from_date, RB.to_date, 
    status, transaction_date, transaction_amount
    from booking join costumer on booking.costumer_id = costumer.id
    join (room_booking as RB join room 
        on RB.hotel_id = room.hotel_id and RB.room_number = room.number)
    on booking.id = RB.id;
