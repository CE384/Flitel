
create function check_room_empty()
  returns trigger as
$func$
begin
    if (exists 
        (select from_date, to_date from room_booking 
        where hotel_id=new.hotel_id and room_number=new.room_number
        and not (to_date < new.from_date or new.to_date < from_date))) 
    then
        raise exception 'This room is not available for the selected dates.';
    end if;
    return new;
end
$func$  language plpgsql;

create trigger check_room_empty
before insert on room_booking 
for each row  execute procedure check_room_empty();


create function check_flight_has_capacity()
  returns trigger as
$func$
begin
    if (select remained_seats from flight_info
        where airline_id=new.airline_id and number=new.flight_number) = 0
    then
        raise exception 'This flight doesnt have enough seats.';
    end if;
    return new;
end
$func$ language plpgsql;

create trigger check_flight_has_capacity
before insert on flight_booking
for each row execute procedure check_flight_has_capacity();
