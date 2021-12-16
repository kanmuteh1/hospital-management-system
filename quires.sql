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
    patient_name TEXT NOT NULL,
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
    facility_id,
    patient_id,
    facility_assign_num INT,
    PRIMARY KEY(id)
    FOREIGN KEY (facility_id)REFERENCES facilities(facility_id),
    FOREIGN KEY (patient_id)REFERENCES patients(patient_id)
);

-- services table
CREATE TABLE services(
    id INTEGER,
    facility_id,
    facility_service TEXT NOT NULL,
    about_service TEXT NOT NULL,
    PRIMARY KEY(id),
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
VALUES("St. Joseph Catholic Hospital","Catholic junction,congo",datetime('now'),"Dr.John Peters","    Lorem ipsum dolor sit amet consectetur adipisicing elit. At magni dolorem cumque inventore praesentium quis suscipit ipsa nemo ratione vero. Molestias sunt eum consectetur labore nam eos at libero voluptate!Lorem
","    Lorem ipsum dolor sit amet consectetur adipisicing elit. At magni dolorem cumque inventore praesentium quis suscipit ipsa nemo ratione vero. Molestias sunt eum consectetur labore nam eos at libero voluptate!Lorem
","stJosephcatholichospital@gmail.com","0777557321","0888244321","st.jch123456789");