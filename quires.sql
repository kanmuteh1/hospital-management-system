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
    orang_number TEXT NOT NULL UNIQUE,
    lonestar_number TEXT NOT NULL UNIQUE,
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

CREATE TABLE diagnosis(
    id INTEGER,
    facility_id,
    patient_id,
    test_taken TEXT NOT NULL,
    diagnostic_result TEXT NOT NULL,
    diagnostic_date DATE NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (facility_id)REFERENCES facilities(facility_id),
    FOREIGN KEY (patient_id)REFERENCES patients(patient_id)
);

CREATE TABLE treaments(
    id INTEGER,
    facility_id,
    patient_id,
    purpose TEXT NOT NULL,
    prescription TEXT NOT NULL,
    prescription_discription TEXT NOT NULL,
    begin_date DATE NOT NULL,
    end_date DATE NOT NULL,
    PRIMARY KEY(id),    
    FOREIGN KEY (facility_id)REFERENCES facilities(facility_id),
    FOREIGN KEY (patient_id)REFERENCES patients(patient_id)
);




INSERT INTO facilities (facility_name,facility_address,funding_date,head_doctor,impact,history,email,orang_number,lonestar_number,password_hash) 
VALUES("Redmenption Hospital","New kru town",datetime('now'),"Dr.Moses Blackie","    Lorem ipsum dolor sit amet consectetur adipisicing elit. At magni dolorem cumque inventore praesentium quis suscipit ipsa nemo ratione vero. Molestias sunt eum consectetur labore nam eos at libero voluptate!Lorem
","    Lorem ipsum dolor sit amet consectetur adipisicing elit. At magni dolorem cumque inventore praesentium quis suscipit ipsa nemo ratione vero. Molestias sunt eum consectetur labore nam eos at libero voluptate!Lorem
","redemption@gmail.com","0778596321","0886243320","redemption123456789");

SELECT col1, col2, ...
 FROM ...
 WHERE ... 
 ORDER BY -- this is a MUST there must be ORDER BY statement
-- the paging comes here
OFFSET     10 ROWS       -- skip 10 rows
FETCH NEXT 10 ROWS ONLY; -- take 10 rows