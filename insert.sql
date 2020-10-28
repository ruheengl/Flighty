insert into airport (city, location_code) values ('Chandigarh', 'IXC');
insert into airport (city, location_code) values ('Delhi', 'DEL');
insert into airport (city, location_code) values ('Fort Worth', 'DFW');
insert into airport (city, location_code) values ('Frankfurt', 'FRA');
insert into airport (city, location_code) values ('Houston', 'IAH');
insert into airport (city, location_code) values ('Louisville', 'SDF');
insert into airport (city, location_code) values ('Mumbai', 'BOM');
insert into airport (city, location_code) values ('New York City', 'JFK');
insert into airport (city, location_code) values ('San Francisco', 'SFO');
insert into airport (city, location_code) values ('Tampa', 'TPA');


insert into airline (airline_id, airline_name) values('AA','American Airlines');
insert into airline (airline_id, airline_name) values('AI','Air India Limited');
insert into airline (airline_id, airline_name) values('LH','Lufthansa');
insert into airline (airline_id, airline_name) values('BA','British Airways');
insert into airline (airline_id, airline_name) values('QR','Qatar Airways');
insert into airline (airline_id, airline_name) values('9W','Jet Airways');
insert into airline (airline_id, airline_name) values('EK','Emirates');
insert into airline (airline_id, airline_name) values('EY','Etihad Airways');


insert into airportContainsAirline (airline_id, location_code) values('AA','SDF');
insert into airportContainsAirline (airline_id, location_code) values('AA','JFK');
insert into airportContainsAirline (airline_id, location_code) values('AA','IAH');
insert into airportContainsAirline (airline_id, location_code) values('AA','SFO');
insert into airportContainsAirline (airline_id, location_code) values('AA','TPA');

insert into airportContainsAirline (airline_id, location_code) values('AI','IXC');
insert into airportContainsAirline (airline_id, location_code) values('AI','DFW');
insert into airportContainsAirline (airline_id, location_code) values('AI','DEL');
insert into airportContainsAirline (airline_id, location_code) values('AI','BOM');
insert into airportContainsAirline (airline_id, location_code) values('AI','IAH');

insert into airportContainsAirline (airline_id, location_code) values('LH','BOM');
insert into airportContainsAirline (airline_id, location_code) values('LH','FRA');
insert into airportContainsAirline (airline_id, location_code) values('LH','JFK');
insert into airportContainsAirline (airline_id, location_code) values('LH','SFO');
insert into airportContainsAirline (airline_id, location_code) values('LH','DFW');

insert into airportContainsAirline (airline_id, location_code) values('BA','JFK');
insert into airportContainsAirline (airline_id, location_code) values('BA','BOM');
insert into airportContainsAirline (airline_id, location_code) values('BA','IXC');
insert into airportContainsAirline (airline_id, location_code) values('BA','FRA');
insert into airportContainsAirline (airline_id, location_code) values('BA','SFO');

insert into airportContainsAirline (airline_id, location_code) values('QR','BOM');
insert into airportContainsAirline (airline_id, location_code) values('QR','DFW');
insert into airportContainsAirline (airline_id, location_code) values('QR','JFK');
insert into airportContainsAirline (airline_id, location_code) values('QR','TPA');
insert into airportContainsAirline (airline_id, location_code) values('QR','SDF');


insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('AI2014','02:10:00','03:15:00','Mumbai','Fort Worth','Connecting',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('QR2305','13:00:00','13:55:00','Mumbai','Fort Worth','Nonstop',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('EY1234','19:20:00','20:05:00','New York City','Tampa','Connecting',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('LH9876','05:50:00','06:35:00','New York City','Mumbai','Nonstop',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('BA1689','10:20:00','10:55:00','Frankfurt','Delhi','Nonstop',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('AA4367','18:10:00','18:55:00','San Francisco','Frankfurt','Nonstop',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('QR1902','22:00:00','22:50:00','Chandigarh','Houston','Nonstop',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('BA3056','02:15:00','02:55:00','Mumbai','Fort Worth','Connecting',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('EK3456','18:50:00','19:40:00','Mumbai','San Francisco','Nonstop',0);
insert into flight (flight_id, arrival, departure, source, destination, route, count_ticket) 
values('9W2334','23:00:00','13:45:00','Houston','Delhi','Direct',0);


insert into flightScheduledForAirline (airline_id, flight_id) values('AI','AI2014');
insert into flightScheduledForAirline (airline_id, flight_id) values('QR','QR2305');
insert into flightScheduledForAirline (airline_id, flight_id) values('EY','EY1234');
insert into flightScheduledForAirline (airline_id, flight_id) values('LH','LH9876');
insert into flightScheduledForAirline (airline_id, flight_id) values('BA','BA1689');
insert into flightScheduledForAirline (airline_id, flight_id) values('AA','AA4367');
insert into flightScheduledForAirline (airline_id, flight_id) values('QR','QR1902');
insert into flightScheduledForAirline (airline_id, flight_id) values('BA','BA3056');
insert into flightScheduledForAirline (airline_id, flight_id) values('EK','EK3456');
insert into flightScheduledForAirline (airline_id, flight_id) values('9W','9W2334');