-- facilities table
CREATE TABLE facilities(
    facility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_name TEXT NOT NULL,
    facility_address TEXT NOT NULL,
    funding_date DATE NOT NULL,
    head_doctor TEXT NOT NULL,
    impact TEXT NOT NULL,
    history TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    orang_number TEXT NOT NULL UNIQUE,
    lonestar_number TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL UNIQUE
);

-- patient table
CREATE TABLE patients(
    patient_id INTEGER,
    patient_name TEXT NOT NULL UNIQUE,
    patient_address TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    email TEXT NOT NULL UNIQUE,
    orang_number TEXT NOT NULL,
    lonestar_number TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    PRIMARY KEY(patient_id)
);

-- registration table
CREATE TABLE registration(
    id INTEGER,
    facility_id INT,
    patient_id INT,
    account_num INT NOT NULL,
    account_pin INT NOT NULL,
    facility_assign_num INT,
    registration_date DATE NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (facility_id)REFERENCES facilities(facility_id),
    FOREIGN KEY (patient_id)REFERENCES patients(patient_id)
);

-- services table
CREATE TABLE services(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facility_id INT,
    facility_service TEXT NOT NULL,
    about_service TEXT NOT NULL,
    FOREIGN KEY (facility_id)REFERENCES facilities(facility_id)
);
