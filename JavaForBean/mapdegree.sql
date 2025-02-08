CREATE DATABASE DegreeProgress;
USE DegreeProgress;

-- Table for storing student details
CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    major_id INT,
    enrollment_year YEAR,
    expected_graduation_year YEAR,
    total_credits_earned INT DEFAULT 0,
    gpa DECIMAL(3,2) DEFAULT 0.00,
    FOREIGN KEY (major_id) REFERENCES Majors(major_id)
);

-- Table for majors and minors
CREATE TABLE Majors (
    major_id INT PRIMARY KEY AUTO_INCREMENT,
    major_name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL
);

-- Table for courses
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL CHECK (credits > 0),
    category ENUM('Major', 'Elective', 'NUPath'),
    prerequisite_id INT,
    offered_semester ENUM('Fall', 'Spring', 'Summer One', 'Summer Two', 'all'),
    FOREIGN KEY (prerequisite_id) REFERENCES Courses(course_id) ON DELETE SET NULL
);

-- Table to define degree requirements
CREATE TABLE DegreeRequirements (
    degree_id INT PRIMARY KEY AUTO_INCREMENT,
    major_id INT,
    total_required_credits INT NOT NULL,
    required_gpa DECIMAL(3,2) DEFAULT 2.00,
    core_courses_required INT,
    elective_credits_required INT,
    capstone_required BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (major_id) REFERENCES Majors(major_id)
);

-- Table for student course enrollments
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    semester_taken VARCHAR(10),
    grade VARCHAR(2),
    credits_earned INT DEFAULT 0,
    status ENUM('Completed', 'In Progress', 'Failed'),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Table for tracking completed credits
CREATE TABLE CompletedCredits (
    student_id INT PRIMARY KEY,
    credits_needed INT,
    total_credits_earned INT DEFAULT 0,
    remaining_credits INT DEFAULT 0,
    gpa DECIMAL(3,2) DEFAULT 0.00,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Table for transfer or AP credits
CREATE TABLE TransferCredits (
    credit_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    source ENUM('AP', 'Transfer', 'CLEP', 'IB'),
    equivalent_course_id INT,
    credits_awarded INT CHECK (credits_awarded > 0),
    hours_awarded INT DEFAULT 0,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (equivalent_course_id) REFERENCES Courses(course_id)
);
