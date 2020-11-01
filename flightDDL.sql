create table users
(
    uname varchar(20) not null,
    passwd varchar(100) not null,
    pno varchar(20) not null,
    first_name varchar(20) not null,
    last_name varchar(20) not null,
    DOB date not null,
    phone_no int(10) not null,
    address varchar(50),
    primary key(uname)
);

create table userMakesPayment
(
	uname varchar(20),
	ticket_id varchar(10),
	primary key (uname, ticket_id),
	foreign key (uname) references users (uname)
	on delete cascade,
	foreign key (ticket_id) references ticket (ticket_id)
	on delete cascade
);

create table ticket
(
    ticket_id varchar(10) not null,
    uname varchar(20),
    flight_id varchar(10),
    status varchar(10),
    price int,
    primary key(ticket_id),
    foreign key (uname) references users (uname)
    on delete set null,
    foreign key (flight_id) references flight (flight_id)
    on delete cascade
);

create table booking
(
	ticket_id varchar(10),
	flight_id varchar(10),
	foreign key (ticket_id) references ticket (ticket_id)
    on delete set null,
	foreign key (flight_id) references flight (flight_id)
    on delete cascade
);

create table flight
(
    flight_id varchar(10) not null,
    arrival time,
    departure time,
    source varchar(15) not null,
    destination varchar(15) not null,
    route varchar(10),
    model varchar(15),
    manufacturer varchar(15),
    count_ticket int,
    primary key(flight_id)
);

create table flightScheduledForAirline
(
	airline_id varchar(10),
	flight_id varchar(10),
	foreign key (airline_id) references airline (airline_id)
    on delete cascade,
	foreign key (flight_id) references flight (flight_id)
    on delete set null
);

create table airline
(
    airline_id varchar(10) not null,
    airline_name varchar(20),
    primary key(airline_id)
);

create table airportContainsAirline
(
	airline_id varchar(10),
	location_code varchar(4),
	foreign key (airline_id) references airline (airline_id)
    on delete cascade,
    foreign key (location_code) references airport (location_code)
    on delete cascade
);

create table airport
(
    location_code varchar(4) not null,
    city varchar(15) not null,
    primary key(location_code)
);

