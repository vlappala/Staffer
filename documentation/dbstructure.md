# Create-lauseet tietokannan alustukseen:

    CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id));
	
    CREATE TABLE production (
	id INTEGER NOT NULL, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	show_duration_hours INTEGER NOT NULL, 
	show_duration_minutes INTEGER NOT NULL, 
	misc_info VARCHAR(2000), 
	PRIMARY KEY (id));

    CREATE TABLE role (
	id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	role_name VARCHAR(144) NOT NULL, 
	date_modified DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id));

    CREATE TABLE show (
	id INTEGER NOT NULL, 
	show_date DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	production_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(production_id) REFERENCES production (id));

    CREATE TABLE shift (
	id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	show_id INTEGER NOT NULL, 
	date_modified DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (account_id, show_id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(show_id) REFERENCES show (id));

    CREATE TABLE shiftdetails (
	id INTEGER NOT NULL, 
	shift_id INTEGER NOT NULL, 
	shift_role VARCHAR(144), 
	shift_locked BOOLEAN NOT NULL, 
	shift_completed BOOLEAN NOT NULL, 
	shift_billed BOOLEAN NOT NULL, 
	date_modified DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(shift_id) REFERENCES shift (id), 
	CHECK (shift_locked IN (0, 1)), 
	CHECK (shift_completed IN (0, 1)), 
	CHECK (shift_billed IN (0, 1)));

