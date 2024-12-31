-- Create the main table for student registration
CREATE TABLE registrations (
    id SERIAL PRIMARY KEY, -- Auto-incrementing unique ID
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('male', 'female')) NOT NULL,
    grade VARCHAR(20) NOT NULL,
    start_date DATE NOT NULL,
    parent_first_name VARCHAR(50) NOT NULL,
    parent_last_name VARCHAR(50) NOT NULL,
    relationship VARCHAR(20) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    address TEXT NOT NULL,
    emergency_contact_name VARCHAR(50) NOT NULL,
    emergency_relationship VARCHAR(20) NOT NULL,
    emergency_contact_number VARCHAR(15) NOT NULL,
    emergency_alternate_number VARCHAR(15),
    medical_condition BOOLEAN NOT NULL DEFAULT FALSE,
    medical_details TEXT,
    medications BOOLEAN NOT NULL DEFAULT FALSE,
    medications_details TEXT,
    previous_school_name VARCHAR(100),
    previous_school_address TEXT,
    previous_school_contact VARCHAR(15),
    transportation BOOLEAN NOT NULL DEFAULT FALSE,
    additional_info TEXT,
    signature TEXT NOT NULL,
    registration_date DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Create an index for fast search on frequently queried columns
CREATE INDEX idx_registrations_email ON registrations (email);
CREATE INDEX idx_registrations_grade ON registrations (grade);

-- Optional: A separate table for medical conditions if needed
CREATE TABLE medical_conditions (
    id SERIAL PRIMARY KEY,
    registration_id INT REFERENCES registrations(id) ON DELETE CASCADE,
    condition_details TEXT NOT NULL
);

-- Optional: A separate table for emergency contacts if needed
CREATE TABLE emergency_contacts (
    id SERIAL PRIMARY KEY,
    registration_id INT REFERENCES registrations(id) ON DELETE CASCADE,
    contact_name VARCHAR(50) NOT NULL,
    relationship VARCHAR(20) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    alternate_number VARCHAR(15)
);

-- Optional: A separate table for previous school details if needed
CREATE TABLE previous_schools (
    id SERIAL PRIMARY KEY,
    registration_id INT REFERENCES registrations(id) ON DELETE CASCADE,
    school_name VARCHAR(100),
    school_address TEXT,
    contact_number VARCHAR(15)
);
