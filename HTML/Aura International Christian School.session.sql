CREATE DATABASE IF NOT EXISTS register_student;

USE register_student;

CREATE TABLE student_registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('male', 'female', 'other') NOT NULL,
    grade_applied_for VARCHAR(20) NOT NULL,
    preferred_start_date DATE NOT NULL,
    parent_first_name VARCHAR(50) NOT NULL,
    parent_last_name VARCHAR(50) NOT NULL,
    relationship_to_student VARCHAR(30) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email_address VARCHAR(100) NOT NULL,
    home_address TEXT NOT NULL,
    emergency_contact_name VARCHAR(50) NOT NULL,
    emergency_relationship VARCHAR(30) NOT NULL,
    emergency_contact_number VARCHAR(15) NOT NULL,
    emergency_alternate_number VARCHAR(15),
    medical_conditions TEXT,
    medications TEXT,
    previous_school_name VARCHAR(100),
    previous_school_address TEXT,
    previous_school_contact VARCHAR(15),
    transportation_required ENUM('yes', 'no') NOT NULL,
    additional_info TEXT,
    parent_signature VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL
);

