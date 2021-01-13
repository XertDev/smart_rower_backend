CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

create type clientrole as enum ('ADMIN', 'NORMAL');
create type scooterstate as enum ('AVAILABLE', 'IN_RUN', 'DISABLED');

create table if not exists clients
(
	id serial not null
		constraint clients_pkey
			primary key,
	role clientrole not null,
	email varchar not null,
	name varchar not null,
	surname varchar not null,
	password_hash varchar not null,
	start_account_date timestamp not null
);

create unique index if not exists clients_email_uindex
	on clients (email);

create table if not exists scooters
(
	id serial not null
		constraint scooters_pkey
			primary key,
    battery_model varchar(80) not null,
    mac varchar(80) not null,
    vehicle_type integer not null,
	state scooterstate default 'AVAILABLE'::scooterstate not null
);

create table if not exists client_subscriptions
(
	id serial not null
		constraint client_subscriptions_pkey
			primary key,
	client_id integer not null
		constraint client_subscriptions_client_id_fkey
			references clients,
	start_time timestamp not null,
	end_time timestamp not null
);

create table if not exists scooter_info
(
	actual_time timestamp not null,
	scooter_id integer not null
		constraint scooter_info_scooter_id_fkey
			references scooters,
	location geometry(Point) not null,
	battery_level float not null,
	battery_temp float not null,
	battery_cycle integer not null,
	is_charging bool not null,
	is_locked bool not null,
	is_riding bool not null,
	reserved_by integer,
	ready_to_ride bool not null,
	zone_id int not null,

	constraint scooter_info_pkey
		primary key (scooter_id, actual_time),
);

create index if not exists idx_scooter_info_location
	on scooter_info (location);

create index if not exists scooter_info_location_index
	on scooter_info (location);

create index if not exists scooter_info_timestamp_index
	on scooter_info (timestamp desc);

create table if not exists rides
(
	id serial not null
		constraint rides_pkey
			primary key,
	client_id integer not null
		constraint rides_client_id_fkey
			references clients,
	scooter_id integer not null
		constraint scooter_id_fkey
			references scooters,
    kilometers_distance float not null,
    pricing float not null,
	start_time timestamp not null,
	end_time timestamp,
	constraint rides_scooter_id_start_time_fkey
		foreign key (scooter_id, start_time) references scooter_info (scooter_id, actual_time),
	constraint rides_scooter_id_end_time_fkey
		foreign key (scooter_id, end_time) references scooter_info (scooter_id, actual_time)
);